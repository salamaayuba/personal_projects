import random

count = 3
while count != 0:
    guess = int(input("Enter a random number: "))
    num = random.randint(1, 20)
    if guess == num:
        print("Congratulations! You won")
        count = 3
    else:
        count -= 1

        while count != 0:
            print("You have {} lives left!".format(count))
            #guess = int(input("Guess again: "))

            if guess < num:
                guess = int(input("Guess a higher number: "))
                count -= 1

            elif guess > num:
                guess = int(input("Guess a lower number: "))
                count -= 1

            elif guess == num:
                print("Congratulations! You got it😀.")
                count = 3
                break

            if count == 0:
                print("You have exhausted your trials. Better luck next time😭.")

print("End of game")