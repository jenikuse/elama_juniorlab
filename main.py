#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from good_vs_evil import *
from ip_validation import *
from squares_in_rectangle import *
from airport_panel import *

def good_evil():
    armies = (["707 423 584 293 572 62", "136 864 0 626 15 152 121"],
              ["132 196 432 622 929 373", "761 683 48 801 805 463 176"],
              ["830 55 258 226 261 227", "831 876 577 745 781 6 438"],
              ["869 260 246 189 401 378", "41 826 818 746 393 705 95"],
              ["0 1 0 0 0 0", "0 0 0 1 0 0 0"],
              ["0 0 0 1 0 0", "0 0 0 0 1 0 0"])
    for army in armies:
        print '\nGood army: %s\tEvil army: %s ' % (army[0], army[1])
        print goodvsevil(army[0], army[1])

def check_ip():
    ips = ("123.456.789.0", "abc.def.ghi.jkl", "12.34.56", "123,45,67,89",
           "53.58.97.93", "28.84.197.169", "255.255.255.255", " 1.2.3.4")
    for ip in ips:
        print '\nIs this IP-address "%s" valid?' % ip
        print isvalidip(ip)

def find_squares():
    rectangles = ([5, 5],
                  [5, 3],
                  [3, 5],
                  [20, 14],
                  [240, 32],
                  [135, 85],
                  [6, 6])
    for rect in rectangles:
        print '\nThe length of the rectangle: %i\tThe width of the rectangle: ' % rect[0], rect[1]
        print 'Sizes of squares: ', sq_in_rect(rect[0], rect[1])

def flap_dspl():
    strings = ([["CAT"], [[1, 13, 27]]],  \
               [["HELLO "], [[15, 49, 50, 48, 43, 13]]],  \
               [["CODE"], [[20, 20, 28, 0]]],  \
               [["NOTHING MOVED"], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]], \
               [["EFGH"], [[53, 53, 53, 53]]])
    for str in strings:
        print '\nString for change: %s\nRotors value to change: %s' % (str[0], str[1])
        print 'New string on the display: ', flap_display(str[0], str[1])


while True:
    choice = int(raw_input('\n\nEnter a number to see:\n'
                           '1 – Who will win? Good army or evils?\n'
                           '2 – Check if the IP-address is correct.\n'
                           '3 – How many squares will fit in a rectangle?\n'
                           '4 – See how work rotors on the airport display\n'
                           '\n0 – Exit\n'))

    if choice == 1:
        good_evil()
    elif choice == 2:
        check_ip()
    elif choice == 3:
        find_squares()
    elif choice == 4:
        flap_dspl()
    elif choice == 0:
        print 'Program was ended\n'
        break
    time.sleep(1)