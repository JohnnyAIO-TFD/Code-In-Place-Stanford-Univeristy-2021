"""
Prints the Fizz Buzz sequence up to a given number.
"""

# define constants for the fizz and buzz numbers
FIZZ_NUM = 3
BUZZ_NUM = 5


def main():
    limit_str = input("Number to count to: ")
    limit = int(limit_str)

    # set up our counter variables outside the loop
    num_fizzed = 0
    num_buzzed = 0
    num_fizzbuzzed = 0

    # loop from 1 until limit (not including limit + 1)
    for i in range(1, limit + 1):
        if i % FIZZ_NUM == 0 and i % BUZZ_NUM == 0:
            # i is a multiple of FIZZ_NUM and BUZZ_NUM
            num_fizzbuzzed += 1
            print("Fizzbuzz")
        elif i % FIZZ_NUM == 0:
            # i is a multiple of FIZZ_NUM, but not BUZZ_NUM
            num_fizzed += 1
            print("Fizz")
        elif i % BUZZ_NUM == 0:
            # i is a multiple of BUZZ_NUM, but not FIZZ_NUM
            num_buzzed += 1
            print("Buzz")
        else:
            # i is not a multiple of FIZZ_NUM Or BUZZ_NUM
            print(i)

    print("")  # print a blank line
    print("Num fizzed: " + str(num_fizzed))
    print("Num buzzed: " + str(num_buzzed))
    print("Num fizzbuzzed: " + str(num_fizzbuzzed))


if __name__ == '__main__':
    main()
