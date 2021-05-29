"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random
A = random.randint(0, 100)
B = random.randint(0, 100)


def main():
    print("What is " + str(A) + " + " + str(B) + "?")
    answ = int(input("Your answer: "))
    suma = A + B
    if suma == answ:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is", suma)
    pass


if __name__ == '__main__':
    main()
