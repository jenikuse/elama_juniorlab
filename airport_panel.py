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
    # your code here

    sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
    s, rtrs = list(lines[0]), rotors[0]

    for i in range(len(rtrs)):
        current = sample.find(s[i])
        s[i] = sample[current + rtrs[i]]
        print s

        for j in range(len(s)):
            if j > i:
                current = sample.find(s[i])
                #s[j] = sample[current + rtrs[i]]
  


    return s

flap_display(["CAT"], [[1, 13, 27]]) #["DOG"]
#flap_display(["HELLO "], [[15,49,50,48,43,13]]) #["WORLD!"]
#flap_display(["CODE"], [[20,20,28,0]]) #["WARS"]
#flap_display(["NOTHING MOVED"], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) #["NOTHING MOVED"]
#flap_display(["EFGH"], [[53, 53, 53, 53]]) #["DDDD"]
#["CAN HEAR YOU SCREAM!"]
#flap_display(["IN SPACE NOBODY...  "], [[48, 47, 0, 21, 38, 120, 48, 15, 41, 11, 43, 19, 47, 3, 17, 2, 41, 50, 23, 16]])