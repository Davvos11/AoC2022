def main(filename: str):
    with open(filename) as file:
        program_counter = 1
        x = 1
        results = []

        for line in file:
            instruction = line[:4]

            program_counter += 1

            if program_counter % 40 == 20:
                results.append(x * program_counter)

            if instruction == "addx":
                program_counter += 1
                x += int(line[5:])

                if program_counter % 40 == 20:
                    results.append(x * program_counter)

    print(sum(results))


if __name__ == '__main__':
    main("input/day10.txt")
