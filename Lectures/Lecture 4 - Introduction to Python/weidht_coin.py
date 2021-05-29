import random


def main():
    prob = random.randint(0, 70)
    answer = input("Heads or tails: ")
    if(answer == "Heads"):
        number = 0
    elif(answer == "Tails"):
        number = 50
    else:
        print("Sorry, you put mistake word")
    if(prob >= number):
        print("Tails")
    else:
        print("Heads")
    pass


if __name__ == "__main__":
    main()
