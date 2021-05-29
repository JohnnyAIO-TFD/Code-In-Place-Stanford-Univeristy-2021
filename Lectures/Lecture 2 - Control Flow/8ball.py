"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""


def main():
    faq = input('What is your questions? ')
    if faq == 'My name is Jonathan?':
        results = 'As I see it, yes.'
    if faq == 'Would I like to get a job in a FANG?':
        results = 'Asl again later.'
    if faq == 'Venezuela would be better?':
        results = 'Cannot predict now.'
    if faq == 'May I be better programmer?':
        results = 'It is centain.'
    if faq == 'My life will be more easyer?':
        results = 'You may rely on it.'

    print(results)
    pass


if __name__ == "__main__":
    main()
