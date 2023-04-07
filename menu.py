from tkinter import *
import t3_game
import rps_game

p1_score = 0
p2_score = 0


def create_menu():
    # creating window
    root = Tk()
    # title window
    root.title("Main Menu")
    root.geometry("750x500")
    root.resizable(0, 0)

    # welcome label
    scores = Label(root, text="GAME MENU", font=(
        "Comic Sans", 30)).place(x=250, y=100)
    # Tic Tac Toe
    t3 = Button(height=3, width=12, font=("Comic Sans", 15),
                text="Tic-Tac-Toe", command=t3_game.start_game)
    t3.pack()
    t3.place(x=300, y=230)

    # Rock Paper Scissors
    rps = Button(height=3, width=20, font=(
        "Comic Sans", 15), text="Rock, Paper, Scissors", command=rps_game.rps_game)
    rps.pack()
    rps.place(x=260, y=320)

    # scoring!!
    scores = Label(root, bg='black', fg='white', text="Scores\n Player 1:"+t3_game.add_scores(1)+"\n Player 2:"+t3_game.add_scores(2), font=(
        "Comic Sans", 20)).place(x=0, y=0)

    # this runs the window
    root.mainloop()


# def t3_window():
#     t3_game_window = Toplevel(root)
#     t3_game.start_game


if __name__ == "__main__":
    create_menu()
