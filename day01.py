def main(filename: str):
    maximum = -1
    current = 0

    with open(filename) as file:
        for i, line in enumerate(file):
            line = line.strip()
            if line == "":
                if current > maximum:
                    maximum = current
                current = 0
            else:
                current += int(line)

    print(maximum)


if __name__ == '__main__':
    main("input/day01-1.txt")
