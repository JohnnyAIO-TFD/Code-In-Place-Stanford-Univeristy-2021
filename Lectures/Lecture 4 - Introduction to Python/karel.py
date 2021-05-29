N_COLS = 3  # notice these constants!
N_ROWS = 3


def main():
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    # this variable will keep track of the way Karel is facing -- it changes if the user says to "turn left"!
    facing_direction = "East"
    curr_col = 1  # this variable ...
    curr_row = 1  # ... and this one keep track of Karel's position in the world! they may change if the user says to "move"
    while (curr_col != N_COLS or curr_row != N_ROWS):
        action = input(
            "What would you like to do? You can move and turn left. Press enter to finish. ")
        if(action == "move" and facing_direction == "East"):
            if(curr_col == N_COLS):
                print("You can't move forward!")
            else:
                curr_col += 1
                print("You moved one step forward and now you're at row " +
                      str(curr_row) + " column " + str(curr_col))
        if(action == "move" and facing_direction == "West"):
            if(curr_col == 1):
                print("You can't move forward!")
            else:
                curr_col = curr_col - 1
                print("You moved one step forward and now you're at row " +
                      str(curr_row) + " column " + str(curr_col))
        # END - COLUMNS
        if(action == "move" and facing_direction == "North"):
            if(curr_row == N_ROWS):
                print("You can't move forward!")
            else:
                curr_row += 1
                print("You moved one step forward and now you're at row " +
                      str(curr_row) + " column " + str(curr_col))
        if(action == "move" and facing_direction == "South"):
            if(curr_row == 1):
                print("You can't move forward!")
            else:
                curr_row = curr_row - 1
                print("You moved one step forward and now you're at row " +
                      str(curr_row) + " column " + str(curr_col))
        if(action == "turn left"):
            if(facing_direction == "East"):
                facing_direction = "North"
            elif(facing_direction == "North"):
                facing_direction = "West"
            elif(facing_direction == "West"):
                facing_direction = "South"
            else:
                facing_direction = "East"
            print("You turned left and are now facing " +
                  str(facing_direction) + "!")

    # ... more code! there's a while loop that starts on this line, but our hint ends here :^)
    pass


if __name__ == "__main__":
    main()
