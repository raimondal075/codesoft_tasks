import random
import string

print("----- RANDOM PASSWORD GENERATOR -----")

password_length = int(input("Enter the desired password length: "))

uppercase_letters = string.ascii_uppercase   # A-Z 
lowercase_letters = string.ascii_lowercase   # a-zcls
digits = string.digits                       # 0-9
special_characters = string.punctuation      # !@#$%^&* etc.
all_characters = uppercase_letters + lowercase_letters + digits + special_characters

if password_length < 4:
	print("Please choose a length of at least 4 for a secure password.")
else:
	password = ""
	for i in range(password_length):
		random_character = random.choice(all_characters)
		password = password + random_character

	print(f"Your generated password is: {password}")
