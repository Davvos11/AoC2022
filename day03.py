def part1(filename: str):
    result = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            m = len(line) // 2
            compartment1 = set(line[:m])
            compartment2 = set(line[m:])

            common = compartment1.intersection(compartment2)
            common = common.pop()  # should only have one item

            v = ord(common)
            prio = v - 96 if v >= 97 else v - 64 + 26
            # print(common, prio)
            result += prio

    print(result)


def part2(filename: str):
    result = 0

    with open(filename) as file:
        lines = file.readlines()
    for i in range(0, len(lines) - 2, 3):
        bag1 = set(lines[i].strip())
        bag2 = set(lines[i + 1].strip())
        bag3 = set(lines[i + 2].strip())

        common = bag1 & bag2 & bag3
        common = common.pop()

        v = ord(common)
        prio = v - 96 if v >= 97 else v - 64 + 26
        result += prio

    print(result)


if __name__ == '__main__':
    # part1("input/day03.txt")
    part2("input/day03.txt")
