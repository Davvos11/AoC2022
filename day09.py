def main(filename: str):
    head = [0, 0]
    tail = [0, 0]
    visited = set()

    print(f"\t\t Head: {head}, Tail: {tail}")

    with open(filename) as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            amount = int(line[2:])

            for i in range(amount):
                # Move head
                if direction == "R":
                    head[1] += 1
                elif direction == "L":
                    head[1] -= 1
                elif direction == "U":
                    head[0] += 1
                elif direction == "D":
                    head[0] -= 1

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

                print(f"{line}:\t Head: {head}, Tail: {tail}")
                # Save tail location
                visited.add(tuple(tail))

    print(visited)
    print(len(visited))


if __name__ == '__main__':
    main("input/day09.txt")
