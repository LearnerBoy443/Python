j=rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
games=[rock,paper,scissors]
print("Welcome to the game of rock paper scissors")
print("Enter 0 for rock, 1 for paper and 2 for scissors")
user_choice=(int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")))
print(games[user_choice])
computer_choice=random.randint(0,2)
print("Computer chose:")
print(games[computer_choice])
#if user_choice==0 and computer_choice==0:
 # print("It's a tie")
#elif user_choice== 0 and computer_choice==1:
 # print("You lose")
#elif user_choice== 0 and computer_choice==2:
#  print("You win")
#elif user_choice == 1 and computer_choice == 0:
 # print("You win")
#elif user_choice == 1 and computer_choice == 1:
 # print("It's a tie")
#elif user_choice == 1 and computer_choice == 2:
 # print("You lose")
#elif user_choice == 2 and computer_choice == 0:
 # print('You lose')
#elif user_choice == 2 and computer_choice == 1:
 # print("You win")
#elif user_choice == 2 and computer_choice ==2:
 # print("It's a tie")
#else:
 # print("Invalid input")
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
