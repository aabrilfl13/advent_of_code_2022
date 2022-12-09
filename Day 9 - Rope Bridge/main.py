from dataclasses import dataclass, field
from typing import Any

DIR_PATH = "Day 9 - Rope Bridge"


@dataclass
class Coors:
    x: int
    y: int


@dataclass
class Knot:
    id: int
    coors: Coors
    prev_knot: Any | None = None
    next_knot: Any | None = None
    history_coors: dict[str, int] = field(default_factory=dict)


if __name__ == "__main__":
    with open(f"./{DIR_PATH}/input", "r") as fptr:
        actions = fptr.readlines()

    NUM_OF_KNOTS = 9

    knots = [Knot(id=0, coors=Coors(x=0, y=0))]
    for i in range(1, NUM_OF_KNOTS + 1):
        tail = Knot(id=i, coors=Coors(x=0, y=0))
        tail.prev_knot = knots[i - 1]
        knots[i - 1].next_knot = tail
        knots.append(tail)
    head = knots.pop(0)

    for action in actions:
        move, positions = action.strip().split()

        for i in range(int(positions)):
            match move:
                case "R":
                    head.coors.x += 1
                case "L":
                    head.coors.x -= 1
                case "U":
                    head.coors.y += 1
                case "D":
                    head.coors.y -= 1

            for knot in knots:
                diff_x = knot.prev_knot.coors.x - knot.coors.x
                diff_y = knot.prev_knot.coors.y - knot.coors.y

                if int(abs(diff_x)) > 1 or int(abs(diff_y)) > 1:
                    knot.coors.x = (
                        knot.coors.x + int(diff_x / int(abs(diff_x)))
                        if diff_x != 0
                        else knot.coors.x
                    )
                    knot.coors.y = (
                        knot.coors.y + int(diff_y / int(abs(diff_y)))
                        if diff_y != 0
                        else knot.coors.y
                    )

                if knot.history_coors.get(f"{knot.coors.x}, {knot.coors.y}"):
                    knot.history_coors[f"{knot.coors.x}, {knot.coors.y}"] += 1
                else:
                    knot.history_coors[f"{knot.coors.x}, {knot.coors.y}"] = 1

    print(f"Rope visit at least once {len(knots[-1:][0].history_coors)} positions")
