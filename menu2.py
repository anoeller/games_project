from tkinter import *
import t3_game
import rps_game

# declare t3 game variables
player = 'X'
game = True
new_game = False
p1_score = 0
p2_score = 0
game_button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# creating window
root = Tk()

# title window
root.title("Main Menu")
root.geometry("750x500")
root.resizable(0, 0)


def t3_window():
    global root, new_game, game_board, game_button, player
    t3_top = Toplevel(root)
    # creating game window
    if (new_game):
        t3_top.destroy()
        new_game = False
        player = "X"
        game_button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # title game window
    t3_top.title("Tic-Tac-Toe!")
    t3_top.geometry("414x455")
    t3_top.resizable(0, 0)

    # iterate through board for formatting
    for i in range(3):
        for j in range(3):
            game_button[i][j] = Button(height=4, width=8, font=(
                "Comic Sans", 20), command=lambda row=i, col=j: t3_game.clicked(row, col))
            game_button[i][j].grid(row=i, column=j)
    t3_top.mainloop()


# def create_menu():
# welcome label
scores = Label(root, text="GAME MENU", font=(
    "Comic Sans", 30)).place(x=250, y=100)
# Tic Tac Toe
t3 = Button(height=3, width=12, font=("Comic Sans", 15),
            text="Tic-Tac-Toe", command=t3_window())
t3.pack()
t3.place(x=300, y=230)

# Rock Paper Scissors
rps = Button(height=3, width=20, font=(
    "Comic Sans", 15), text="Rock, Paper, Scissors", command=rps_game.rps_game)
rps.pack()
rps.place(x=260, y=320)

# scoring!!
scores = Label(root, bg='black', fg='white', text="Scores\n Player 1:"+(t3_game.add_scores(1)+rps_game.add_scores(1))+"\n Player 2:"+(t3_game.add_scores(2)+rps_game.add_scores(2)), font=(
    "Comic Sans", 20)).place(x=0, y=0)

# this runs the main menu window
root.mainloop()


# if __name__ == "__main__":
#     # create_menu()
