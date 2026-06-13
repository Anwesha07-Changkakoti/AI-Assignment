import math

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():

    print()

    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate():

    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return 10 if row[0] == 'X' else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == 'X' else -10

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == 'X' else -10

    return 0

def moves_left():

    for row in board:
        if ' ' in row:
            return True

    return False

def minimax(depth, isMax):

    score = evaluate()

    if score == 10:
        return score

    if score == -10:
        return score

    if not moves_left():
        return 0

    if isMax:

        best = -1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == ' ':

                    board[i][j] = 'X'

                    best = max(
                        best,
                        minimax(depth + 1, False)
                    )

                    board[i][j] = ' '

        return best

    else:

        best = 1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == ' ':

                    board[i][j] = 'O'

                    best = min(
                        best,
                        minimax(depth + 1, True)
                    )

                    board[i][j] = ' '

        return best

def find_best_move():

    best_val = 1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == ' ':

                board[i][j] = 'O'

                move_val = minimax(0, True)

                board[i][j] = ' '

                if move_val < best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

while True:

    print_board()

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] != ' ':
        print("Cell already occupied!")
        continue

    board[row][col] = 'X'

    if evaluate() == 10:
        print_board()
        print("You Win!")
        break

    if not moves_left():
        print_board()
        print("Draw!")
        break

    ai_row, ai_col = find_best_move()

    board[ai_row][ai_col] = 'O'

    print(f"\nAI played at ({ai_row}, {ai_col})")

    if evaluate() == -10:
        print_board()
        print("AI Wins!")
        break

    if not moves_left():
        print_board()
        print("Draw!")
        break