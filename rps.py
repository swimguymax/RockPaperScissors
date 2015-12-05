from random import randint

player_score = 0

cpu_score = 0

result = "null"

results = {
	#wins
	1:"rock beats scissors",
	2:"paper beats rock",
	3:"scissors beat paper",
	#losses
	4:"paper beats rock",
	5:"scissors beat paper",
	6:"rock beats scissors",
	#ties
	7:"you both chose rock",
	8:"you both chose paper",
	9:"you both chose scissors"
}

results2 = {"player":0, "cpu":3, "tie":6}

choices = {
	1:"rock",
	2:"paper",
	3:"scissors"
}

def play_hand(cpu, player):
	if cpu == player:
		result = "tie"

	elif (cpu == 2 and player == 1) or (cpu == 3 and player == 2) or (cpu == 1 and player == 3):
		result = "cpu"

	elif (player == 2 and cpu == 1) or (player == 3 and cpu == 2) or (player == 1 and cpu == 3):
		result = "player"

	return result

def play_game():
	global player_score, cpu_score
	
	while True:
		player_string = str(raw_input("Enter rock, paper or scissors; or enter quit to leave the game. \nPLAYER> ")).lower()

		cpu_number = randint(1, 3)

		if player_string == "quit" or player_string=="exit":
			print("Quitting...")
			break

		elif player_string == "rock":
			player_number = 1

		elif player_string == "paper":
			player_number = 2

		elif player_string == "scissors":
			player_number = 3
		
		else:
			print("Please choose a valid option\n")
			continue

		print("CPU---> "+choices[cpu_number])
		result = play_hand(cpu_number, player_number)

		if result == "player":
			print("Well done, you have won the round: "+results[player_number+results2[result]])
			player_score += 1

		elif result == "cpu":
			print("You have lost the round: "+results[player_number+results2[result]])
			cpu_score += 1

		elif result == "tie":
			print("You have drawn: "+results[player_number+results2[result]])

		print("The current score is: Player-" + str(player_score) + ", CPU-" + str(cpu_score) + "\n\n")

play_game()
