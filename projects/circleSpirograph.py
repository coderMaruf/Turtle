#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 01:28:48 2021

@author: maruf
"""

import turtle as t

t.bgcolor("black")
t.pensize(2)
t.speed(0)

for i in range(7):
    for colors in ['red', 'magenta', 'blue', 'cyan', 'yellow', 'white', 'aqua']:
        t.color(colors)
        t.circle(100)
        t.left(10)
        
t.hideturtle()
