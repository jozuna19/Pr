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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
uzr_choose = int(input("Let's play Rock, Paper, Scissors! Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))

if uzr_choose >= 3 or uzr_choose < 0:
    print("Invalid number, you lose")
else:
    print(game_images[uzr_choose])

    comp_choose = random.randint(0,2)
    print("Computer Chose:")
    print(game_images[comp_choose])

    #UDEMY RPS LOGIC
    if uzr_choose == 0 and comp_choose == 2:
        print("You win")
    elif comp_choose == 0 and uzr_choose == 2:
        print("You lose")
    elif comp_choose > uzr_choose:
        print("You lose")
    elif uzr_choose > comp_choose:
        print("You win")
    elif comp_choose == uzr_choose:
        print("You tied")


#RPS Logic
# if uzr_choose == 0 and comp_choose == 1:
#     print("You lose")
# elif uzr_choose == 0 and comp_choose == 2:
#     print("You win")
# elif uzr_choose == 0 and comp_choose == 0:
#     print("You tied")

# if uzr_choose == 1 and comp_choose == 2:
#     print("You lose")
# elif uzr_choose == 1 and comp_choose == 0:
#     print("You win")
# elif uzr_choose == 1 and comp_choose == 1:
#     print("You tied")

# if uzr_choose == 2 and comp_choose == 0:
#     print("You lose")
# elif uzr_choose == 2 and comp_choose == 1:
#     print("You win")
# elif uzr_choose == 2 and comp_choose == 2:
#     print("You tied")





#Logic
"""
0 vs O TIE
0 vs 1 LOSE
0 vs 2 WIN

1 vs 1 TIE
1 vs 0 WIN
1 vs 2 LOSE

2 vs 2 TIE
2 vs 0 LOSE
2 vs 1 WIN
"""