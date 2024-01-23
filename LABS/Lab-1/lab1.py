# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Neron Parmar 
# Student Number: 171690217
#

def wins_rock_scissors_paper(player_throw, opponent_throw):
	player1 = player_throw.lower()
	player2 = opponent_throw.lower()

	# taking if else loop
	#if player wins
	if player1 == 'rock' and player2 == 'scissors':
		return True
	elif player1 == 'paper' and player2 == 'rock':
		return True
	elif player1 == 'scissors' and player2 == 'paper':
		return True
	#if player loss
	else:
		return False

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

	digit = int(input("Enter the digit: "))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b  # Corrected indentation
        return b


def sum_to_goal(number, goals):
	for i in range(len(number)):
		for j in range(i + 1, len(number)):
			if number[i] + number[j] == goals:
				return number[i] * number[j]
	return 0

class UpCounter:
    def __init__(self, step_size=1):
        self.count_value = 0
        self.step_size = step_size

    def count(self):
        return self.count_value

    def update(self):
        self.count_value += self.step_size

class DownCounter(UpCounter):
    def update(self):
        self.count_value -= self.step_size
