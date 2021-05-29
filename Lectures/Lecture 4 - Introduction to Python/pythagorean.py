import math


def main():
    AB = float(input("Enter the length of AB: "))
    AC = float(input("Enter the length of AC: "))
    total = math.sqrt((AB**2) + (AC**2))
    print("The length of BC (the hypotenuse) is:", total)
    pass


if __name__ == "__main__":
    main()
