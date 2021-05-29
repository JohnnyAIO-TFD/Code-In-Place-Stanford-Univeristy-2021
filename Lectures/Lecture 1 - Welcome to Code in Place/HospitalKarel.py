from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem
def makeround():
    for i in range(3):
        turn_left()

def hospital():
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    makeround()
    move()
    put_beeper()
    makeround()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()

def main():
    while front_is_clear():
        move()
        if beepers_present():
            hospital()
    pass

if __name__ == '__main__':
    run_karel_program('HospitalKarel.w')