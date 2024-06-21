import random

bot_list = ("rock", "paper", "scissor")
bot_score = 0
player_score = 0
round_no = 1

print("Welcome to rock paper scissor game!")
player_name = input("enter player name: ")
total_rounds=int(input("Enter number of rounds between '1' and '10'(both inclusive): "))
if total_rounds < 1:
    total_rounds = 1
    print("total rounds set to 1 due to input being less than 1.")
if total_rounds > 10:
    total_rounds = 10
    print("total rounds set to 10 due to input being greater than 10.")

while round_no <= total_rounds:
    print("enter your choice:\n1) rock \n2) paper \n3) scissor")
    player_choice = input()

    if player_choice == "rock":
        print("choice of",player_name,"is:",player_choice)
    elif player_choice == "paper":
        print("choice of",player_name,"is:",player_choice)
    elif player_choice == "scissor":
        print("choice of",player_name,"is:",player_choice)
    else:
        print("invalid choice")
    
    bot_choice=random.choices(bot_list)

    if bot_choice ==['rock']:
        print("bot choice is: rock")
    if bot_choice ==['paper']:
            print("bot choice is: paper")
    if bot_choice ==['scissor']:
        print("bot choice is: scissor")

    if bot_choice == ['paper'] and player_choice == "scissor":
        print(player_name,"won in round", round_no)
        player_score += 1
    elif bot_choice == ['paper'] and player_choice == "rock":
        print("Bot won in round", round_no)
        bot_score +=1
    elif bot_choice == ['scissor'] and player_choice == "paper":
        print("Bot won in round", round_no)
        bot_score +=1
    elif bot_choice == ['scissor'] and player_choice == "rock":
        print(player_name,"won in round", round_no)
        player_score += 1
    elif bot_choice == ['rock'] and player_choice == "paper":
        print(player_name,"won in round", round_no)
        player_score += 1
    elif bot_choice == ['rock'] and player_choice == "scissor":
        print("Bot won in round", round_no)
        bot_score +=1
    else:
        print("tie in round",round_no)
    
    round_no +=1
    if bot_score > player_score:
        print("bot leads the game by ", bot_score-player_score,"points")
    if bot_score < player_score:
        print(player_name,"leads by ",player_score-bot_score,"points")
    if bot_score == player_score:
        print("Scores tied up till now on ",bot_score-player_score,"point")

print("final score of bot is: ",bot_score)
print("final score of",player_name,"is",player_score)

if bot_score > player_score:
    final_score = bot_score - player_score
    print("bot won by ",final_score)
elif bot_score < player_score:
    final_score = player_score - bot_score
    print(player_name,"won by",final_score)
else:
    print("Its a tie.")