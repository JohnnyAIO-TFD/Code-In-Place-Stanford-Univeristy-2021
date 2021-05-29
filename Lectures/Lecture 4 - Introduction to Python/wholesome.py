def main():
    answer = " "
    while answer != "I am capable of doing anything I put my mind to.":
        print("Please type the following affirmation: I am capable of doing anything I put my mind to.")
        answer = input("")
        if(answer == "I am capable of doing anything I put my mind to."):
            print("That's right! :)")
        else:
            print("That was not the affirmation.")
    pass


if __name__ == "__main__":
    main()
