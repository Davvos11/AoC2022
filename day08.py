def part01(filename: str):
    # Trees will be a matrix of lists (height (int), visible (bool or None))
    trees = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            trees.append([[int(char), None] for char in line])

    visible = 0

    # Loop through the trees in 4 directions
    for i in range(4):
        # Rotate the matrix
        trees = list(zip(*trees[::-1]))

        for row in trees:
            previous = -1
            for tree in row:
                # Set visible to True or False only if it has not been set before
                # or to True if it was False before
                # (never set it to False if it was already True)
                if not tree[1]:
                    tree[1] = tree[0] > previous

                # Update the highest value of this row
                if tree[0] > previous:
                    previous = tree[0]

                # On the last iteration, count
                if i == 3 and tree[1]:
                    visible += 1
        pass
    print(visible)


def part02(filename: str):
    trees = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            trees.append([int(char) for char in line])

    best_score = -1

    for i in range(len(trees)):
        for j in range(len(trees[i])):
            current_tree = trees[i][j]
            score = 1

            # Loop through the 4 possible directions
            for d in range(4):
                count = 1

                while True:
                    if d == 0:
                        if j + count >= len(trees[i]):
                            break
                        next_tree = trees[i][j + count]
                    elif d == 1:
                        if j - count < 0:
                            break
                        next_tree = trees[i][j - count]
                    elif d == 2:
                        if i + count >= len(trees):
                            break
                        next_tree = trees[i + count][j]
                    elif d == 3:
                        if i - count < 0:
                            break
                        next_tree = trees[i - count][j]

                    count += 1

                    if next_tree >= current_tree:
                        break

                score *= (count - 1)

            if score > best_score:
                best_score = score

    print(best_score)


if __name__ == '__main__':
    part01("input/day08.txt")
    part02("input/day08.txt")
