# -*- coding: utf-8 -*-
class Vecommon:
    def little_endian_to_int(s):
        ba = bytearray.fromhex(s)
        ba.reverse()
        val = 0
        for b in ba:
            val = val * 256 + b
        return val

    def int_to_little_endian(i):
        return "{:02X}{:02X}00".format(i & 0xFF, (int(i/256)) & 0xFF)
