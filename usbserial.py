#!/usr/bin/python

from time import sleep
import serial
from bitarray import bitarray




class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
ser = serial.Serial('/dev/ttyACM0', 9600)
"""
while True:
	char = getch()  # User input, but not displayed on the screen
	print '{} type{}'.format(char, type(char))
	ser.write(char)
"""

off=(bitarray('11111111').tobytes())
on = (bitarray('00000000').tobytes())
mir = '0111111'
mohammed = '1111101'
neha = '1111110'
darold = '1110111'
kat = '1111011'
bo = '1111111'
cycle = [mir, mohammed, neha, darold, bo, kat]
cycle_bit_arr = [bitarray(person).tobytes() for person in cycle]
ser.write(off)

while True:
    ser.write(off)
    for i in cycle_bit_arr:
        ser.write(i)
        sleep(.5)
        ser.write(off)
        #sleep(.1)
    sleep(.5)
    ser.write(off)
    sleep(.5)
    ser.write(on)
    sleep(5)