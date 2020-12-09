# ghiceste numarul

import random

true_number = random.randint(1,15)

guess_number = int(input("Enter your guess between 1 and 15:"))
#print(true_number)

while True:
    if guess_number == true_number:
        print("Ai ghicit numarul!!!!")
        break

    elif guess_number < true_number:
            print("Numarul incercat e mai mic decat cel generat")
            guess_number = int(input("Enter your guess between 1 and 15:"))

    elif guess_number > true_number:
            print("Numarul incercat e mai mare decat cel generat")
            guess_number = int(input("Enter your guess between 1 and 15:"))
