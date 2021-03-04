
# -*- coding: utf-8 -*-

class Mpptsim:
    # Send hex command to Victron SmartSolar Charge Controller
    # e.g. send_command("7F0ED00") = Get Battery maximum current
    #       return value: ":7F7ED009C09C5"
    # e.g. send_command("1") = Ping Device
    # Please refer for BlueSolar-HEX-protocol-MPPT.pdf for detailed info.
    def send_command(self, cmd):
        if cmd == "1":
            return ":55441BB"
        elif cmd == "3":
            return ":15441BF"
        elif cmd == "7EFED0072":
            return ":7EFED00185A"
        return "Not implement."

        # todo return value checksum veirfication
        # 所有返回的命令必须跟发出的命令匹配才有意义，否则就是错的

    def read_text_frame(self):
        return {'PID': '0xA057', 'FW': '154', 'SER#': 'HQ18295PH3P',
                      'V': '22680', 'I': '23400', 'VPV': '61970', 'PPV': '541',
                      'CS': '3', 'MPPT': '2', 'OR': '0x00000000', 'ERR': '0',
                      'LOAD': 'ON', 'H19': '18405', 'H20': '221', 'H21': '961',
                      'H22': '507', 'H23': '958', 'HSDS': '248'}

    (FRAME_ALL, FRAME_TEXT, FRAME_HEX) = range(3)
    #
    # # return value:
    # # hex frame: string
    # # text frame: object
    # def read_frame(self, frame_type = FRAME_ALL):
    #     self.data_init()
    #     broadcast_cnt = 0
    #     while True:
    #         data = self.ser.read()
    #         for single_byte in data:
    #             packet = self.packet_check(single_byte)
    #             if (packet != None):
    #                 self.dump_int_array(packet, "Response")
    #                 if isinstance(packet, list):
    #                     return "".join(chr(c) for c in packet)
    #                 return packet
    #
    # def __init__(self):
    #     self.debug = False
    #     self.header1 = ord('\r') #0x0D
    #     self.header2 = ord('\n') #0x0A
    #     self.hexmarker = ord(':') #0x3A
    #     self.delimiter = ord('\t') #0x09
    #
    # def data_init(self):
    #     self.key = ''
    #     self.value = ''
    #     self.bytes_sum = 0;
    #     self.state = self.WAIT_HEADER
    #     self.dict = {}
    #     self.hex_array = []
    #
    # (HEX, WAIT_HEADER, IN_KEY, IN_VALUE, IN_CHECKSUM) = range(5)
    #
    # def gen_hex_command(self, cmd):
    #     hex_command = [self.hexmarker]
    #     for c in cmd:
    #         hex_command.append(ord(c))
    #
    #     check_result = self.hex_checksum(cmd)
    #     for c in "{:02X}".format(check_result):
    #         hex_command.append(ord(c))
    #     hex_command.append(self.header2)
    #     return hex_command
    #
    # def hex_checksum(self, cmd):
    #     checksum = 0
    #     is_high = False
    #
    #     for c in cmd:
    #         if ord(c) == self.hexmarker:
    #             continue
    #         checksum += int(c,16)* (16 if is_high else 1)
    #         is_high = not is_high
    #
    #     check_result = (0x155 - checksum & 0xFF) & 0xff
    #     return check_result
    #
    #
    # # For internal debug use.
    # def dump_int_array(self, i, comment):
    #     if self.debug:
    #         print ("=====",comment,"=====")
    #         if isinstance(i, list) and type(i[0] is int):
    #             print("".join(chr(c) for c in i))
    #             # print(".".join("{:02x}".format(c) for c in i))
    #         else:
    #             print(i)
