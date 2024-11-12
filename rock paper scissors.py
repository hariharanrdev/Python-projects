import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Main function to play the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Choose rock, paper, or scissors. Let's see who wins!")

    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()