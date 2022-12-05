import re


def main(filename: str):
    count = 0

    with open(filename) as file:
        for line in file:
            regex = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line.strip())

            a, b, x, y = regex.group(1), regex.group(2), regex.group(3), regex.group(4)
            a, b, x, y = int(a), int(b), int(x), int(y)

            if (b >= x) and (y >= a):
                print(line.strip())
                count += 1

        print(count)


if __name__ == '__main__':
    main("input/day04.txt")
