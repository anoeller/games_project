from tkinter import *
from tkinter import messagebox

# declare variables
player = 'X'
game = True
new_game = False
p1_score = 0
p2_score = 0
game_button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def clicked(row, col):
    """
    If box is "empty" (or zero) and clicked then 'X' or 'O' will be placed
    """
    global player, game_button

    print(game_board)

    # changes box to 'X' if clicked
    if player == 'X' and game_board[row][col] == 0 and game == True:
        game_button[row][col].configure(text='X')
        game_board[row][col] = 'X'
        player = 'O'

    # changes box to 'O' if clicked
    if player == 'O' and game_board[row][col] == 0 and game == True:
        game_button[row][col].configure(text="O")
        game_board[row][col] = 'O'
        player = 'X'

    check_winner()


def check_winner():
    """
    determines if 'X' or 'O' wins if three in a row/col or diagonal
    """
    global p1_score, p2_score, game, new_game

    # iterate through rows and cols to check winner
    for i in range(3):
        # CHECKS COLS
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != 0:
            game = False
            if game_board[0][i] == 'X':
                p1_win()
            if game_board[0][i] == 'O':
                p2_win()
            break

        # CHECKS ROWS
        elif game_board[i][0] == game_board[i][1] == game_board[i][2] != 0:
            game = False
            if game_board[i][0] == 'X':
                p1_win()
            if game_board[i][0] == 'O':
                p2_win()
            break

        # CHECK DIAGONAL
        elif game_board[0][0] == game_board[1][1] == game_board[2][2] != 0:
            game = False
            if game_board[0][0] == 'X':
                p1_win()
            if game_board[0][0] == 'O':
                p2_win()
            break
        elif game_board[0][2] == game_board[1][1] == game_board[2][0] != 0:
            game = False
            if game_board[1][1] == 'X':
                p1_win()
            if game_board[1][1] == 'O':
                p2_win()
            break

        # CHECK TIE
        elif game_board[0][0] and game_board[0][1] and game_board[0][2] and game_board[1][0] and game_board[1][1] and game_board[1][2] and game_board[2][0] and game_board[2][1] and game_board[2][2] != 0:
            game = False
            win_msg = messagebox.showinfo(
                message="Tie Game!")
            quit()

# not sure this is implemented well?


def add_scores(play):
    global p1_score, p2_score
    if play == 1:
        p1_score += 1
        return str(p1_score-1)
    if play == 2:
        p2_score += 1
        return str(p2_score-1)

# display if P1 wins


def p1_win():
    win_msg = messagebox.showinfo(
        message="Congratulations!\nPlayer 1 won!")
    add_scores(1)
    quit()


# display if P2 wins
def p2_win():
    win_msg = messagebox.showinfo(
        message="Congratulations!\nPlayer 2 won!")
    add_scores(2)
    quit()


def start_game(master):
    global root, new_game, game_board, game_button, player
    # creating game window
    if (new_game):
        root.destroy()
        new_game = False
        player = "X"
        game_button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    root = Tk()

    # title game window
    root.title("Tic-Tac-Toe!")
    root.geometry("414x455")
    root.resizable(0, 0)

    # iterate through board for formatting
    for i in range(3):
        for j in range(3):
            game_button[i][j] = Button(height=4, width=8, font=(
                "Comic Sans", 20), command=lambda row=i, col=j: clicked(row, col))
            game_button[i][j].grid(row=i, column=j)
    root.mainloop()


if __name__ == "__main__":
    start_game()
