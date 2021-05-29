from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def move2():
    for i in range(2):
        move()

def front():
    for i in range(2):
        turn_left()

def makeAround():
    for i in range(3):
        turn_left()

def move3():
    for i in range(3):
        move()

def main():
    move2()
    pick_beeper()
    move()
    turn_left()
    move2()
    put_beeper()
    front()
    move2()
    makeAround()
    move3()
    front()
    pass

if __name__ == '__main__':
    run_karel_program('Puzzle.w')