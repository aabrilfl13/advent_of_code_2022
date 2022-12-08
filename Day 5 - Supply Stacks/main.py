from typing import List


class Stack:
    def __init__(self):
        self.items: List[str] = []

    def push(self, x) -> None:
        self.items.append(x)

    def pop(self) -> str:
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("Pile")

    def size(self) -> int:
        return len(self.items)

    def top(self) -> str:
        return self.items[-1]


def init_stacks(lines_of_stack: list) -> List[Stack]:
    stacks: List[Stack] = []

    los = lines_of_stack[:-1]
    n_stacks = int(lines_of_stack[-1:][0].strip()[-1:])

    pos = 0
    for _ in range(0, n_stacks):
        stack = Stack()
        for line in reversed(los):
            line = line[pos : pos + 3].strip()

            if not line:
                break
            stack.push(line)

        pos += 4
        stacks.append(stack)

    return stacks


def init_movements(lines_of_mvnt: list) -> List[dict]:
    mvnts = []
    for line in lines_of_mvnt:
        l = line.strip().split(" ")
        mvnts.append({"move": int(l[1]), "from": int(l[3]), "to": int(l[5])})

    return mvnts


def print_stacks(stacks, top: bool = False):
    for i, stack in enumerate(stacks, start=1):
        if top:
            print(f"{stack.items[-1:][0]}", end=" ")
        else:
            print(f"{i} - {stack.items}")
    print("--------------------------------")


def rearrangement(stacks: List[Stack], movements: dict) -> List[Stack]:
    for movement in movements:
        for i in range(movement["move"]):
            crate = stacks[movement["from"] - 1].pop()
            stacks[movement["to"] - 1].push(crate)

        # print_stacks(stacks)

    return stacks


def rearrangement_9001(stacks: List[Stack], movements: dict) -> List[Stack]:
    """ 
        To complete this challenge and not remove the stack implements
        we just take the list of items that the stack have.
    """
    for movement in movements:
        move = movement["move"]
        crates = stacks[movement["from"] - 1].items[-move:]
        del stacks[movement["from"] - 1].items[-move:]  # we remove the moved items

        stacks[movement["to"] - 1].items += crates

        # print_stacks(stacks)

    return stacks


if __name__ == "__main__":
    with open("./Day 5 - Supply Stacks/input", "r") as fptr:
        lines = fptr.readlines()

        for i, line in enumerate(lines, start=1):
            if "\n" in line[:3]:
                break

        stacks = init_stacks(lines_of_stack=lines[:9])
        movements = init_movements(lines_of_mvnt=lines[10:])

        stacks = rearrangement_9001(stacks, movements)

        print_stacks(stacks, top=True)
