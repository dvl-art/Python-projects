print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
        quit()

print("Okay! Let's Play")


answer = input("What does CPU stands for? ").lower()

if answer == "central processing unit":
        print("Correct")
else:
        print("Incorrect")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
        print("Correct")
else:
        print("Incorrect")

answer = input("What does RAM stands for? ")
if answer.lower() == "Random access memory":
        print("Correct")
else:
        print("Incorrect")

answer = input("What does PSU stands for?")
if answer.lower() == "power supply":
        print("Correct")
else:
        print("Incorrect")






