LEN = 14


def main(filename: str):
    with open(filename) as file:
        data = file.read().strip()

    buffer = data[:LEN]
    count = LEN

    for char in data[LEN:]:
        # Move the buffer
        buffer = buffer[1:] + char
        count += 1

        # Check if there are repeating characters
        if len(set(buffer)) == len(buffer):
            print(f"Found at {count}")
            break


if __name__ == '__main__':
    main("input/day06.txt")
