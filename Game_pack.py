import random



def main_menu():
    print('''There are 2 games that you can choose to play. \
    first game is guess the number game and the second game is rock,paper,scissor. ''')
    user_game = int(input('''which game do you want to play? \
    1. guessing number \
    2. rock,paper,scissor. \
    enter the number: '''))
    if user_game == 1:
        guessing_game()
    elif user_game == 2:
        modes()


def modes():
    print('''Nice. we have 3 modes to play RCP game. \
    mode 1: you and pc will play the game until one of you reaches 5 scores, whoever reached faster, is the winner\
    mode 2: you are the only player. if you reach -5, you lose and if you reach 5, you win.\
    mode 3: you and pc play for 10 times. after 10 times whoever reaches the highest score is the winner''')
    user_mode = int(input('which mode you want to play? 1, 2, 3? enter the number: '))
    if user_mode == 1:
        mode_1()
    elif user_mode == 2:
        mode_2()
    elif user_mode == 3:
        mode_3()


# first game


def guessing_game():
    while True:
        user_chances = int(input("how many chances do you want? "))
        if 50 >= user_chances >= 3:
            print('Great! you have', user_chances, 'chances to guess.')
            break
        else:
            print('your chances must be between the range of 3 to 50, try again')
    while True:
        start_number = int(input('what is the start number?: '))
        end_number = int(input('what is the end number?: '))
        subtract = abs(start_number - end_number)
        if subtract >= 50:
            print("thank you! now the game starts! let's have some fun!! ")
            break
        else:
            print('the gap less than 50 is not valid.')
    the_number = random.randrange(start=start_number, stop=end_number)
    user_chances1 = user_chances
    while user_chances1 > 0:
        guess1 = int(input('guess the number!: '))
        if guess1 == the_number:
            print("Bravo! That's right!")
            break
        elif guess1 > the_number:
            user_chances -= 1
            print('Nope! Try again. You have', user_chances, 'chance(s) left')
            print('the number is less than ', guess1)
        elif guess1 < the_number:
            user_chances -= 1
            print('Nope! Try again. You have', user_chances, 'chance(s) left')
            print('the number is greater than', guess1)
        if user_chances == 0:
            print('Sorry, your chances reached the limit!')
            break


# rock paper scissor game different modes:
def mode_1():
    user_score = 0
    pc_score = 0

    while True:
        valid_inputs = ['scissors', 'rock', 'paper']
        pc_input = random.choice(valid_inputs)
        user_input = input('rock, paper, scissors?: ')

        if (user_input == 'scissors' and pc_input == 'rock') or\
                (user_input == 'paper' and pc_input == 'scissors') or\
                (user_input == 'rock' and pc_input == 'paper'):
            pc_score += 1
            print('Wrong guess. PC score:', pc_score)
        elif (user_input == 'rock' and pc_input == 'scissors') or\
                (user_input == 'scissors' and pc_input == 'paper') or\
                (user_input == 'paper' and pc_input == 'rock'):
            user_score += 1
            print('Right. Your score:', user_score)
        elif (user_input == 'rock' and pc_input == 'rock') or\
                (user_input == 'scissors' and pc_input == 'scissors') or\
                (user_input == 'paper' and pc_input == 'paper'):
            print('no score; said the same item.')

        if user_score == 5:
            print('You won the game! Congratulations!')
            break
        elif pc_score == 5:
            print('Sorry! PC won the game!')
            break


def mode_2():
    total_score = 0
    # game will continue until it reaches -1 or 2.
    while -1 <= total_score < 2:
        key_words = ['scissors', 'paper', 'rock']
        pc_input = random.choice(key_words)
        user_input = input('rock paper scissors?: ')
        score = 0

        if (pc_input == 'rock' and user_input == 'scissors') or \
                (pc_input == 'scissors' and user_input == 'paper') or \
                (pc_input == 'paper' and user_input == 'rock'):
            score -= 1
            print('you lost a point')
        elif (pc_input == 'scissors' and user_input == 'rock') or \
                (pc_input == 'paper' and user_input == 'scissors') or \
                (pc_input == 'rock' and user_input == 'paper'):
            score += 1
        elif (user_input == 'rock' and pc_input == 'rock') or\
                (user_input == 'scissors' and pc_input == 'scissors') or\
                (user_input == 'paper' and pc_input == 'paper'):
            print('no score; said the same item.')
        total_score += score
        print(f"You've got {total_score}, scores!")
        if total_score == 2:
            print('you won.')
        elif total_score == -2:
            print('you lost.')


def mode_3():
    rounds_played = 0
    user_score = 0
    pc_score = 0
    while rounds_played < 5:
        valid_inputs = ['scissors', 'rock', 'paper']
        user_input = input('rock, paper, scissors?: ')
        pc_input = random.choice(valid_inputs)
        if (user_input == 'scissors' and pc_input == 'rock') or\
                (user_input == 'paper' and pc_input == 'scissors') or\
                (user_input == 'rock' and pc_input == 'paper'):
            pc_score += 1
            print('Wrong guess. PC score:', pc_score, '. Your score: ', user_score)
        elif (user_input == 'rock' and pc_input == 'scissors') or\
                (user_input == 'scissors' and pc_input == 'paper') or\
                (user_input == 'paper' and pc_input == 'rock'):
            user_score += 1
            print('Right. Your score:', user_score, '. Pc score: ', pc_score)
        elif (user_input == 'rock' and pc_input == 'rock') or\
                (user_input == 'scissors' and pc_input == 'scissors') or\
                (user_input == 'paper' and pc_input == 'paper'):
            print('no score; said the same item.')
        rounds_played += 1
    if user_score > pc_score:
        print('Your score: ', user_score, ', pc score: ', pc_score, '. You are the winner.')
    elif user_score < pc_score:
        print('Your score: ', user_score, ', pc score: ', pc_score, '. Pc is the winner.')


user_name = input('what is your name? \U0001f970 ')
name = user_name
print(f'hello {name}')
main_menu()

# to ask user if they want to play or not.
while True:
    start_over = int(input('Do you want to play again? if yes, type 0 if not type 1: '))
    if start_over == 0:
        print('really happy to play with you again! \U0001f607 ')
        main_menu()
    else:
        print('had a nice time with you! I hope you come back soon!  bye.')
        break
