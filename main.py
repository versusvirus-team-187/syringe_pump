#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from sp_display import read_float


diameter = read_float("Enter the syringe-diameter.", 5, 1)
flow_rate = read_float("Enter the flow-rate [ml/h].", 1, 0.1)
time = read_float("Enter the run-time in h.", 5, 1)




#
# Displays the message. Prompts the user to enter a float number.
#
def read_float(message, retVal, increment):
    while Button.down:
        pass
    while Button.enter:
        _print_float(message, retVal)
        if Button.left:
            increment *= 10
            while Button.left:
                pass
        if Button.right:
            increment *= 10
            while Button.right:
                pass
        if Button.up:
            retVal += increment
            while Button.up:
                pass
        if Button.down:
            retVal -= increment
            while Button.down:
                pass
    return retVal

def _print_float(message, value):
    brick.display.clear()
    brick.display.text(message)
    brick.display.text(str(value))
