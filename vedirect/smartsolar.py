# -*- coding: utf-8 -*-
from vedirect import Vedirect

# todo:
# 1. check if return value match command send.

class Smartsolar:
    PARAM_MAP = {
        "BatteryFloatVoltage": ':7F6ED00',
        "BatteryAbsorptionVoltage": ":7F7ED00",
        "SystemTotal":":7DDED00",
        "UserTotal":"7DCEDDC"
    }

    def __init__(self, serialport, timeout, debug = False):
        self.ve = Vedirect(serialport, timeout, debug)

    def read_text_frame(self):
        return self.ve.read_text_frame()

    def ping_device(self):
        raw_result = self.ve.send_command("1")
        return self.resp_done_decode(raw_result)

    def get_app_version(self):
        raw_result = self.ve.send_command("3")
        return self.resp_done_decode(raw_result)

    def resp_done_decode(self, raw_result):
        result = raw_result[2:6]
        version = result[3] + "." + result[0:2]
        return version

    def get_param(self, param):
        cmd_str = self.PARAM_MAP[param]
        raw_result = self.ve.send_command(cmd_str) #rtn ":7F7ED009C09C5"

        if raw_result[0:len(cmd_str)]!=cmd_str:
            print("Maybe async--------")
            raw_result = self.ve.send_command(cmd_str)
        result = raw_result[len(cmd_str)+1:len(raw_result)-2] # 9C09
        ba = bytearray.fromhex(result) #b'\x9c\t'
        ba.reverse()
        val = 0        # final result 0x099C = 2460
        for b in ba:
            val = val * 256 + b
        return (val / 100.0, "V", param)
