# -*- coding: utf-8 -*-

import serial


#
# There are two type of frame for the VEdirect protocol: text frame and hex frame.
#
# Text frame are leaded by two bytes: 0x0D, 0X0A ("\r\n"), end by keyword
# 'Checksum\t\0x??'. This makes the receiver very easy to find the end of the
# the frame if processed by stream. But if you missed the start of the frame,
# there is no way to find the end of it.
#
# Text frame checksum are (all bytes sum + Checksum byte) & 0xFF == 0.
#
# Hex frame are leaded by colon(":"), anytime the colon appears, the previous
# frame terminated immediately and switch to the start of a hex frame. The
# byte 0x0A is the end of a hex frame. e.g.:
#
# Beside the leading colon(":"), the whole hex frame are build only by hex
# characters: '0'-'9','A'-'F', and t
#
class Venew:

    def __init__(self, serialport, timeout):
        self.debug = False
        self.serialport = serialport
        self.ser = serial.Serial(serialport, 19200, timeout=timeout)
        self.header1 = ord('\r') #0x0D
        self.header2 = ord('\n') #0x0A
        self.hexmarker = ord(':') #0x3A
        self.delimiter = ord('\t') #0x09

    (FRAME_ALL, FRAME_TEXT, FRAME_HEX) = range(3)

    def readFrame(self, frameType = FRAME_ALL):
        while True:
            b = self.ser.read()
            print(b, end="      ", flush = True)



    (HEX, WAIT_HEADER, IN_KEY, IN_VALUE, IN_CHECKSUM) = range(5)

    def input(self, byte):
        if byte == self.hexmarker and self.state != self.IN_CHECKSUM:
            self.state = self.HEX

        if self.state == self.WAIT_HEADER:
            self.bytes_sum += byte
            if byte == self.header1:
                self.state = self.WAIT_HEADER
            elif byte == self.header2:
                self.state = self.IN_KEY

            return None
        elif self.state == self.IN_KEY:
            self.bytes_sum += byte
            if byte == self.delimiter:
                if (self.key == 'Checksum'):
                    self.state = self.IN_CHECKSUM
                else:
                    self.state = self.IN_VALUE
            else:
                self.key += chr(byte)
            return None
        elif self.state == self.IN_VALUE:
            self.bytes_sum += byte
            if byte == self.header1:
                self.state = self.WAIT_HEADER
                self.dict[self.key] = self.value;
                self.key = '';
                self.value = '';
            else:
                self.value += chr(byte)
            return None
        elif self.state == self.IN_CHECKSUM:
            self.bytes_sum += byte
            self.key = ''
            self.value = ''
            self.state = self.WAIT_HEADER
            if (self.bytes_sum % 256 == 0):
                self.bytes_sum = 0
                return self.dict
            else:
                self.bytes_sum = 0
        elif self.state == self.HEX:
            self.bytes_sum = 0
            if byte == self.header2:
                self.state = self.WAIT_HEADER
                return self.hex_array
            else:
                self.hex_array.append(byte)

        else:
            raise AssertionError()

    # Device will broadcast human readable information every second.
    # Set skip_broadcast to True will skip this info and try to grab hex result only.
    def read_data_single(self, skip_broadcast = False):
        self.data_init()
        i = []
        broadcast_cnt = 0
        while True:
            data = self.ser.read()
            for single_byte in data:
                i.append(single_byte)
                packet = self.input(single_byte)
                if (packet != None):
                    if skip_broadcast and i[0]!=ord(':') and broadcast_cnt < 10:
                        i=[]
                        broadcast_cnt +=1
                    else:
                        self.dump_int_array(i, "Result")
                        return packet

    def read_data_callback(self, callbackFunction):
        # command ping
        #self.ser.write([self.hexmarker,ord('1'),ord('5'),ord('4'),self.header2])
        # 3a:35:35:34:34:31:42:42:0a   raw data
        # :  5  5  4  4  1  2  2    conver to asc
        # :=hex mode, 5 = ping, 5441 is the real data 0x4154 = version 1.54  ?

        # command: get Battery absorption voltage
        # "7F7ED006A" 7=get, F7ED=0xEDF7 = absorption voltage, 00=always zero, 6A checksum = 07 + FE + ED + 00 + 6A = 0x255
        # 除了指令是1个字符，其余都是两个字符表示一个0xFF，计算checksum的时候用这种奇怪的拆解进行计算
        # self.ser.write([self.hexmarker,ord('7'),ord('F'),ord('7'),ord('E'),ord('D'),ord('0'),ord('0'),ord('6'),ord('A'),self.header2])
        #3a:37:46:37:45:44:30:30:39:43:30:39:43:35:0a raw raw_data
        # :  7  F  7  E  D  0  0  9  C  0  9  C  5   先转换成字符串，
        # 0x099C = 2460 = 24.60v   然后获得真正的数据，再decoding。同样的，需要知道这个字符串中对应的字段是 uint8还是uint16

        i = []
        while True:
            data = self.ser.read()
            for byte in data:
                i.append(byte)
                packet = self.input(byte)
                if (packet != None):
                    self.dump_int_array(i, "Result")
                    i = []
                    callbackFunction(packet)

    # Send hex command to Victron SmartSolar Charge Controller
    # e.g. send_command(":7F0ED00") = Get Battery maximum current
    #       return value: ":7F7ED009C09C5"
    # e.g. send_command(":1") = Ping Device
    # Please refer for BlueSolar-HEX-protocol-MPPT.pdf for detailed info.
    def send_command(self, cmd):
        i = []
        checksum = 0
        is_high = True

        for c in cmd:
            i.append(ord(c))
            if c!=':':
                checksum += int(c,16)*16 if is_high else int(c,16)
            is_high = not is_high

        check_result = (0x155 - checksum & 0xFF) & 0xff
        for c in "{:02X}".format(check_result):
            i.append(ord(c))
        i.append(self.header2)
        self.dump_int_array(i, "Command")
        self.ser.write(i)

        raw_res = self.read_data_single(True)
        return "".join(chr(c) for c in raw_res)

        # todo return value checksum veirfication
        # 所有返回的命令必须跟发出的命令匹配才有意义，否则就是错的

    def dump_int_array(self, i, comment):
        if self.debug:
            print (comment)
            print("".join(chr(c) for c in i))
            print(".".join("{:02x}".format(c) for c in i))
