import re


def main(filename: str):
    stacks = {i: [] for i in range(1, 10)}
    instructions = []

    with open(filename) as file:
        for line in file:
            if line.strip().startswith('['):
                # Split on spaces and get second character (i.e. ignore the [ and ])
                # (or make None if empty)
                crates = [line[i] if line[i] != ' ' else None for i in range(1, len(line), 4)]
                for i, crate in enumerate(crates):
                    # (bottom crates will be at the end of the list)
                    if crate is not None:
                        stacks[i + 1].append(crate)
            elif line.startswith('m'):
                regex = re.search(r"move (\d+) from (\d+) to (\d+)", line)
                instructions.append({'amount': int(regex.group(1)), 'from': int(regex.group(2)), 'to': int(regex.group(3))})

        for ins in instructions:
            # Get crates that need  to be moved
            to_move = stacks[ins['from']][:ins['amount']]
            # Remove crates from original stack
            del stacks[ins['from']][:ins['amount']]
            # Put crates on new stack (in reverse order)
            to_move.reverse()
            stacks[ins['to']] = to_move + stacks[ins['to']]

        result = ""
        for stack in stacks.values():
            # Get top crate
            if len(stack) > 0:
                result += stack[0]
        print(result)


if __name__ == '__main__':
    main("input/day05.txt")
