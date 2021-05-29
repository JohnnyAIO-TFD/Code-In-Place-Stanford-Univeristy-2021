"""
TODO: Write a description here
"""

import random


def main():
    corrects = 0
    while corrects < 3:
        A = random.randint(0, 100)
        B = random.randint(0, 100)
        print("What is " + str(A) + " + " + str(B) + "?")
        answ = int(input("Your answer: "))
        suma = A + B

        if suma == answ:
            corrects += 1
            if(corrects == 3):
                print("Correct! You've gotten " +
                      str(corrects) + " correct in a row")
                print("Congratulations! You mastered addition.")
            else:
                print("Correct! You've gotten " +
                      str(corrects) + " correct in a row")
        else:
            print("Incorrect. The expected answer is", suma)
            corrects = 0

    pass


if __name__ == '__main__':
    main()
