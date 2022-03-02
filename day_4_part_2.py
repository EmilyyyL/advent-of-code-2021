from sys import stdin

def check_win(board):
    for i in range(5):
        row = []
        for j in range(5):
            row.append(bool(board[i][j] is None))
        if all(row) is True:
            return True

    for i in range(5):
        col = []
        for j in range(5):
            col.append(bool(board[j][i] is None))
        if all(col) is True:
            return True
    
    return False

def calculate_score(board):
    total = 0
    for row in board:
        total += sum(filter(None, row))
    return total



numbers = list(map(int, input().split(",")))

boards = []
counter = 0
board = []
for line in stdin:
    if line.strip():
        board.append(list(map(int, filter(None, line.strip().split(" ")))))
        counter += 1
        if counter % 5 == 0:
            boards.append(board)
            board = []

min_num = 0
score = 0
numu = 0
for board in boards: 
    counter = 0
    for number in numbers:
        for i in range(5):
            for j in range(5):
                if board[i][j] == number:
                    board[i][j] = None
        if check_win(board):
            if counter > min_num:           # Only line difference from part 1
                min_num = counter
                score = calculate_score(board)
                numu = number
            break
        else:
            counter += 1

print(f"Final Score: {score * numu}")