from karel.stanfordkarel import *

"""
File: Archway.py
------------------------------
Karel will move up and over the archway.
"""

def archway():
    for i in range(3):
        move()
    for i in range(3):
        turn_left()

def main():
    
    turn_left()
    for i in range(3):
        archway()
    pass

if __name__ == "__main__":
    run_karel_program()