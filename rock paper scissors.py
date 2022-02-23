import random
rock = '''
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

player_choice_int = int(input("Choose 0 for rock, 1 for paper, 2 for scissors.\n"))
# win: 0-2, 1-0, 2-1
# lose: 2-0, 1-2 0-1

# win = -2, 1, 1
# lose = 2, -1, -1
options = [rock, paper, scissors]
player_choice = options[player_choice_int]
computer_choice_int = random.randint(0, 2)
computer_choice = options[computer_choice_int]
result = player_choice_int - computer_choice_int

print(f"You chose {player_choice}")
print(f"Computer chose {computer_choice}")

if result == -2 or result == 1:
    print("You win!")
elif result == 2 or result == -1:
    print("You lose!")
elif result == 0:
    print("Tie!")