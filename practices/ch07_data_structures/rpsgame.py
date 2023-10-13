import random

rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper']
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors']
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock']
    },
}



def main():
    show_header()
    play_game("You", "Computer")

def show_header():
    print("-----------------------------")
    print(" Rock Paper Scissors V1")
    print("-----------------------------")

def play_game(player_1, player_2):
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0
    wins = {
        
    }

    roll_names = list(rolls.keys())

    while wins_p1 < rounds and  wins_p2  < rounds:
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Can't play that, exiting")
            continue

        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie!")
        else:
            print(f"{winner} takes the round")
            if winner == player_1:
                wins_p1 += 1
            elif winner == player_2:
                wins_p2 += 1

        print(f"Score is {player_1}: {wins_p1} and {player_2}: {wins_p2}.")
        print()

    overall_winner = None
    if wins_p1 >= rounds:
        overall_winner = player_1
    else:
        overall_winner = player_2

    print(f"{overall_winner} wins the game!")

def find_winner(wins, names):
    return False

def check_for_winning_throw(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("The play was tied")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2
    return winner

def get_roll(player_name, rolls):
    print("Available rolls:")
    for index, r in enumerate(rolls, start=1):
        print(f"{index}. {r}")
    
    selected_index = int(input(f"{player_name}, what is your roll? ")) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {selected_index+1} is our of bounds!")
        return None
    
    return rolls[selected_index]

if __name__ == '__main__':
    main()
