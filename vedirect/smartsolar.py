# -*- coding: utf-8 -*-
from vedirect import Vedirect
class Smartsolar:
    PARAM_MAP = {
        "BatteryFloatVoltage": ':7F6ED00',
        "BatteryAbsorptionVoltage": ":7F7ED00",
    }

    def __init__(self, serialport, timeout):
        self.ve = Vedirect(serialport, timeout)

    def pingDevice(self):
        raw_result = self.ve.send_command(":1") #rtn ":7F7ED009C09C5"
        result = raw_result[2:6]
        version = result[3] + "." + result[0:2]
        return version

    def getParam(self, param):
        raw_result = self.ve.send_command(self.PARAM_MAP[param]) #rtn ":7F7ED009C09C5"
        result = raw_result[8:12] # 9C09
        ba = bytearray.fromhex(result) #b'\x9c\t'
        ba.reverse()
        val = 0        # final result 0x099C = 2460
        for b in ba:
            val = val * 256 + b
        return (val / 100.0, "V", param)
