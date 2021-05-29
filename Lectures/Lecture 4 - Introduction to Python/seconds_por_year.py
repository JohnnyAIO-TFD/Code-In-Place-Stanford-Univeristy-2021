minutes = 60  # seconds
hour = 60  # minutes
day = 24  # hours
year = 365  # days


def main():
    number = int(input("Introduce the seconds: "))
    print("The minutes are:", number/minutes)
    print("The hours are:", number/(minutes*hour))
    print("The Day are:", number/(minutes*hour*day))
    print("The year are:", number/(minutes*hour*day*year))
    pass


if __name__ == "__main__":
    main()
