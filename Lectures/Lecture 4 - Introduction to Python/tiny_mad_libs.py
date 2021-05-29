# adjective noun verb
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my "


def main():
    adjd = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")
    results = SENTENCE_START + adjd + " " + noun + " " + verb + "!"
    print(results)
    pass


if __name__ == "__main__":
    main()
