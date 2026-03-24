import random

num = random.randint(1, 100)

tries = 7

while tries > 0:

    guess = int(input("Guess: "))

    if guess == num:
        print("Correct")
        break

    elif guess > num:
        print("Too high")

    else:
        print("Too low")

    tries -= 1

if tries == 0:
    print("Game Over", num)