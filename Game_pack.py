import random

def main_menu():
    print('''There are 2 games that you can choose to play. \n
first game is guess the number game and the second game is rock,paper,scissor. ''')
    user_game = int(input('''which game do you want to play? \n
    1. guessing number \n
    2. rock,paper,scissor. \n
enter the number: '''))
    if user_game == 1:
        guessing_game()
    elif user_game == 2:
        choosen_mode()

def choosen_mode():
    user = input('''do you want to play rock,paper,scissors with pc or another user?: \n
                 if with pc : 0
                 if with user : 1
                ''')
    if user == 0:
        pc_modes()
    elif user == 1:
        user_modes()

def pc_modes():
    print('''Nice. we have 3 modes to play RCP game. \n
    mode 1: you and pc will play the game until one of you reaches specific score, whoever reached faster, is the winner.\n
    mode 2: you are the only player. you can choose lost point and win point for example -2 you lose, 2 you win.\n
    mode 3: you and pc play for your chosen times. after times is over, whoever reaches the highest score is the winner. \n
    mode 4: there are two users playing. ''')
    user_mode = int(input('which mode you want to play? 1, 2, 3? enter the number: '))
    if user_mode == 1:
        pc_mode_1()
    elif user_mode == 2:
        pc_mode_2()
    elif user_mode == 3:
        pc_mode_3()


def user_modes():
    print('''Nice. we have 3 modes to play RCP game. \n
        mode 1: you and another user will play the game until one of you reaches specific score,\
whoever reached faster,is the winner.\n
        mode 2: you can choose lost point and win point. for example -2 you lose, 2 you win.\n
        mode 3: you and another user play for the chosen times. after times is over,\
whoever reaches the highest score is the winner. ''')
    user_choice = int(input('which mode you want to play? 1, 2, 3? enter the number: '))
    if user_choice == 1:
        user_mode_1()
    elif user_choice == 2:
        user_mode_2()
    elif user_choice == 3:
        user_mode_3()


def user_mode_1():
    user1_scores = 0
    user2_scores = 0
    username1 = input('first user please enter your name: ')
    username2 = input('second user please enter your name: ')
    chances = int(input('until what score you want to play?'))

    while True:
        user1 = input('rock, paper, scissors?: ')
        user2 = input('rock, paper, scissors?: ')
        if (user2 == 'scissors' and user1 == 'rock') or \
                (user2 == 'paper' and user1 == 'scissors') or \
                (user2 == 'rock' and user1 == 'paper'):
            user1_scores += 1
            print(f'{username2} is wrong. {username1}:', user1_scores)
        elif (user2 == 'rock' and user1 == 'scissors') or \
                (user2 == 'scissors' and user1 == 'paper') or \
                (user2 == 'paper' and user1 == 'rock'):
            user2_scores += 1
            print(f"{username1} is wrong. {username2}'s score:", user2_scores)
        elif (user2 == 'rock' and user1 == 'rock') or \
                (user2 == 'scissors' and user1 == 'scissors') or \
                (user2 == 'paper' and user1 == 'paper'):
            print('no score; said the same item.')

        if user1_scores == chances:
            print(f'{username1} won the game! Congratulations!')
            break
        elif user2_scores == chances:
            print(f'{username2} won the game!')
            break

def user_mode_2():
    user1_total_score = 0
    user2_total_score = 0
    first_username = input('first user please enter your name: ')
    second_username = input('second user please enter your name: ')
    user1_win_point = int(input(f'{first_username} please choose the winning point: '))
    user1_lost_point = int(input(' please choose the losing point: '))
    user1_scores = 0
    user2_scores = 0
    # game will continue until it reaches win point or losing point
    while user1_win_point > user1_total_score >= user1_lost_point:
        user1 = input(f'{first_username}, rock, paper, scissors?: ')
        user2 = input(f'{second_username}, rock, paper, scissors?: ')
        if (user2 == 'scissors' and user1 == 'rock') or \
            (user2 == 'paper' and user1 == 'scissors') or \
            (user2 == 'rock' and user1 == 'paper'):
            user1_scores += 1
            user1_total_score += user1_scores
            print(f'{second_username} is wrong. {first_username}:', user1_scores)
            print(f'{first_username} : {user1_total_score} vs {second_username} : {user2_total_score}')
        elif (user2 == 'rock' and user1 == 'scissors') or \
            (user2 == 'scissors' and user1 == 'paper') or \
            (user2 == 'paper' and user1 == 'rock'):
            user2_scores += 1
            user2_total_score += user2_scores
            print(f'{first_username} is wrong. {second_username} score: {user2_scores}')
            print(f'{first_username} : {user1_total_score} vs {second_username} : {user2_total_score}')

        elif (user2 == 'rock' and user1 == 'rock') or \
            (user2 == 'scissors' and user1 == 'scissors') or \
            (user2 == 'paper' and user1 == 'paper'):
            print('no score; said the same item.')
            print(f'{first_username} : {user1_total_score} vs {second_username} : {user2_total_score}')

        if user1_total_score == user1_win_point:
            print(f'{first_username} is the winner with {user1_total_score}scores!')
            break
        elif user1_total_score == user1_lost_point:
            print(f'''{first_username} has lost the game with {user1_total_score} scores!\n
                        {second_username} is the winner with {user2_total_score}.!''')
            break
        elif user2_total_score == user1_win_point:
            print(f'{second_username} is the winner with {user2_total_score}scores!')
            break
        elif user2_total_score == user1_lost_point:
            print(f'''{second_username} has lost the game with {user2_total_score} scores!\n
                    {first_username}is the winner with {user1_total_score}.''')
            break


def user_mode_3():
    rounds_played = 0
    rounds = int(input('how many times do you want to play?: '))
    username1 = input('first user please enter your name: ')
    username2 = input('second user please enter your name: ')
    user1_scores = 0
    user2_scores = 0
    while rounds_played < rounds:
        user1 = input('rock, paper, scissors?: ')
        user2 = input('rock, paper, scissors?: ')
        if (user2 == 'scissors' and user1 == 'rock') or \
                (user2 == 'paper' and user1 == 'scissors') or \
                (user2 == 'rock' and user1 == 'paper'):
            user1_scores += 1
            print('Wrong guess. second user:', user1_scores)
        elif (user2 == 'rock' and user1 == 'scissors') or \
                (user2 == 'scissors' and user1 == 'paper') or \
                (user2 == 'paper' and user1 == 'rock'):
            user2_scores += 1
            print('Right. Your score:', user2_scores)
        elif (user2 == 'rock' and user1 == 'rock') or \
                (user2 == 'scissors' and user1 == 'scissors') or \
                (user2 == 'paper' and user1 == 'paper'):
            print('no score; said the same item.')
        rounds_played += 1
        if user1_scores > user2_scores:
            print(
                f"{username1} score: {user1_scores}; {username2} score: {user2_scores}. {username1} is the winner.")
        elif user1_scores < user2_scores:
            print(
                f"{username1} score: {user1_scores}; {username2} score: {user2_scores}. {username2} is the winner.")
        elif user1_scores == user2_scores:
            print(f'there is no winner or loser. {user1_scores}:{user2_scores}')

def pc_mode_1():
    user_score = 0
    pc_score = 0
    chances = int(input('until what score you want to play?'))

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

        if user_score == chances:
            print('You won the game! Congratulations!')
            break
        elif pc_score == chances:
            print('Sorry! PC won the game!')
            break

def pc_mode_2():
    total_score = 0
    win_point = int(input('choose the winning point: '))
    lost_point = int(input('choose the losing point: '))
    # game will continue until it reaches win point or losing point
    while lost_point <= total_score < win_point:
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
        print(f"You've got {total_score} scores!")
        if total_score == win_point:
            print('you won.')
        elif total_score == lost_point:
            print('you lost.')


def pc_mode_3():
    rounds_played = 0
    user_score = 0
    pc_score = 0
    choosen_rounds = int(input('how many times do you want to play?: '))
    while rounds_played < choosen_rounds:
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



while True:
    start_over = int(input('Do you want to play again? if yes, type 0 if not type 1: '))
    if start_over == 0:
        print('really happy to play with you again! \U0001f607 ')
        main_menu()
    else:
        print('had a nice time with you! I hope you come back soon!  bye.')
        break

