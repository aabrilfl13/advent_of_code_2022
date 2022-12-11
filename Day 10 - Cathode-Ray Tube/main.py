DIR_PATH = __file__[:-8]


if __name__ == "__main__":
    with open(f"{DIR_PATH}/input", "r") as fptr:
        instructions = fptr.readlines()

        CICLES = 2
        queue = []

        x = 1
        solutions = []
        row = 0
        col = 0
        for i in range(1, 241):
            # Refresh queue
            for q in queue:
                q["cicles"] -= 1

            # Add value if queue has finished
            if queue and queue[0]["cicles"] == 0:
                x += queue.pop(0)["value"]

            # Do the command
            if instructions and not queue:
                instruction = instructions.pop(0)
                command = instruction.strip().split()
                if command[0] == "noop":
                    pass
                elif command[0] == "addx":
                    queue.append({"value": int(command[1]), "cicles": CICLES})

            if col - x in [-1, 0, 1]:
                print("#", end="")
            else:
                print(".", end="")

            col += 1

            # PART 1
            # if i in [20, 60, 100, 140, 180, 220]:
            #     print(i, ":", x, "- strength: ", x * i)
            #     solutions.append(x * i)

            # PART 2
            if i % 40 == 0:
                print("")
                row += 1
                col = 0

        # PART 1
        # print("Total stenght: ", sum(solutions))
