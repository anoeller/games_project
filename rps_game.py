p1_score = 0
p2_score = 0


def rps_game():
    # Prompt users to input r, p, or s
    item1 = input(
        "Player 1 - Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors:\n").lower()
    item2 = input(
        "Player 2 - Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors:\n").lower()

    # check to see if valid input for r, p, or s
    if item1 == 'r' or item1 == 'p' or item1 == 's':
        pass
    else:
        item1 = input(
            "Player 1 entered invalid input.  Please enter 'r', 'p', or 's':\n")
    if item2 == 'r' or item2 == 'p' or item2 == 's':
        pass
    else:
        item2 = input(
            "Player 2 entered invalid input.  Please enter 'r', 'p', or 's':\n")

    # determine who wins
    # player 1 = r, player 2 = r,p,s
    if item1 == 'r':
        if item2 == 'r':
            print("It's a tie!")
        if item2 == 'p':
            print("Player 2 wins!")
            add_scores(2)
        if item2 == 's':
            print("Player 1 wins!")
            add_scores(1)
    # player 1 = s, player 2 = r,p,s
    if item1 == 's':
        if item2 == 's':
            print("It's a tie!")
        if item2 == 'p':
            print("Player 1 wins!")
            add_scores(1)
        if item2 == 'r':
            print("Player 2 wins!")
            add_scores(2)
    # player 1 = p, player 2 = r,p,s
    if item1 == 'p':
        if item2 == 'p':
            print("It's a tie!")
        if item2 == 's':
            print("Player 2 wins!")
            add_scores(2)
        if item2 == 'r':
            print("Player 1 wins!")
            add_scores(1)


def add_scores(play):
    global p1_score, p2_score
    if play == 1:
        p1_score += 1
        return str(p1_score-1)
    if play == 2:
        p2_score += 1
        return str(p2_score-1)
