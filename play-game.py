game_over = False
# decidindo a escolha do computador
from random import choice
import os

while not game_over:
    os.system('cls' if os.name == 'nt' else 'clear')
    options = ['rock', 'scissors', 'paper']
    computer_option = choice(options)

    # recebendo e checkando a escolha do usuario
    checked = False
    while not checked:
        user_input = input('choose:\n- rock\n- paper\n- scissors\n-> ')
        if user_input in options:
            checked = True
        else:
            print('Please, choose one of the three options.')

    # comparando
    user_wins = False
    computer_wins = False
    tie = False

    if user_input == 'rock':
        if computer_option == 'paper':
            computer_wins = True
        else:
            user_wins = True
    elif user_input == 'paper':
        if computer_option == 'scissors':
            computer_wins = True
        else:
            user_wins = True
    elif user_input == 'scissors':
        if computer_option == 'rock':
            computer_wins = True
        else: 
            user_wins = True
    elif user_input == computer_option: #empate
        tie = True

    # printando escolhas
    print(f'\nyour pick: {user_input}')
    print(f"machine's pick: {computer_option}")

    # parabenizando ganhador
    if user_wins:
        print('\nCongratulations, you won!')
    elif computer_wins:
        print('\nYou lose :(')
    elif tie:
        print('\nits a draw!')

    # perguntando se ele quer continuar ou parar de jogar
    while True:
        continue_game = input('\nWant to play again? (y/n)\n')
        if continue_game == 'n':
            print('\nThank you for playing!')
            game_over = True
            break
        if continue_game == 'y':
            break
        elif continue_game != 'y'and continue_game != 'n':
            print('Please, enter a valid key.')
