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
player1_score=0
player2_score=0

multiplayer=(input("Would you like to add another player? (y/n) ")).lower()

while True:
    if multiplayer not in ('y', 'n'):
        print(multiplayer, "is not a valid response.")

    if multiplayer=='y':
        for match in range(1,3):
            print("Match :", match)
            player1=input("Player 1: Rock, paper or scissors? (r/p/s) ")
            player2=input("Player 2: Rock, paper or scissors? (r/p/s) ")
            if (player1=="r" and player2=="s") or (player1=="s" and player2=="p") or (player1=="p" and player2=="r"):
                print("Player 1 wins!")
                player1_score+=1

            elif (player2=="r" and player1=="s") or (player2=="s" and player1 =='p') or (player2=="p" and player1=="r"):
                print("Player 2 wins")
                player2_score+=1

            elif player1==player2:
                print("Draw!")

        if player1_score==2:
            print("Congratulations Player 1! You are the overall winner.")
            print("Player 1 has won ", str(player1_score), "mathces. Player 2 has won ", str(player2_score), " matches.")
            break
        
        elif player2_score==2:
            print("Congratulations PLayer 2! You are the overall winner.")
            print("Player 1 has won ", str(player1_score), "mathces. PLayer 2 has won ", str(player2_score), " matches.") 
            break

    elif multiplayer=='n':
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
            print("You have won ", str(user_score), "mathces. Computer has won ", str(computer_score), " matches.")
            break
        
        elif computer_score==2:
            print("Oopsie! Computer is the overall winner.")
            print("You have won ", str(user_score), "mathces. Computer has won ", str(computer_score), " matches.") 
            break



    

    
    
    
            
    