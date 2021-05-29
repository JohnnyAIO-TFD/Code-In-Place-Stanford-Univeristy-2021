SAMPLE_LIST = ['a', 'b', 'c', 'd', 'e']
MAX_LENGTH = 3


def shorten(lst, max_len):
    while len(lst) > max_len:
        last = lst.pop()
        print(last)
    pass


def main():
    shorten(SAMPLE_LIST, MAX_LENGTH)


if __name__ == "__main__":
    main()
