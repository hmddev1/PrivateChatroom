# #f string
# x = 45
# print(f"I am {x}")

# #Distance between earth and sun
# print("What is distance between earth and sun?")
# kms = input()
# au = float(kms) / 149080000
# print(f"Okay, You saied the distance between earth and sun is {kms} equals {au} AU!")

#Play RSP with computer
import random

player = input("Hey! What is your move babe? ").lower()

num = random.randint(0,2)
if num == 0:
   computer = "rock"
elif num == 1:
   computer = "scissors" 
elif num == 2:
   computer = "paper"

print(f"computer plays {computer}")

if player == "rock" and computer == "scissors":
   print(f"You choose {palyer} so you win honey! :)) ")
else: 
      print("computer wins! :( ")
if player == "paper" and computer == "rock":
   print("Player wins!")




# player1 = input("what is your move number 1?").lower()
# player2 = input("what is your move number 2?").lower()

# if player1 == "rock" and player2 == "paper":
#    print(f"you choose {player1}, player2 wins!")
# elif player1 == "scissors" and player2 == "rock":
#    print("Yay!")
