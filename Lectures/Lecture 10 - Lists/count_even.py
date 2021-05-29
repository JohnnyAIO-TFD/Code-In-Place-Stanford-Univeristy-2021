SAMPLE_LIST = [1, 2, 3, 4, 5, 6]


def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0
    for i in lst:
        if(i % 2 == 0):
            count += 1
    print(count)
    pass


def main():
    count_even(SAMPLE_LIST)


if __name__ == "__main__":
    main()
