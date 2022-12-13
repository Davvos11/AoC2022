def main(filename: str):
    heightmap = []
    start = (0, 0)
    end = (0, 0)

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
            heightmap.append(row)

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
            print(current_length)
            return

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


if __name__ == '__main__':
    main("input/day12.txt")
