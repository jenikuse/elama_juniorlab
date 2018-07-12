#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Write an algorithm that will check whether IPv4 addresses are valid.
IP addresses are valid if they consist of 4 octets with values between 0..255 (inclusive)

The input argument is a string with an IP address.
'''
def isvalidip(str):
    res, idx, flag = [], 0, True

    if str[0] not in '0123456789':
        return False

    for i in range(len(str)):
        if str[i] == ',':
            return False

        if str[i] == '.':
            res.append(int(str[idx:i]))  # current octet
            idx = i + 1  # start new octet

            if res[-1] < 0 or res[-1] > 255:
                return False
    res.append(int(str[idx:len(str)]))

    if len(res) != 4:
        flag = False
    return flag