###
# Write a program to simulate a game of Rock, Paper, Scissors.
# The game will prompt the player to choose rock, paper, or scissors by typing 'r',
# 'p', or 's'. The computer will randomly select its choice. The game will then display
# both choices using emojis and determine the winner based on the rules
###

import random

options={"r": "🪨","p": "📝", "s": "✂️"}

user_score=0
computer_score=0

while True:
    user_choice=input("Rock, paper or scissors? (r/p/s) ")
    uchoice_lower=user_choice.lower()
    computer_choice=random.choice(list(options.keys()))
        
    if uchoice_lower in list(options.keys()):
        print("You chose: ", options[uchoice_lower])
        print("Computer chose:", options[computer_choice])

        if (uchoice_lower=="r" and computer_choice=="s") or (uchoice_lower=="s" and computer_choice=="p") or (uchoice_lower=="p" and computer_choice=="r"):
            print("You win!")
            user_score+=1

        if (computer_choice=="r" and uchoice_lower=="s") or (computer_choice=="s" and uchoice_lower =='p') or (computer_choice=="p" and uchoice_lower=="r"):
            print("You lose!")
            computer_score+=1

        elif computer_choice==uchoice_lower:
            print("Draw!")

        
    else:
        print(uchoice_lower, "is not a valid response.")  

    if user_score==2:
        print("Congratulations! You are the overall winner.")
        break
    elif computer_score==2:
        print("Oopsie! Computer is the overall winner.") 
        break


    
    
    
            
    