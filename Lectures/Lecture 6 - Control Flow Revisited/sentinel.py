"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""


def main():
    number = 0
    suma = 0
    while number != -1:
        number = int(input("Type a number: "))
        if(number != -1):
            suma += number
    print("total is: ", suma)
    pass


if __name__ == '__main__':
    main()
