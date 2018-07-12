#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In middle-earth is approaching war. There are many battles of the forces of light with darkness.
As the one and the other race decide to unite in order to defeat the enemy.
Each race has its own forces, which are estimated points.

On the side of good will fight:         On the dark side fighting:
The hobbit: 1                           Orcs: 1
People: 2                               People: 2
Elves: 3                                Varga: 2
Dwarves: 3                              Goblins: 2
Eagles: 4                               Uruk-Hai: 3
Wizards: 10                             Trolls: 5
                                        Wizards: 10

Your task is to determine who will win the battle.
The function takes two arguments, which are strings. Each line contains a space separated number
of creatures that will fight for the race (the order is the same as in the above lists).

The function should return "Battle Result: Good triumphs over Evil" if good wins,
"Battle Result: Evil eradicates all trace of Good" if evil wins and
"Battle Result: No victor on this battle field" if it is a draw.
"""
def goodvsevil(good, evil):

    def sumString(str):
        sum, idx = 0, 0
        for i in range(len(str)):
            if str[i] == ' ':
                sum += int(str[idx:i])
                idx = i + 1
            elif i == len(str) - 1:
                sum += int(str[idx:i + 1])
        return sum

    sum_good, sum_evil = sumString(good), sumString(evil)

    if sum_good > sum_evil:
        return "Battle Result: Good triumphs over Evil"
    elif sum_good < sum_evil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victory on this battle field"