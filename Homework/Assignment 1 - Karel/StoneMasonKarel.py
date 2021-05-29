from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""
def main():
    if front_is_clear():
        repair_main_quad()
        repair_arch()
    else:
        put_beeper()
    if no_beepers_present():
        put_beeper()

def repair_main_quad():
    while front_is_clear():
        repair_arch()
        front_blocked_put_beeper_move()

def repair_arch():
    turn_left()
    while front_is_clear():
        repair_column()

def repair_column():
    if no_beepers_present():
        put_beeper()
    else:
        move()

def move_south():
    turn_around()
    while front_is_clear():
            move()
    move_to_next_column()

def front_blocked_put_beeper_move():
    if no_beepers_present():
        put_beeper()
    move_south()

def turn_around():
    for i in range(2):
        turn_left()

def move_to_next_column():
    turn_left()
    if front_is_clear():
        for i in range(4):
            move()

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')