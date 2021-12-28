import random

variants: list = ['rock', 'paper', 'scissors', 'lizard', 'spock']


def player_choice():
    """choice player"""
    while True:
        player: str = str(input('Your choice (rock paper scissors lizard spock)? '))
        if player not in variants:  # checking for player input errors
            print(f'Invalid input {player}')
        else:
            return player


def computer_choice(variants_f: list):
    """choice computer"""
    computer: str = variants_f[random.randint(0, 4)]  # randomly select a shape for the computer
    return computer


def examination(player_f, computer_f):
    """determining the winner"""
    print(player_f)
    print(computer_f)
    if player_f == 'rock' and (computer_f == 'scissors' or computer_f == 'lizard'):
        print('Player WIN!')
    elif player_f == 'paper' and (computer_f == 'rock' or computer_f == 'spock'):
        print('Player WIN!')
    elif player_f == 'scissors' and (computer_f == 'paper' or computer_f == 'lizard'):
        print('Player WIN!')
    elif player_f == 'lizard' and (computer_f == 'paper' or computer_f == 'spock'):
        print('Player WIN!')
    elif player_f == 'spock' and (computer_f == 'rock' or computer_f == 'scissors'):
        print('Player WIN!')
    elif player_f == computer_f:
        print("draw")
    else:
        print("Сomputer WIN!")


def main():
    while True:
        examination(player_choice(), computer_choice(variants))
        while True:
            game: str = str(input('Repeat (Y/N)?')).lower()  # the system asks the player if he wants to repeat the game

            if game == 'y':
                break
            elif game == 'n':
                exit()


main()
