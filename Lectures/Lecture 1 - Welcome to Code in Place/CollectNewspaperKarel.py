from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def makeAround():
    for i in range(3):
        turn_left()

def main():
    for i in range(2):
        move()
    makeAround()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_left()
    turn_left()
    move()
    makeAround()
    move()
    turn_left()
    for i in range(2):
        move()
    turn_left()
    turn_left()
    pass

if __name__ == "__main__":
    run_karel_program()