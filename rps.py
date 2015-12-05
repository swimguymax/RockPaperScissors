from random import randint

player_score = 0

cpu_score = 0

result = "null"

def play_hand(cpu, player):
	if cpu == player:
		result = "tie"

	elif (cpu == 2 and player == 1) or (cpu == 3 and player == 2) or (cpu == 1 and player == 3):
		result = "cpu"

	elif (player == 2 and cpu == 1) or (player == 3 and cpu == 2) or (player == 1 and cpu == 3):
		result = "player"

	return result

def play_game():
	
	while True:
		player_string = str(input("Enter rock, paper or scissors, or quit to leave the game"))

		cpu_number = randint(1, 3)

		if player_string == "quit":
			break

		elif player_string == "rock":
			player_number = 1

		elif player_string == "paper":
			player_number = 2

		elif player_string == "scissors":
			player_number = 3
			play_hand(cpu_number, player_number)

		if result == "player":
			print("Well done, you have won the round.")
			player_score = player_score + 1

		elif result == "cpu":
			print("You have lost the round.")
			cpu_score = cpu_score + 1

		elif result == "tie":
			print("You have drawn")

		print("The current score is Player:" + player_score + " CPU: " +cpu_score)

play_game()