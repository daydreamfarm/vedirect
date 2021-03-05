
# -*- coding: utf-8 -*-
from vedirect import Vecommon
from vedirect import Veconst

class Mpptsim:
    def send_command(self, cmd):
        self.dump_int_array(cmd, "COMMAND")
        if cmd[1]=='1':
            return (True,":55441BB")
        elif cmd[1]=="3":
            return (True,":15441BF")
        if cmd[1]=='7':
            i = Vecommon.little_endian_to_int(cmd[2:6])
            if not i in Veconst.REG_PARAMS.keys():
                return (False, "Param Not Exists!")
            reg = Veconst.REG_PARAMS[i]
            if reg[5][7:8]=='1':
                return (False, "Unknown ID")
            return (True, reg[5])
        else:
            return (False, "Unknown command" + cmd)

    def read_text_frame(self):
        return {'PID': '0xA057', 'FW': '154', 'SER#': 'HQ18295PH3P',
                      'V': '22680', 'I': '23400', 'VPV': '61970', 'PPV': '541',
                      'CS': '3', 'MPPT': '2', 'OR': '0x00000000', 'ERR': '0',
                      'LOAD': 'ON', 'H19': '18405', 'H20': '221', 'H21': '961',
                      'H22': '507', 'H23': '958', 'HSDS': '248'}

    def __init__(self, debug = False):
        self.debug = debug
        self.header1 = ord('\r') #0x0D
        self.header2 = ord('\n') #0x0A
        self.hexmarker = ord(':') #0x3A
        self.delimiter = ord('\t') #0x09

    def dump_int_array(self, i, comment):
        if self.debug:
            print ("=====",comment,"=====")
            if isinstance(i, list) and type(i[0] is int):
                print("".join(chr(c) for c in i))
                # print(".".join("{:02x}".format(c) for c in i))
            else:
                print(i)
