import random 
while True:
    user_action =input("Enter a choice (Rock,paper,Scissors):")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice (possible_actions)

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
       if computer_action =="Scissors":
           print(f"Rock smashes scissors! You win!")
       else:
           print(f"Paper covers rock! You lose.")
    elif user_action == "Paper":
       if computer_action =="Rock":
           print(f"paper smashes rock! You win!")
       else:
           print(f"Scissors covers paper! You lose.")
    elif user_action == "Scissors":
       if computer_action =="paper":
           print(f"scissors smashes paper! You win!")
       else:
           print(f"Paper covers rock! You lose.")        
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
       break
           

           