DIR_PATH = "Day 9 - Rope Bridge"

if __name__ == "__main__":
    with open(f"./{DIR_PATH}/input", "r") as fptr:
        actions = fptr.readlines()

    head = {"coors": [0, 0], "history_coors": {}}
    tail = {"coors": [0, 0], "history_coors": {}}

    for action in actions:
        move, positions = action.strip().split()

        for i in range(int(positions)):
            match move:
                case "R":
                    head["coors"][0] += 1
                case "L":
                    head["coors"][0] -= 1
                case "U":
                    head["coors"][1] += 1
                case "D":
                    head["coors"][1] -= 1

            diff_x = head["coors"][0] - tail["coors"][0]
            diff_y = head["coors"][1] - tail["coors"][1]

            if int(abs(diff_x)) > 1 or int(abs(diff_y)) > 1:
                tail["coors"][0] = (
                    tail["coors"][0] + int(diff_x / int(abs(diff_x)))
                    if diff_x != 0
                    else tail["coors"][0]
                )
                tail["coors"][1] = (
                    tail["coors"][1] + int(diff_y / int(abs(diff_y)))
                    if diff_y != 0
                    else tail["coors"][1]
                )

            if head["history_coors"].get(f"{head['coors'][0]}, {head['coors'][1]}"):
                head["history_coors"][f"{head['coors'][0]}, {head['coors'][1]}"] += 1
            else:
                head["history_coors"][f"{head['coors'][0]}, {head['coors'][1]}"] = 1

            if (
                tail["history_coors"].get(f"{tail['coors'][0]}, {tail['coors'][1]}")
                and not last_coord == tail["coors"]
            ):
                tail["history_coors"][f"{tail['coors'][0]}, {tail['coors'][1]}"] += 1
            else:
                tail["history_coors"][f"{tail['coors'][0]}, {tail['coors'][1]}"] = 1

            last_coord = tail["coors"].copy()

    print(f"Rope visit at least once {len(tail['history_coors'])} positions")
