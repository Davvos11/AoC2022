def main(filename: str):
    with open(filename) as file:
        program_counter = 0
        crt = ""
        x = 1

        for line in file:
            instruction = line[:4]

            program_counter += 1

            crt += crt_char(x, program_counter)

            if instruction == "addx":
                program_counter += 1
                crt += crt_char(x, program_counter)
                x += int(line[5:])

    print(crt)


def crt_char(x: int, program_counter: int) -> str:
    program_counter = program_counter % 40
    if program_counter - 1 in {x - 1, x, x + 1}:
        result = "#"
    else:
        result = " "

    if program_counter == 0:
        result += "\n"

    return result


if __name__ == '__main__':
    main("input/day10.txt")
