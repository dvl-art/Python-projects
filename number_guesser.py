import random

random_number_user = input("Enter the number you want to guess: ")

if random_number_user.isdigit():
    random_number_user = int(random_number_user)

    if random_number_user <= 0:
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please enter a number")
    quit()

random_number = random.randint(0, random_number_user)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
            print("Your number was greater")
    else:
            print("Your number was less")
print("You got it in ", guesses, "guesses")



    

