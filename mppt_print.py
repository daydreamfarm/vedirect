#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os
from vedirect import Smartsolar

def print_data_callback(packet):
    print(packet)
#    print(":".join("{:02x}".format(ord(c)) for c in packet))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process VE.Direct protocol')
    parser.add_argument('--port', help='Serial port')
    parser.add_argument('--timeout', help='Serial port read timeout', type=int, default='60')
    args = parser.parse_args()

    ss = Smartsolar('/dev/tty.usbserial-VE4ZKFJZ', 60, debug=False,sim=True)
    t =(ss.read_text_frame())
    print(t)
    # print(ss.ping_device())
    # print("app version", ss.get_app_version())

    # print("SystemTotal", ss.get_param("UserTotal"))
