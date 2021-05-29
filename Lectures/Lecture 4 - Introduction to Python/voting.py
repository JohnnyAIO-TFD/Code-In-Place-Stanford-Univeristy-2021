def main():
    age = int(input("How old are you? "))
    if(age >= 16):
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")
    if(age >= 25):
        print("You can vote in Stanlau where the voting age is 20.")
    else:
        print("You cannot vote in Stanlau where the voting age is 20.")
    if(age >= 48):
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")
    pass


if __name__ == "__main__":
    main()
