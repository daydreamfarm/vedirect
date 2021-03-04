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
# byte 0x0A ('\n') is the end of a hex frame. e.g.:
#
# Beside the leading colon(":"), the whole hex frame are build only by hex
# characters: '0'-'9','A'-'F'.
#
#
# Command: ping
# Command string:
#    ':0154\n'
# Code:
#    self.ser.write([self.hexmarker,ord('1'),ord('5'),ord('4'),self.header2])
# Reponse
#    3a:35:35:34:34:31:42:42:0a   Raw data
#    :  5  5  4  4  1  2  2  \n   ASCII string
# Explaination:
#  := hex mode,
#  5 = response of ping
#  5441 data in little endian format, hex data is 0x4154 = version 1.54
#
# Command: get Battery absorption voltage
# Command String:
#   ':7F7ED006A\n'
# Code:
#   self.ser.write([self.hexmarker,ord('7'),ord('F'),ord('7'),ord('E'),ord('D'),ord('0'),ord('0'),ord('6'),ord('A'),self.header2])
# Command Explaination:
#   7 = Get params
#   F7ED = 0xEDF7 = params: absorption voltage
#   00 = Flags sub byte, always zero
#   6A = checksum = 07 + FE + ED + 00 + 6A = 0x255 & 0x55 = 0
# Response:
#   3a:37:46:37:45:44:30:30:39:43:30:39:43:35:0a Raw data
#   :  7  F  7  E  D  0  0  9  C  0  9  C  5  \n ASCII string
# Data:
#  data is four bytes (int 16) just follow the command in this case,
# '9C09' = 0x099C = 2460 = 24.60v


class Vedirect:
    # Send hex command to Victron SmartSolar Charge Controller
    # e.g. send_command("7F0ED00") = Get Battery maximum current
    #       return value: ":7F7ED009C09C5"
    # e.g. send_command("1") = Ping Device
    # Please refer for BlueSolar-HEX-protocol-MPPT.pdf for detailed info.
    def send_command(self, cmd):
        hex_command = self.gen_hex_command(cmd)
        for i in range(10):
            self.dump_int_array(hex_command, "Command")
            self.ser.write(hex_command)
            raw_res = self.read_frame(self.FRAME_HEX)
            if raw_res and raw_res[0]==chr(self.hexmarker) and self.hex_checksum(raw_res) == 0:
                self.err_msg = ""
                return raw_res
        self.err_msg = "No valid response!"
        return False

        # todo return value checksum veirfication
        # 所有返回的命令必须跟发出的命令匹配才有意义，否则就是错的

    def read_text_frame(self):
        self.dump_int_array("Read Text Frame", "Command")
        for i in range(10):
            result = self.read_frame()
            if not isinstance(result,str):
                return result

    (FRAME_ALL, FRAME_TEXT, FRAME_HEX) = range(3)

    # return value:
    # hex frame: string
    # text frame: object
    def read_frame(self, frame_type = FRAME_ALL):
        self.data_init()
        broadcast_cnt = 0
        while True:
            data = self.ser.read()
            for single_byte in data:
                packet = self.packet_check(single_byte)
                if (packet != None):
                    self.dump_int_array(packet, "Response")
                    if isinstance(packet, list):
                        return "".join(chr(c) for c in packet)
                    return packet

    def __init__(self, serialport, timeout, debug = False):
        self.debug = debug
        self.serialport = serialport
        self.ser = serial.Serial(serialport, 19200, timeout=timeout)
        self.header1 = ord('\r') #0x0D
        self.header2 = ord('\n') #0x0A
        self.hexmarker = ord(':') #0x3A
        self.delimiter = ord('\t') #0x09

    def data_init(self):
        self.key = ''
        self.value = ''
        self.bytes_sum = 0;
        self.state = self.WAIT_HEADER
        self.dict = {}
        self.hex_array = []

    (HEX, WAIT_HEADER, IN_KEY, IN_VALUE, IN_CHECKSUM) = range(5)

    # Process a single byte. Return packet content at the end of frame, and None
    # if in a frame.
    def packet_check(self, byte):
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


    # def read_data_callback(self, callbackFunction):
    #     i = []
    #     while True:
    #         data = self.ser.read()
    #         for byte in data:
    #             i.append(byte)
    #             packet = self.packet_check(byte)
    #             if (packet != None):
    #                 self.dump_int_array(i, "Result")
    #                 i = []
    #                 callbackFunction(packet)


    # Attch leading colon at the beginning of the command and checksum byte and
    # 0x0A to the end of raw command to create full hex command byte array.
    # e.g. gen_hex_command("7F7ED00")
    # return ":7F7ED006A" in ASCII int array
    def gen_hex_command(self, cmd):
        hex_command = [self.hexmarker]
        for c in cmd:
            hex_command.append(ord(c))

        check_result = self.hex_checksum(cmd)
        for c in "{:02X}".format(check_result):
            hex_command.append(ord(c))
        hex_command.append(self.header2)
        return hex_command

    def hex_checksum(self, cmd):
        checksum = 0
        is_high = False

        for c in cmd:
            if ord(c) == self.hexmarker:
                continue
            checksum += int(c,16)* (16 if is_high else 1)
            is_high = not is_high

        check_result = (0x155 - checksum & 0xFF) & 0xff
        return check_result


    # For internal debug use.
    def dump_int_array(self, i, comment):
        if self.debug:
            print ("=====",comment,"=====")
            if isinstance(i, list) and type(i[0] is int):
                print("".join(chr(c) for c in i))
                # print(".".join("{:02x}".format(c) for c in i))
            else:
                print(i)
