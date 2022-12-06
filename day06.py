def main(filename: str):
    with open(filename) as file:
        data = file.read().strip()

    buffer = data[:4]
    count = 4

    for char in data[4:]:
        # Move the buffer
        buffer = buffer[1:] + char
        count += 1

        # Check if there are repeating characters
        if len(set(buffer)) == len(buffer):
            print(f"Found at {count}")
            break


if __name__ == '__main__':
    main("input/day06.txt")
