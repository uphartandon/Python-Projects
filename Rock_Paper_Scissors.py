"""
This is Rock Paper & Scissors Game
"""

import random                #Importing random module
import time
Choice = ["Rock","Paper","Scissor"]
user_choices = {1:"Rock",2:"Paper",3:"Scissor"}

# print(user_choices.items())
# print(user_choices[1])
# print("System o/p is",Sys_Op)
# print(Sys_Op)

import emoji                 #Importing emoji module
# print(emoji.emojize(':thumbs_up:'))
# print(emoji.emojize(':thumbs_down:'))
# print(emoji.emojize(':grinning_face_with_big_eyes:'))

user_score=0
comp_score=0
Total_Chances = 10

print("WELCOME TO PLAY - ROCK PAPER & SCISSORS",emoji.emojize(':grinning_face_with_big_eyes:'))
time.sleep(2)
try:
    i=1
    while(i<10):    #Condition to run the game for 10 times

        print("\n"f"'This is your {i} round'" "\n"
        f"'And {Total_Chances-1} more rounds are Left'")
        Sys_Op = random.choice(Choice)
        print("\n" "Please provide your choice for playing this game")

        for key, value in user_choices.items():                 #Dynamic user input
            print("For", value, "Press", key, ":", "\n", end="")
        user_input = int(input())
        user_value = user_choices[user_input]
        # print("User value is",user_value)

        if user_value == Sys_Op:
            print("\n""Computer o/p was", Sys_Op)
            print("This match is drawn")
            user_score = user_score + 0
            comp_score = comp_score + 0
            print("Your Score is", user_score)
            print("System Score is", comp_score)


        elif (user_value=="Rock" and Sys_Op =="Scissor"):  #User Winning Conditions
            print("\n""Computer o/p was", Sys_Op)
            print("Great! You won the match",emoji.emojize(':thumbs_up:'))
            user_score +=1
            print("Your Score is",user_score)
            print("Computer score is",comp_score)

        elif (user_value == "Paper" and Sys_Op == "Rock"):
            print("\n""Computer o/p was", Sys_Op)
            print("Great! You won the match",emoji.emojize(':thumbs_up:'))

            user_score += 1
            print("Your Score is", user_score)
            print("Computer score is", comp_score)

        elif (user_value == "Scissor" and Sys_Op == "Paper"):
            print("\n""Computer o/p was", Sys_Op)
            print("Great! You won the match",emoji.emojize(':thumbs_up:'))
            user_score += 1
            print("Your Score is", user_score)
            print("Computer score is", comp_score)

        # System Winning Conditions
        elif (user_value == "Rock" and Sys_Op == "Paper"):
            print("\n""Computer o/p was", Sys_Op)
            print("Oops!""," "You lost","Computer won the match",emoji.emojize(':thumbs_down:'))
            comp_score += 1
            print("Your Score is", user_score)
            print("Computer score is", comp_score)

        elif (user_value == "Paper" and Sys_Op == "Scissor"):
            print("\n""Computer o/p was", Sys_Op)
            print("Oops!""," "You lost","Computer won the match",emoji.emojize(':thumbs_down:'))
            comp_score += 1
            print("Your Score is", user_score)
            print("Computer score is", comp_score)

        elif (user_value == "Scissor" and Sys_Op == "Rock"):
            print("\n""Computer o/p was", Sys_Op)
            print("Oops!""," "You lost","Computer won the match",emoji.emojize(':thumbs_down:'))
            comp_score += 1
            print("Your Score is", user_score)
            print("Computer score is", comp_score)

        Total_Chances -= 1
        i = i + 1
        time.sleep(3)


    if comp_score>user_score:
        print("Computers won the Series of 10 Matches",emoji.emojize(':grinning_face_with_big_eyes:'))
    elif comp_score<user_score:
        print("You won the Series of 10 Matches",emoji.emojize(':grinning_face_with_big_eyes:'))
    else:
        print("Series Drawn")

except Exception as e:
    print("Please provide the correct input")
