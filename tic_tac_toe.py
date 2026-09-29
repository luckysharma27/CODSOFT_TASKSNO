import math

board = [" " for _ in range(9)]

def print_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best

    best = math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(True)
            board[i] = " "
            best = min(best, score)
    return best

def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    print("=" * 45)
    print("       CODSOFT AI - TIC-TAC-TOE")
    print("=" * 45)
    print("You are X. AI is O.")
    print("Choose a position from 1 to 9:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        print_board()

        while True:
            try:
                position = int(input("Enter your position (1-9): "))
                index = position - 1

                if index < 0 or index > 8:
                    print("Please enter a number from 1 to 9.")
                elif board[index] != " ":
                    print("That position is already occupied.")
                else:
                    board[index] = "X"
                    break
            except ValueError:
                print("Please enter a valid number.")

        if check_winner("X"):
            print_board()
            print("You win!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        ai_move = best_move()
        board[ai_move] = "O"
        print("AI chose position:", ai_move + 1)

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
