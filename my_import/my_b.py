# -*- coding: utf-8 -*-
import struct

if __name__ == '__main__':
    num = 0x1234567
    var = struct.pack('i', num)
    print(var)

    print(hex(var[0]))

