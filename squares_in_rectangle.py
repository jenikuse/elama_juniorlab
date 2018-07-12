#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
cut rectangle into squares
You are given two values:

The length of the rectangle (parameter lng)
The width of the rectangle (the width parameter)
You must return an array of numbers with the size of the side of each square.

If the arguments passed are equal, return None.
"""
def sq_in_rect(lng, wdth):

    if lng == wdth:
        return None
    elif lng < wdth:
        big, small = wdth, lng
    else:
        big, small = lng, wdth

    bs = [big, small]
    res = []

    while big > small:
        n = big / small
        numb = big - small

        for i in range(n):
            res.append(small)

        big, small = small, numb

    if n < len(res):
        if res[-1] * n != res[-n-1]:
            tmp = res[-n-1] % res[-1]
            for i in range(res[-1]/tmp):
                res.append(tmp)

    # strange case when we have many squares with the same size, but it works
    else:
        add_num = bs[0] - (res[-1] * n)
        for i in range(res[-1] / (bs[0] - (res[-1] * n))):
            res.append(add_num)

    return res