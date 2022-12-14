import ast
from enum import Enum
from functools import cmp_to_key


class Comparison(Enum):
    WRONG = 1
    CORRECT = 2
    EQUAL = 3


def main(filename: str):
    packets = []

    with open(filename) as file:
        pairs = file.read().split("\n\n")

    result = 0

    for i, pair in enumerate(pairs):
        pair1, pair2 = pair.strip().split("\n")
        pair1 = ast.literal_eval(pair1)
        pair2 = ast.literal_eval(pair2)

        # Save (for part 2)
        packets.append(pair1)
        packets.append(pair2)

        comp = compare(pair1, pair2)
        if comp == Comparison.CORRECT:
            result += i + 1

    print(f"Part 1: {result}")

    # Add divider packets
    packets.append([[2]])
    packets.append([[6]])
    # Sort using our comparison
    packets = sorted(packets, key=cmp_to_key(compare_function))
    # Get indices of divider packets
    divider1 = packets.index([[2]]) + 1
    divider2 = packets.index([[6]]) + 1

    print(f"Part 2: {divider1 * divider2}")


def compare(entry1: int | list, entry2: int | list) -> Comparison:
    islist1 = isinstance(entry1, list)
    islist2 = isinstance(entry2, list)

    if not islist1 and not islist2:
        # Both are integers, check if 1 < 2
        if entry1 < entry2:
            return Comparison.CORRECT
        elif entry1 == entry2:
            return Comparison.EQUAL
        else:
            return Comparison.WRONG
    else:
        # Convert to lists
        list1 = entry1 if islist1 else [entry1]
        list2 = entry2 if islist2 else [entry2]

        # Both are now lists
        for i in range(len(list1)):
            if i >= len(list2):
                # If the right list runs out of items first, the inputs are not in the right order.
                return Comparison.WRONG
            # check if 1 <= 2 (recursion)
            comparison = compare(list1[i], list2[i])
            # If equal, continue. Otherwise, return the result (greater or smaller)
            if comparison != Comparison.EQUAL:
                return comparison
        if len(list1) == len(list2):
            # If the lists are the same length and no comparison makes a decision about the order,
            # continue checking the next part of the input.
            return Comparison.EQUAL
        # If the left list runs out of items first, the inputs are in the right order.
        return Comparison.CORRECT


def compare_function(entry1, entry2) -> int:
    comparison = compare(entry1, entry2)
    if comparison == Comparison.CORRECT:
        return -1
    elif comparison == Comparison.WRONG:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main("input/day13.txt")
