def is_valid_sudoku(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0  #usuwami liczbe do sprawdzenia

                if not is_valid(board, num, i, j):  # sprawdzenie liczby czy pasuje
                    board[i][j] = num  #przywroceeni liczby
                    return False

                board[i][j] = num  # prztwrocenie jestli jest git

    return True

def print_board(board): #funkcja tworzenie planszy
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -") #oddzielenie poziome po trzecim znaku w pionie

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ") #oddzielenie po trzecim znaku w poziomie

            if j == 8:
                print(board[i][j]) #plansza 9x9
            else:
                print(str(board[i][j]) + " ", end="") 

def find_empty_location(board): #przeszukuje plansze w poszukiwaniu 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0: 
                return (i, j)
    return None

def is_valid(board, num, row, col): 
    for i in range(9): 
        if board[row][i] == num or board[i][col] == num: #sprwdzenie czy znajduje sie liczba w kolumnie i wierszu
            return False #jesli znajdzie znaca False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3) #sprwadzenie czy znajduje sie liczba po kwadracie
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False #false jesli ktorakolwiek komurka ma liczbe

    return True

def solve_sudoku(board): 
    empty = find_empty_location(board) #wyszukuje pusta komorke, jesli nie ma gra jest rozwiazana

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10): #probuje wstawic cyfre w puste miejsce uwzgledniajac is_valid 
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0 

    return False #jesli false (nie ualo znalezc sie miejsca) funkcja wraca do board[row][col] = 0

board = (
        [[0, 0, 0, 4, 0, 0, 1, 9, 0],
         [0, 3, 0, 0, 0, 0, 8, 6, 0],
         [0, 0, 7, 0, 8, 3, 5, 0, 0],
         [0, 0, 0, 0, 0, 8, 6, 0, 0],
         [8, 0, 5, 1, 0, 8, 0, 0, 0],
         [0, 2, 0, 0, 0, 0, 3, 5, 0],
         [0, 8, 1, 0, 4, 0, 0, 0, 0],
         [0, 0, 0, 0, 7, 0, 0, 0, 0],
         [0, 4, 0, 2, 5, 0, 0, 0, 0]]
         )

if is_valid_sudoku(board) and solve_sudoku(board):
    print("Sudoku Solved:")
    print_board(board)
else:
    print("Invalid Sudoku or no solution exists")
