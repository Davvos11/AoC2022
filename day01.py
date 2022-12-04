def main(filename: str):
    totals = []
    current = 0

    with open(filename) as file:
        for i, line in enumerate(file):
            line = line.strip()
            if line == "":
                totals.append(current)
                current = 0
            else:
                current += int(line)

    print(sum(sorted(totals, reverse=True)[:3]))


if __name__ == '__main__':
    main("input/day01-1.txt")
