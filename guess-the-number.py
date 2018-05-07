import random
def game():
    secret = random.randint(1, 10)
    guesses = []
    while len(guesses) < 3:
        try:
            guess = int(input("Guess a number:"))
        except ValueError:
            print('{} is not a number'.format(guess))
        else:
            if guess == secret:
                print('Correct! The number was {}!'.format(guess))
                break
            elif guess < secret:
                print('Higher')
                guesses.append(guess)
            else:
                print('Lower')
                guesses.append(guess)
    else:
        print("Sorry, the number was {}".format(secret))
        play_again = input('Do you want to play again? Y/N')
        if play_again.lower() == 'y':
            game()
        else:
            print('See you next time!')
game()
