def main(filename: str):
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


if __name__ == '__main__':
    main("input/day03.txt")
