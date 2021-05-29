from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""
def putWater20():
    for i in range(20):
        put_beeper()
    move()

def putWater21():
    for i in range(21):
        put_beeper()
    move()

def main():
    putWater20()
    putWater21()
    pass

if __name__ == '__main__':
    run_karel_program('3x3.w')