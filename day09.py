def main(filename: str):
    # List of nots (0 = H)
    knots = [[0, 0] for i in range(0, 10)]
    visited = set()

    print(f"\t\t {knots}")

    with open(filename) as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            amount = int(line[2:])

            for _ in range(amount):
                # Move head
                if direction == "R":
                    knots[0][1] += 1
                elif direction == "L":
                    knots[0][1] -= 1
                elif direction == "U":
                    knots[0][0] += 1
                elif direction == "D":
                    knots[0][0] -= 1

                for i in range(len(knots)-1):
                    # Head is the knot in front of the knot we are moving
                    head = knots[i]
                    # Tail is the knot that we are moving now
                    tail = knots[i+1]
                    move_tail(head, tail)

                print(f"{line}:\t {knots}")
                # Save tail location
                visited.add(tuple(knots[-1]))

    print(visited)
    print(len(visited))


def move_tail(head: [int], tail: [int]) -> ([int], [int]):
    # Move tail based on position of head
    if head[0] == tail[0]:  # If on same row
        if abs(head[1] - tail[1]) > 1:
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1] -= 1
    elif head[1] == tail[1]:  # If on same column
        if abs(head[0] - tail[0]) > 1:
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1
    else:  # If diagonally
        if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
            pass
        else:
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1] -= 1

    return head, tail


if __name__ == '__main__':
    main("input/day09.txt")
