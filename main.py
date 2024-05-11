import random


def set_difficulty():
    EASY_LEVEL = 10
    HARD_LEVEL = 5
    level = input("Choose the difficulty level: Type easy/hard: ").lower()

    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


#checks user guess against the answer and returns lives left
def compare(user_guess, correct_answer, lives):
    if user_guess < correct_answer:
        print("Too low")
        return lives - 1

    elif user_guess > correct_answer:
        print("Too high")
        return lives - 1

    else:
        print("That's correct. You win!")


def play_game():
    print("I am thinking of a number between 1 and 100!")
    answer = random.randint(1, 100)
    #print(f"Psst, Correct answer: {answer}")

    tries = set_difficulty()
    guess = 0

    #repeat the process until user gets it right or has tries left.
    while guess != answer:
        print(f"You have {tries} attempts left.")

        guess = int(input("Make a guess: "))
        tries = compare(guess, answer, tries)

        if tries == 0:
            print("No attempts left. You lose!")
            return

        elif guess != answer:
            print("Guess again")


play_game()





