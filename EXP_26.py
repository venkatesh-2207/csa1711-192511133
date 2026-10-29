


def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")
    print()


def check_winner(board, player):
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        all(board[i] == player for i in line)
        for line in winning_lines
    )


def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def computer_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def main():
    board = [" "] * 9
    print("Tic-Tac-Toe: You are X, Computer is O")
    print("Choose positions 1 to 9.")

    while True:
        display_board([
            str(i + 1) if cell == " " else cell
            for i, cell in enumerate(board)
        ])

        try:
            position = int(input("Enter your position (1-9): ")) - 1
        except ValueError:
            print("Enter a valid number.")
            continue

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid or occupied position. Try again.")
            continue

        board[position] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("You win!")
            break

        if " " not in board:
            display_board(board)
            print("It's a draw!")
            break

        move = computer_move(board)
        board[move] = "O"
        print("Computer chooses position", move + 1)

        if check_winner(board, "O"):
            display_board(board)
            print("Computer wins!")
            break

        if " " not in board:
            display_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
