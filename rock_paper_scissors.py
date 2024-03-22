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

import random
get_input = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print("You chose:")
if get_input == 0:
    print(rock)
elif get_input == 1:
    print(paper)
elif get_input == 2:
    print(scissors)

print("AI chose:")
AI_input = random.randint(0, 2)
if AI_input == 0:
    print(rock)
elif AI_input == 1:
    print(paper)
elif AI_input == 2:
    print(scissors)

if AI_input == 1 and get_input == 2:
    print("You Win!")
elif AI_input == 2 and get_input == 0:
    print("You Win!")
elif AI_input == 0 and get_input == 1:
    print("You Win!")   
elif AI_input == get_input:
    print("Draw!")
else:
    print("AI Win!")