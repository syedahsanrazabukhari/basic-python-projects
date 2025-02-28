import random

def computer_guesses():
    low, high = 1, 100
    attempts = 0
    
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    while True:
        if low > high:
            print("Hmm, something went wrong! Did you change your number?")
            break

        guess = random.randint(low, high)
        attempts += 1
        print(f"Is your number {guess}?")
        feedback = input("Enter 'h' if it's too high, 'l' if it's too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I guessed your number in {attempts} attempts! 🎉")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")

computer_guesses()

