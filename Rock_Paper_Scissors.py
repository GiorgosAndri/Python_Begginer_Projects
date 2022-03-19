import random

lista = ["rock", "paper", "scissors"]
computer_score = 0
user_score = 0
print("Welcome to the Rock, Paper, Scissors game!")
print("The rules are simple. Rock beats Scissors, Scissors beats paper and Paper beats Rock")
while True:
 computer_guess = lista[int(random.randint(0, 2))]
 user_guess = input("Choose Rock, Paper,Scissors or write Q to quit ").lower()
 if user_guess == "q":
     print("Bye :(")
     quit()
 if user_guess not in lista:
     print("You have to choose Rock, Paper or Scissors.")
     quit()
 if computer_guess == user_guess:
     print("You both chose the same. It's a draw")
 elif computer_guess == "rock" and user_guess == "scissors":
     print("The computer guessed: ", computer_guess)
     print("You guessed: ", user_guess)
     print("You lose")
     computer_guess += 1
 elif computer_guess == "paper" and user_guess == "rock":
     print("The computer guessed: ", computer_guess)
     print("You guessed: ", user_guess)
     print("You lose")
     computer_score += 1
 elif computer_guess == "scissors" and user_guess == "paper":
     print("The computer guessed: ", computer_guess)
     print("You guessed: ", user_guess)
     print("You lose")
     computer_score += 1
 else:
     print("The computer guessed: ", computer_guess)
     print("You guessed: ", user_guess)
     print("You win")
     user_score += 1
 print("Computer's score: ", computer_score)
 print("Your score: ", user_score)




