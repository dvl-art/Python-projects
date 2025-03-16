print("Let's play the quize game")
user_reply = str(input("Do you want to play the game? Shall we continue?"))
if user_reply.lower() == "yes":
	print("So let's start the game")
	total_score = 0
	answer = input("What is stand for CPU? ")
	if answer.lower() == "central processing unit":
		print("You are right")
		total_score += 1
	else:
		print("You are wrong")

	answer = input("What is stand for GPU? ")
	if answer.lower() == "graphics processing unit":
		print("You are right")
		total_score += 1
	else:
		print("You are wrong")

	answer = input("What is stand for POS? ").lower()
	if answer == "power supply":
		print("You are right")
		total_score += 1
	else:
		print("You are wrong")

	print("Your have given total right answers " + str(total_score) + " out of 3")
else:
	print("No problem, play next time")
	quit()




