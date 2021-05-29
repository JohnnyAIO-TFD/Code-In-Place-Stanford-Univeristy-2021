MAXIMUM = 50


def main():
    tall = 1000
    while tall > MAXIMUM:
        tall = int(input("How tall are you? "))
        if(tall > MAXIMUM):
            print("You're tall enough to ride!")
        else:
            print("Go ahead")
    pass


if __name__ == "__main__":
    main()
