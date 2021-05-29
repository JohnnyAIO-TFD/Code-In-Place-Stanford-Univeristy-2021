SAMPLE_ROSTER = ['miranda', 'karel', 'shrek', 'donkey']


def find_karel(roster):
    """
    Prints whether or not Karel is in the roster.
    >>> find_karel(['chris', 'mehran'])
    Karel isn't here.
    >>> find_karel(['karel', 'is', 'here'])
    Karel is here!
    """
    if 'karel' in roster:
        print("Karel is here!")
    else:
        print("Karel is not here!")
    pass


def main():
    # delete the pass statement below and write your code here!
    find_karel(SAMPLE_ROSTER)


if __name__ == "__main__":
    main()
