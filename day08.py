def main(filename: str):
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


if __name__ == '__main__':
    main("input/day08.txt")
