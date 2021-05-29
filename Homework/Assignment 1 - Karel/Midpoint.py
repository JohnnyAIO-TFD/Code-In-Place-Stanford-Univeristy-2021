from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper in the middle of the first row.
"""

def main():
    count_and_find_middle()

def count_and_find_middle():
    count_corners()
    turn_around()
    if front_is_clear():
        find_middle()

def count_corners():
    put_beeper()
    while front_is_clear():
        next_corner()
        #Replace beepers to next corner
        replace_beepers() 
        put_beeper()

def find_middle():
    while beepers_present():
        sub_2_beepers()
        move()
        replace_beepers()
    one_step_back()
    put_beeper()

def sub_2_beepers():
    if beepers_present():
        pick_beeper()
        if beepers_present():
            pick_beeper()

def next_corner():
    if front_is_clear():
        move()

def replace_beepers():
#One corner back. Face the same direction.
    one_step_back() 
    while beepers_present():
        pick_beeper()
        move()
        put_beeper()
        one_step_back()
    move()

def one_step_back():
    turn_around()
    move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program('Midpoint.w')