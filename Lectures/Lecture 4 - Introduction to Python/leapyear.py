def main():
    year = int(input("Give your year: "))
    if(not year % 4):
        if(not year % 100):
            if(not year % 400):
                print("That's leap year!")
            else:
                print("That's not a leap year")
        else:
            print("That's leap year!")
    else:
        print("That's not a leap year")
    pass


if __name__ == "__main__":
    main()
