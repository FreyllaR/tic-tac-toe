import random


# Существующий код игры

def make_ai_move(board):
    # Выбираем случайную свободную клетку
    free_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_cells.append((i, j))

    if free_cells:
        row, col = random.choice(free_cells)
    else:
        row, col = None, None

    return row, col


def is_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False

    return True


def play_vs_ai():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        if player == "X":
            # Ход игрока
            row = int(input("Введите строку: "))
            col = int(input("Введите столбец: "))
            board[row][col] = player
        else:
            # Ход ИИ
            row, col = make_ai_move(board)
            if row is not None:
                board[row][col] = player

        # Проверка победы
        if check_win(board, player):
            print(f"Победил {player}!")
            break

            # Проверка ничьей
        if is_draw(board):
            print("Ничья!")
            break

        # Смена игрока
        player = "O" if player == "X" else "X"


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


def play_multiplayer():
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

            update_score(player)


# Добавим подсчет очков
player_1_score = 0
player_2_score = 0


def update_score(winner):
    global player_1_score, player_2_score
    if winner == "X":
        player_1_score += 1
    elif winner == "O":
        player_2_score += 1


# Вывод счета после игры
def show_score():
    print(f"Счет: {player_1_score} : {player_2_score}")


# Основная функция
def main():
    while True:
        mode = input("Выберите режим (1 - ИИ, 2 - Мультиплеер): ")

        if mode == "1":
            play_vs_ai()
        elif mode == "2":
            play_multiplayer()

        show_score()

main()
