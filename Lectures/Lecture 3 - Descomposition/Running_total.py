SENTINEL = 0


def main():
    # get one number before the loop. We need this number
    # so that we have an initial value for the running total,
    # and a condition for the while loop
    user_number_str = input("Enter a value: ")
    user_number = int(user_number_str)
    total_so_far = user_number

    # keep on asking for a number and updating the running total
    # until the user enters 0
    while user_number != SENTINEL:
        print("Running total is " + str(total_so_far))
        user_number_str = input("Enter a value: ")
        user_number = int(user_number_str)
        total_so_far = total_so_far + user_number


if __name__ == '__main__':
    main()
