import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts < max_attempts:
        print(f"You have {max_attempts - attempts} attempts left.")
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number!")
            return

        attempts += 1

    print("Sorry, you ran out of attempts. The number was:", secret_number)

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
