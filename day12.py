def parse(filename: str):
    heightmap = []
    start = (0, 0)
    end = (0, 0)
    zeroes = []

    with open(filename) as file:
        for i, line in enumerate(file):
            row = []
            for j, char in enumerate(line.strip()):
                value = ord(char) - 97
                if char == "S":
                    start = (i, j)
                    value = 0
                elif char == "E":
                    end = (i, j)
                    value = 25
                row.append(value)
                if value == 0:
                    zeroes.append((i, j))
            heightmap.append(row)

    return heightmap, start, end, zeroes


def bfs(heightmap: [[int]], start: (int, int), end: (int, int)):
    queue = []
    visited = set()
    lengths = dict()

    queue.append(start)
    lengths[start] = 0
    visited.add(start)

    while len(queue) != 0:
        location = queue.pop(0)
        value = heightmap[location[0]][location[1]]
        current_length = lengths[location]

        if location == end:
            return current_length

        for offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get next location
            next_x = location[0] + offset[0]
            next_y = location[1] + offset[1]

            if next_x < 0 or next_x > len(heightmap) - 1 or \
                    next_y < 0 or next_y > len(heightmap[0]) - 1:
                continue

            next_location = (next_x, next_y)
            next_value = heightmap[next_x][next_y]

            # If this location has not been visited before and
            # is reachable, add it to the queue
            if next_location not in visited and \
                    next_value - value <= 1:
                queue.append(next_location)
                visited.add(next_location)
                lengths[next_location] = current_length + 1


def main():
    heightmap, start, end, zeroes = parse("input/day12.txt")
    print(f"Part one: {bfs(heightmap, start, end)}")

    shortest = None
    for start_option in zeroes:
        length = bfs(heightmap, start_option, end)
        if shortest is None or length is not None and length < shortest:
            shortest = length
    print(f"Part two: {shortest}")


if __name__ == '__main__':
    main()
