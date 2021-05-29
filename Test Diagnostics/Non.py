def main():
    number_prev = -10000
    number_next = 1
    count = 0
    number_next = float(input("Enter num: "))
    while number_next >= number_prev:
        # number_next = float(input("Enter num: "))
        number_prev = number_next
        count = count + 1
        number_next = float(input("Enter num: "))
    print("Thanks for playing!")
    print("Sequence length:", count)


main()