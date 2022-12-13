import math
import re
from typing import Callable


class Monkey:
    def __init__(self, items: [int], operator: str, argument: str,
                 divisible_test: int, true_monkey: int, false_monkey: int):
        self.items = items
        self.operator = operator
        self.argument = argument
        self.divisible_test = divisible_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.count = 0

    def __repr__(self):
        return f"Items: {self.items}, count = {self.count}"


def parse(filename: str):
    monkeys: [Monkey] = []

    with open(filename) as file:
        monkeys_input = file.read().split("\n\n")

    for lines in monkeys_input:
        regex = re.search(r"Monkey \d+:\s+Starting items: ([\d ,]+)\s+"
                          r"Operation: new = old ([*+]) (\d+|old)\s+"
                          r"Test: divisible by (\d+)\s+"
                          r"If true: throw to monkey (\d+)+\s+"
                          r"If false: throw to monkey (\d+)", lines)
        items = [int(x) for x in regex.group(1).split(", ")]
        operator = regex.group(2)
        argument = regex.group(3)
        divisible_test = int(regex.group(4))
        true_monkey = int(regex.group(5))
        false_monkey = int(regex.group(6))

        monkeys.append(Monkey(items, operator, argument, divisible_test, true_monkey, false_monkey))

    return monkeys


def evaluate(old: int, operator: str, argument: str):
    if argument == "old":
        argument = old
    else:
        argument = int(argument)

    if operator == "*":
        return old * argument
    elif operator == "+":
        return old + argument


def run(monkeys: [Monkey]):
    modulo = math.prod({monkey.divisible_test for monkey in monkeys})

    for r in range(10000):

        for j, monkey in enumerate(monkeys):
            # print(f"Monkey {j}")
            items = monkey.items
            monkey.items = []
            for item in items:
                # print(f"\tMonkey inspects an item with a worry level of {item}.")
                # Apply operation
                item = evaluate(item, monkey.operator, monkey.argument)
                # print(f"\t\tWorry level changes to {item}")

                # Apply modulo of all divisible tests to item
                item = item % modulo
                # print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {item}")

                # Check to which monkey it gets thrown
                # print(f"\t\tItem with worry level {item} is thrown to monkey ", end='')
                if item % monkey.divisible_test == 0:
                    monkeys[monkey.true_monkey].items.append(item)
                    # print(monkey.true_monkey)
                else:
                    monkeys[monkey.false_monkey].items.append(item)
                    # print(monkey.false_monkey)
                # Increase inspection counter of monkey
                monkey.count += 1

        print(f"Round {r + 1}:")
        # print(f"\t{monkeys}")

    print([f"Monkey {i}: {monkey.count}" for i, monkey in enumerate(monkeys)])

    sorted_counts = sorted([monkey.count for monkey in monkeys])
    result = sorted_counts[-1] * sorted_counts[-2]

    print(f"Monkey business: {result}")


def main():
    monkeys = parse("input/day11.txt")
    run(monkeys)


if __name__ == '__main__':
    main()
