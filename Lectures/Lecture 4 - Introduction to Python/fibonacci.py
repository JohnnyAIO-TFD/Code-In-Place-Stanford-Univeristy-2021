NUMBER = 10000


def main():
    n1, n2 = 0, 1
    while n1 <= NUMBER:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
    pass


if __name__ == "__main__":
    main()
