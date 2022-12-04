import re


def main(filename: str):
    total = 0

    with open(filename) as file:
        for line in file:
            points = 0

            regex = re.search(r"([ABC]) ([XYZ])", line.strip())
            strategy = to_ldw(regex.group(2))
            opponent = to_rps(regex.group(1))

            if strategy == "lose":
                if opponent == "rock":
                    you = "scissors"
                elif opponent == "paper":
                    you = "rock"
                elif opponent == "scissors":
                    you = "paper"
            elif strategy == "draw":
                you = opponent
                points += 3
            elif strategy == "win":
                if opponent == "rock":
                    you = "paper"
                elif opponent == "paper":
                    you = "scissors"
                elif opponent == "scissors":
                    you = "rock"
                points += 6

            if you == "rock":
                points += 1
            elif you == "paper":
                points += 2
            elif you == "scissors":
                points += 3

            # print(you, strategy, points)
            total += points

    print(total)


def to_rps(unit: str) -> str:
    if unit == "A" or unit == "X":
        return "rock"
    if unit == "B" or unit == "Y":
        return "paper"
    if unit == "C" or unit == "Z":
        return "scissors"


def to_ldw(unit: str) -> str:
    if unit == "X":
        return "lose"
    if unit == "Y":
        return "draw"
    if unit == "Z":
        return "win"


if __name__ == '__main__':
    main("input/day02.txt")
