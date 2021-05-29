"""
TODO: Write a description here
"""

import random


def parImpar(n):
    return n % 2 == 0


def main():
    count = 0
    n = int(input("Enter a number: "))
    while n > 1:
        if(parImpar(n)):
            # Even
            aux = n
            n = n//2
            print(str(aux) + " is even, so I take half: " + str(n))
        else:
            # Odd
            aux = n
            n = 3*n + 1
            print(str(aux) + " is odd, so I make 3n + 1: " + str(n))
        count += 1
    print("The process took " + str(count) + " steps to reach 1")
    pass


if __name__ == "__main__":
    main()
