"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""


def main():
    number = int(input('Enter a weight on Earth: '))
    weight = number*37.8/100
    print('The equivalent on Mars:', weight)
    pass


if __name__ == "__main__":
    main()
