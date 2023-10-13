
# Decide who goes first
# Create "board"
# Choose which column to play
# First to 4 in a row wins

def main():
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    active_player_index = 0
    players = ["Zach", "Computer"]
    symbols = ["X", "O"]
        
    print(board[3])


if __name__ == '__main__':
    main()