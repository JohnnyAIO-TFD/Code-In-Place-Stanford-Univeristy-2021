
def main():
    x = 1
    plus_five(x)
    print(x)


def plus_five(y):
    global x
    x = y + 5


if __name__ == '__main__':
    main()
