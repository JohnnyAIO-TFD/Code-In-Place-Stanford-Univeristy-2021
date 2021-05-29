from karel.stanfordkarel import *

"""
File: Obstacles.py
------------------------------
Karel will jump over the obstacles and put beepers in the pink squares.
"""
def makeAround():
    for i in range(3):
        turn_left()

def front():
    for i in range(2):
        turn_left()

def obstacles():
    for i in range(3):
        for i in range(2):
            makeAround()
            move()
        put_beeper()
        front()
        move()

def main():
    move()
    turn_left()
    move()
    obstacles()
    makeAround()
    move()
    move()
    makeAround()
    move()
    turn_left()

    pass

if __name__ == "__main__":
    run_karel_program()