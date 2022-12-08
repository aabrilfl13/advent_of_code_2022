def which_elve_carrying_more(elves: list) -> int:
    calories_elves = []
    for i, elve in enumerate(elves, start=1):
        calories = 0
        for calorie in elve:
            calories += int(calorie)
        calories_elves.append(calories)

    calories_elves = sorted(calories_elves, reverse=True)

    total_maximun_calories = calories_elves[0] + calories_elves[1] + calories_elves[2]

    return total_maximun_calories


if __name__ == "__main__":
    with open("./input", "r") as fptr:
        arr = []
        elve = []
        lines = fptr.read().split("\n")
        for line in lines:
            if line:
                elve.append(line)
            else:
                arr.append(elve)
                elve = []

    calories = which_elve_carrying_more(arr)
    print(calories)
