import random

again = "y"

while again == "y":
    number = random.randint(1, 50)
    attempts = 0

    print("Guess the number between 1 and 50")

    guess = 0
    while guess != number:
        guess = int(input("Enter guess: "))
        attempts += 1

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("Correct! You took", attempts, "attempts")

    again = input("Play again? (y/n): ")
