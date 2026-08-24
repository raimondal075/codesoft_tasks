import random

def get_computer_choice():
	"""Randomly select rock, paper, or scissors for the computer."""
	options = ["rock", "paper", "scissors"]
	return random.choice(options)

def get_user_choice():
	"""Ask the user for their choice and validate it."""
	while True:
		choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
		if choice in ["rock", "paper", "scissors"]:
			return choice
		else:
			print("Invalid choice! Please type rock, paper, or scissors.\n")

def decide_winner(user_choice, computer_choice):
	"""
	Determine the result of the round.
	Returns "win", "lose", or "tie" from the user's perspective.
	"""
	if user_choice == computer_choice:
		return "tie"

	beats = {
		"rock": "scissors",
		"scissors": "paper",
		"paper": "rock"
	}

	if beats[user_choice] == computer_choice:
		return "win"
	else:
		return "lose"

def play_game():
	print("=" * 40)
	print("   WELCOME TO ROCK - PAPER - SCISSORS")
	print("=" * 40)
	print("Rules:")
	print(" - Rock beats Scissors")
	print(" - Scissors beat Paper")
	print(" - Paper beats Rock")
	print(" - Same choice = Tie")
	print("=" * 40)

	user_score = 0
	computer_score = 0
	round_number = 1

	while True:
		print(f"\n----- Round {round_number} -----")

		user_choice = get_user_choice()
		computer_choice = get_computer_choice()

		result = decide_winner(user_choice, computer_choice)

		print(f"\nYour choice     : {user_choice}")
		print(f"Computer's choice: {computer_choice}")

		if result == "tie":
			print("Result: It's a TIE!")
		elif result == "win":
			print("Result: You WIN this round!")
			user_score += 1
		else:
			print("Result: You LOSE this round!")
			computer_score += 1

		print(f"\nScore -> You: {user_score}  |  Computer: {computer_score}")

		play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
		while play_again not in ["yes", "no", "y", "n"]:
			play_again = input("Please enter 'yes' or 'no': ").strip().lower()

		if play_again in ["no", "n"]:
			break

		round_number += 1

	print("\n" + "=" * 40)
	print("           FINAL SCORE")
	print("=" * 40)
	print(f"You: {user_score}   |   Computer: {computer_score}")

	if user_score > computer_score:
		print("Congratulations! You won the overall game!")
	elif user_score < computer_score:
		print("Computer won the overall game. Better luck next time!")
	else:
		print("The overall game is a TIE!")

	print("\nThanks for playing! Goodbye.")

# Entry point of the program
if __name__ == "__main__":
	play_game()
