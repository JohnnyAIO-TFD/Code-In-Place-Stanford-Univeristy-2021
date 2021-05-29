def print_ones_digit(num):
    number = num % 10
    print(number)
    pass


def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)


if __name__ == "__main__":
    main()
