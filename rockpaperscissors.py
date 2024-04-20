import random

def Game(gamer_choice, comp_choice):
    if gamer_choice == comp_choice:
        return "It's a tie!"
    elif (gamer_choice == 'rock' and comp_choice == 'paper') or \
         (gamer_choice == 'paper' and comp_choice == 'scissors') or \
         (gamer_choice == 'scissors' and comp_choice == 'rock'):
        return "Computer wins!"
    else:
        return "You win!"

def main():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        print("Welcome to Rock,Paper,Scissors!")
        gamer_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if gamer_choice not in choices:
            print("Invalid choice! Please choose again.")
            continue
        
        comp_choice = random.choice(choices)
        print(f"The computer chooses: {comp_choice}")
        
        result = Game(gamer_choice, comp_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
