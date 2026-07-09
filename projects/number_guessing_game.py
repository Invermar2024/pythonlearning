import random


def main():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Guess the number from 1 to 10.")

    while True:
        guess_text = input("Your guess: ")

        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Correct. You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()
