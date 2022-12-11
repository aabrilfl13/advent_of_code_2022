from __future__ import annotations

from dataclasses import dataclass, field


DIR_PATH = __file__[:-8]


@dataclass
class Item:
    worry_level: int


@dataclass
class Monkey:
    id: int
    name: str
    operation: str = ""
    inspections: int = 0
    items: list = field(default_factory=list)

    divisor: int | None = None
    mcm: int | None = None
    test_true_monkey: Monkey | None = None
    test_false_monkey: Monkey | None = None

    def test(self, value: int) -> None:
        monkey_receiver: Monkey = (
            self.test_true_monkey
            if value % self.divisor == 0
            else self.test_false_monkey
        )
        item = self.pop_item()
        monkey_receiver.add_item(item)

    def calculate_operation(self, old):
        self.inspections += 1
        old = int(old)
        return eval(self.operation)

    def add_item(self, item: Item):
        self.items.append(item)

    def pop_item(self):
        return self.items.pop(0)


def print_monkeys(monkeys: dict):
    for monkey in monkeys.values():
        print(monkey.id, "-", monkey.inspections)


if __name__ == "__main__":
    monkeys: dict(int, Monkey) = {}

    with open(f"{DIR_PATH}/input", "r") as fptr:
        saved_test_for_later: dict(int, dict) = {}

        while True:
            line = fptr.readline()
            if not line:
                break
            line = line.strip().split(":")

            if "Monkey" in line[0]:
                monkey = Monkey(id=int(line[0][-1:]), name=line[0])
                monkeys.update({monkey.id: monkey})
            elif "Starting items" in line[0]:
                items = line[1].strip().split(", ")
                for item_worry_level in items:
                    monkey.add_item(item=Item(worry_level=item_worry_level))
            elif "Operation" in line[0]:
                operation = line[1].split(" = ")[-1:][0]
                monkey.operation = operation
            elif "Test" in line[0]:
                saved_test_for_later[monkey.id] = {
                    "divisor": int(line[1].strip().split()[-1:][0]),
                    1: fptr.readline().strip(),
                    0: fptr.readline().strip(),
                }

        # update test conditios once we have all monkeys created
        for monkey_id, conditions in saved_test_for_later.items():
            monkey = monkeys[monkey_id]
            monkey.divisor = conditions["divisor"]

            for i in reversed(range(0, 2)):
                condition_test = conditions[i]
                monkey_to_throw = int(condition_test.strip().split()[-1:][0])
                if i:
                    monkey.test_true_monkey = monkeys.get(monkey_to_throw)
                else:
                    monkey.test_false_monkey = monkeys.get(monkey_to_throw)

        mcm = 1
        for monkey in monkeys.values():
            mcm *= monkey.divisor

        for monkey in monkeys.values():
            monkey.mcm = mcm

    print("All monkeys are set. Let's start the problem...")

    ROUNDS = 10000
    for i in range(ROUNDS):  # rounds
        for monkey in monkeys.values():
            monkey: Monkey
            if not monkey.items:
                continue

            items = monkey.items.copy()
            for item in items:
                # multiply worry level
                item.worry_level = monkey.calculate_operation(item.worry_level)
                if item.worry_level > monkey.mcm:
                    item.worry_level %= monkey.mcm

                # divide worry level  # PART 1
                # item.worry_level //= 3

                # test
                # monkey.test(item.worry_level)  # PART 1
                monkey.test(item.worry_level)  # PART 2

        # if i % 1000 == 0:
        #     print(f"#########ROUNDS: {i} ############")
        #     print_monkeys(monkeys)

    ordered_dict = {
        k: v
        for k, v in sorted(
            monkeys.items(), key=lambda x: x[1].inspections, reverse=True
        )
    }
    monkey_ids_ordered = []
    for monkey in ordered_dict.values():
        monkey_ids_ordered.append(monkey.id)

    print_monkeys(monkeys)

    print(
        "Monkey Bussisness value:",
        ordered_dict[monkey_ids_ordered[0]].inspections
        * ordered_dict[monkey_ids_ordered[1]].inspections,
    )
