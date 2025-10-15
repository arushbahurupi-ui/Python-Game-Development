import random

secret = random.randint(1,10)

guess_count = 1
guess_limit = 4

while guess_count <= guess_limit:
    guess = input("Enter your guess: ")
    guess_count += 1
    if guess == secret:
        print("You have won!")
        break
else:
    print("Sorry you have failed!")

