def main():
    div = int(input('Please enter an integer to be divided: '))
    sustr = int(input('Please enter an integer to divide by: '))
    results = div//sustr
    remainder = div % sustr
    print('The result of this division is',
          results, 'with a remainder of', remainder)
    pass


if __name__ == "__main__":
    main()
