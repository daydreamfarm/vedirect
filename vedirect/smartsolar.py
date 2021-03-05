# -*- coding: utf-8 -*-
from vedirect import Vecommon
from vedirect import Veconst
from vedirect import Vedirect
from vedirect import Mpptsim


# todo:
# 1. check if return value match command send.

class Smartsolar:
    def __init__(self, serialport, timeout, debug = False, sim = False):
        self.sim = sim
        self.debug = debug
        if sim:
            self.ve = Mpptsim(debug)
        else:
            self.ve = Vedirect(serialport, timeout, debug)

    def read_text_frame(self):
        return self.text_translate(self.ve.read_text_frame())

    def ping_device(self):
        flag,raw_result = self.ve.send_command("1")
        return self.resp_done_decode(raw_result)

    def get_app_version(self):
        flag,raw_result = self.ve.send_command("3")
        return self.resp_done_decode(raw_result)

    # Decode ping/get app command response.
    def resp_done_decode(self, raw_result):
        result = raw_result[2:6]
        version = result[3] + "." + result[0:2]
        return version

    def get_param(self, param):
        if not param in Veconst.REG_PARAMS.keys():
            return ("Param not found!")
        cmd_str = ":7" + Vecommon.int_to_little_endian(param)

        flag,raw_result = self.ve.send_command(cmd_str) #rtn ":7F7ED009C09C5"

        if not flag:
            return (flag, raw_result)

        result = raw_result[len(cmd_str):len(raw_result)-2] # 9C09
        reg_param = Veconst.REG_PARAMS[param]
        if reg_param[Veconst.IDX_DATA_TYPE] == Veconst.TYPE_STRING: # string
            val = bytearray.fromhex(result).decode("utf-8").strip("\x00")
        else:
            val = Vecommon.little_endian_to_int(result)

        reg_param = Veconst.REG_PARAMS[param]
        if reg_param[Veconst.IDX_SCALE] > 0:
            val = val * reg_param[Veconst.IDX_SCALE]
        return (True,(val, reg_param[Veconst.IDX_UNIT], reg_param[Veconst.IDX_DESC]))

    def human_dump(self, d):
        for i in d:
            print(i[0],":",i[1],i[2])

    def text_translate(self, dict):
        tar_dict = []
        for k in dict:
            if k in Veconst.VEDIRECT_MAPPING.keys():
                v = dict[k]
                if Veconst.VEDIRECT_MAPPING[k]["process"] > 0:
                    v = "{:.02f}".format(float(v)*Veconst.VEDIRECT_MAPPING[k]["process"])
                elif Veconst.VEDIRECT_MAPPING[k]["process"] == -10:
                    v = Veconst.PID_MAPPING[v]
                elif Veconst.VEDIRECT_MAPPING[k]["process"] == -11:
                    v = Veconst.CS_MAPPING[v]
                elif Veconst.VEDIRECT_MAPPING[k]["process"] == -12:
                    v = Veconst.MPPT_MAPPING[v]
                attr = [Veconst.VEDIRECT_MAPPING[k]["name"], v, Veconst.VEDIRECT_MAPPING[k]["unit"],dict[k]]
            else:
                attr = [k,dict[k],"",dict[k], dict[k]]
            tar_dict.append(attr)
        if self.debug:
            self.human_dump(tar_dict)
        return tar_dict
