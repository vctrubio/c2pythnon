
# FIND Directions
def dir_reduc_v1(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack    

def dir_reduc_v2(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dir_reduc_v2(dir3) if len(dir3) < len(arr) else dir3

# Tic Tak Toe validator 
def is_solved(board):
    for row in board:
        if all(value == row[0] and value != 0 for value in row):
            return row[0] 

    for col in range(3):
        if all(row[col] == board[0][col] and board[0][col] != 0 for row in board):
            print(row)
            return board[0][col] 

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    if all(value != 0 for row in board for value in row):
        return 0  # Cat's game
    return -1
'''
All function - all(value == row[0] and value != 0 for value in row)
for value in row: This part is a generator expression that iterates over each value in the row.

value == row[0] and value != 0: This is the condition that each value in the row must satisfy. It checks whether the current value is equal to the first element of the row (row[0]) and not equal to 0.

all(...): The all() function takes an iterable (in this case, the generator expression) and returns True if all elements in the iterable are true.
'''

#beer pyramid where bonus is the total money and price is price per beer_can, thus we need to stack them up as a pyramid
def beeramid(bonus, price):
    cans = bonus // price 
    level = 0
    total_cans_used = 0
    
    while total_cans_used <= cans:
        level +=1
        total_cans_used += max(0, level**2)  # Ensure that negative values are treated as 0
    return 0 if level == 0 else level - 1

if __name__ == '__main__':
    print('run lv5.')
