opponent_move = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

win_move = {"A": "B", "B": "C", "C": "A"}
lose_move = {"A": "C", "B": "A", "C": "B"}

your_move = {
    "X": -1,  # Rock
    "Y": 0,  # Paper
    "Z": 1,  # Scissors
}


def rps2(games: list) -> int:
    if not games:
        return 0

    score = 0

    for game in games:
        op, you = game.split(" ")

        if your_move[you] == 0:  # draw
            score += 3 + opponent_move[op]

        elif your_move[you] == 1:  # win
            my_win_move = win_move[op]
            score += 6 + opponent_move[my_win_move]

        else:  # win
            my_lose_move = lose_move[op]
            score += 0 + opponent_move[my_lose_move]

    return score


def rps(games: list) -> int:
    if not games:
        return 0

    score = 0

    for game in games:
        op, you = game.split(" ")

        if opponent_move[op] == your_move[you]:  # draw
            score += 3 + your_move[you]

        elif (
            (op == "A" and you == "Z")
            or (op == "B" and you == "X")
            or (op == "C" and you == "Y")
        ):  # lose
            score += 0 + your_move[you]
        else:  # win
            score += 6 + your_move[you]

        # if opponent_move[op] < your_move[you]:  # win
        #     score += 3 + your_move[you]
    return score


if __name__ == "__main__":
    with open("./Day2 - Rock Paper Scissors/input", "r") as fptr:
        arr = []
        elve = []
        games = fptr.read().split("\n")

        score = rps2(games)
        print(score)
