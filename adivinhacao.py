import random


def guesser():
    print("Welcome to the number guesser!")

    number = random.randrange(1, 101)
    guesses = 0
    guess = 0

    while guess != number:
        guess = int(input("Type a number between 1 and 100: "))

        if guess not in range(1, 101):
            print("Invalid!")
            continue

        elif guess < number:
            print("Higher! ")

        elif guess > number:
            print("Lower! ")

        guesses += 1

    print(f"Congratulations, you found the number!!! It took you {guesses} guesses")


if __name__ == "__main__":
    guesser()