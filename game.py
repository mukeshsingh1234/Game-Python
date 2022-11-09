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
choice = input("What do your choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
game_list = [rock, paper, scissors]
choice = int(choice)
if choice >=3 or choice < 0:
    print("You have entered an Invalid Number, You Lose!")
else:
    selected = (game_list[choice])
    print(f"You chose:\n{selected}")

    com = len(game_list)
    rand_num = random.randint(0, 2)
    com_choice = game_list[rand_num]
    print(f"Computer chose:\n{com_choice}")
    if choice ==0 and rand_num == 2:
        print("You win!")
    elif choice == 2 and rand_num ==0:
        print("You Lose!")
    elif rand_num > choice:
        print("You Lose!")
    elif choice < rand_num:
        print("You win!")
    elif rand_num == choice:
        print("It's a draw")
