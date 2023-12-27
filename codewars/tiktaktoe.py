SIZE = 3

'''
1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C
'''


def print_board(board):
    for i, row in enumerate(board):
        print(f'{i + 1}| {row}')
    print([chr(65 + i) for i in range(SIZE)])


def get_board_cord(board, tuple):
    return board[tuple[0]][tuple[1]]


def rtn_cord(cord):
    letter_to_index = {chr(65 + i): i for i in range(SIZE)}
    # print(letter_to_index)
    letter, number = cord[0], cord[1]
    # print(letter, number)
    letter_index = letter_to_index[letter.upper()]
    # print(letter_index)
    number_index = int(number) - 1
    # print(number_index)
    if letter_index not in range(SIZE) or number_index not in range(SIZE):
        print('!Invalid input')
        return None
    return (number_index, letter_index)


def init():
    board = [[0] * SIZE for _ in range(SIZE)]  # board = [[0] * SIZE] * SIZE
    print('Board Initialized')
    print_board(board)
    return board


def run(board):
    def board_is_not_full(board):
        # for row in board:
        #     for cell in row:
        #         if cell == 0:
        #             return True
        # return False
        return any(cell == 0 for row in board for cell in row)

    def check_winner(board):
        # Check rows
        for row in board:
            if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
                return row[0]

        # Check columns
        for col in range(3):
            if all(board[row][col] == 'X' for row in range(3)) or all(board[row][col] == 'O' for row in range(SIZE)):
                return board[0][col]

        # Check diagonals
        if all(board[i][i] == 'X' for i in range(SIZE)) or all(board[i][i] == 'O' for i in range(SIZE)):
            return board[0][0]

        if all(board[i][2 - i] == 'X' for i in range(SIZE)) or all(board[i][2 - i] == 'O' for i in range(SIZE)):
            return board[0][2]

        return None

    turn = 1
    while board_is_not_full(board):
        if turn % 2 == 1:
            player = 'X'
        else:
            player = 'O'

        print(f'Player {player}\'s turn')
        cord = rtn_cord(input('Enter cord: '))
        if cord is not None:
            if get_board_cord(board, cord) == 0:
                board[cord[0]][cord[1]] = player
                print_board(board)
                turn += 1
            else:
                print('!Cell is already filled')
        if check_winner(board):
            ptr = check_winner(board)
            print(f'Player {ptr} won')
            break


if __name__ == '__main__':
    run(init())
