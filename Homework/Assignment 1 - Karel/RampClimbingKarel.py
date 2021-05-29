from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""
def moveTwo():
    move()
    move()

def makeround():
    for i in range(3):
        turn_left()

def Climbing():
    if no_beepers_present():
        put_beeper()
    moveTwo()
    turn_left()
    move()
    put_beeper()
    makeround()

def ClimbingOpposite():
    move()
    turn_left()
    moveTwo()
    put_beeper()
    makeround()

def main():
    while front_is_clear():
        Climbing()
    turn_left()
    while front_is_clear():
        ClimbingOpposite()
    pass

if __name__ == '__main__':
    run_karel_program('RampKarel3.w')