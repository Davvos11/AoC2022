import re


def main(filename: str):
    total = 0

    with open(filename) as file:
        for line in file:
            points = 0

            regex = re.search(r"([ABC]) ([XYZ])", line.strip())
            you = to_rps(regex.group(2))
            opponent = to_rps(regex.group(1))

            if you == opponent:
                # Draw
                points += 3
            elif (you == "rock" and opponent == "scissors") or \
                    (you == "paper" and opponent == "rock") or \
                    (you == "scissors" and opponent == "paper"):
                # Win
                points += 6
            if you == "rock":
                points += 1
            if you == "paper":
                points += 2
            if you == "scissors":
                points += 3

            # print(points)
            total += points

    print(total)


def to_rps(unit: str) -> str:
    if unit == "A" or unit == "X":
        return "rock"
    if unit == "B" or unit == "Y":
        return "paper"
    if unit == "C" or unit == "Z":
        return "scissors"


if __name__ == '__main__':
    main("input/day02.txt")
