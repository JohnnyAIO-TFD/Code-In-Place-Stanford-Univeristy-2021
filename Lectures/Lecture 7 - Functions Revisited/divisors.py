def print_divisors(num):
    div = 1
    print("Here are the divisors of ", num)
    while(div <= num):
        if(num % div == 0):
            print(div)
        div += 1
    pass


def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


if __name__ == "__main__":
    main()
