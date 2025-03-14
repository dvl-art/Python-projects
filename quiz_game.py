print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
        quit()

print("Okay! Let's Play")
score = 0

answer = input("What does CPU stands for? ").lower()

if answer == "central processing unit":
        print("Correct")
        score += 1
else:
        print("Incorrect")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
        print("Correct")
        score += 1
else:
        print("Incorrect")

answer = input("What does RAM stands for? ")
if answer.lower() == "Random access memory":
        print("Correct")
        score += 1
else:
        print("Incorrect")

answer = input("What does PSU stands for?")
if answer.lower() == "power supply":
        score += 1 
        print("Correct")
else:
        print("Incorrect")

print(f"You got total of {score} questions correct.")
print("You got total of" + str(score) + "questions correct.")
print("You got total of" + " " + str((score / 4 ) * 100) + "%." + "questions correct.")






