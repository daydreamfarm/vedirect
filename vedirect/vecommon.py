# -*- coding: utf-8 -*-
class Vecommon:
    def little_endian_to_int(s):
        ba = bytearray.fromhex(s)
        ba.reverse()
        val = 0
        for b in ba:
            val = val * 256 + b
        return val
