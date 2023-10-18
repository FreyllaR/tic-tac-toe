def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_symbol = "X"

    print("Добро пожаловать в игру 'Крестики нолики'!")
    print_board(board)

    while True:
        print(f"Игрок {current_symbol}, ваш ход (строка [0-2], столбец [0-2]):")

        # Get row input
        while True:
            try:
                row = int(input("Введите строку: "))
                if row < 0 or row > 2:
                    print("Неверный ввод. Введите значение между 0 и 2.")
                else:
                    break
            except ValueError:
                print("Неверный ввод. Введите значение между 0 и 2.")

        # Get column input
        while True:
            try:
                col = int(input("Введите столбец: "))
                if col < 0 or col > 2:
                    print("Неверный ввод. Введите значение между 0 и 2.")
                else:
                    break
            except ValueError:
                print("Неверный ввод. Введите значение между 0 и 2.")

        if board[row][col] != " ":
            print("Ячейка уже занята. Попробуй еще.")
            continue

        board[row][col] = current_symbol
        print_board(board)

        if check_win(board, current_symbol):
            print(f"Игрок {current_symbol} победил!")
            break

        if all(cell != " " for row in board for cell in row):
            print("Ничья!")
            break

        current_symbol = "O" if current_symbol == "X" else "X"

if __name__ == "__main__":
    play_game()