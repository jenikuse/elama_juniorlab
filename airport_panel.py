#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imagine that you are at the airport and stuck on the Board of arrival / departure.
You notice that each symbol is controlled by the rotor,
and the order of the symbols on each rotor is the following:

ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.: =-+*/0123456789

After thinking a little, you realize that the display works according to the following rules:

1) Starting from the left edge (from the current symbol to the end of the line)
all values change until the left rotor symbol is correct.
2) The mechanism then moves one rotor to the right.
3) Repeats step one. And so until the whole line is updated.
4) The whole procedure is repeated from top to bottom until all the scoreboard is updated.

the flapDisplay function takes two arguments: an array of words and an array of offsets.
"""
def flap_display(lines, rotors):

    sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
    s, rtrs = list(lines[0]), rotors[0]
    res = ['']
    for i in range(len(s)):
        for j in range(i, len(rtrs)):

            current = sample.find(s[j])
            idx_rotor = current + rtrs[i]
            if idx_rotor >= len(sample):
                idx_rotor -= len(sample)

            s[j] = sample[idx_rotor]

    for i in range(len(s)):
        res[0] += s[i]

    return res