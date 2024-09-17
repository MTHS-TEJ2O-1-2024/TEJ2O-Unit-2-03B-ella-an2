"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
from time import sleep


display.clear()
sleep(1)

display.scroll("Area equals: 5 x 3 =" + str(5 * 3) + "cm ^ 2")
sleep(0.5)
display.clear

display.scroll("Perimeter equals: 5 + 5 + 3 + 3 =" + str(5 + 5 + 3 + 3) + "cm")
sleep(0.5)
display.clear
