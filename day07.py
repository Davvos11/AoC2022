from typing import Union


class Folder:
    def __init__(self, name: str, parent: 'Folder'):
        self.name = name
        self.children = dict()
        self.parent = parent
        self.size = -1

    def add_child(self, child: Union['Folder', 'File']):
        self.children[child.name] = child

    def get_size(self):
        # Calculate the size if it is not calculated yet
        if self.size == -1:
            self.size = 0
            for child in self.children.values():
                self.size += child.get_size()
        # Return the size
        return self.size


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


def build_tree(filename: str):
    # Assuming we always start with "/"
    root = Folder("/", None)
    current_directory = root

    with open(filename) as file:
        # Build a file tree
        for line in file:
            line = line.strip()
            if line[0] == "$":
                # Parse commands
                if line[2:4] == "cd":
                    name = line[5:]
                    if name == "/":
                        # Move back to root
                        current_directory = root
                    elif name == "..":
                        # Move up one directory
                        current_directory = current_directory.parent
                    else:
                        # Move into the specified directory
                        # (Assuming we always do a ls of the current folder before cd-ing into a child)
                        current_directory = current_directory.children[name]
                # (we can ignore "ls" since lines that don't start with "$" only happen as a result of ls)
            else:
                # Parse folder contents
                if line[0:3] == "dir":
                    folder = Folder(line[4:], current_directory)
                    current_directory.add_child(folder)
                else:
                    size, name = line.split(" ")
                    size = int(size)
                    file = File(name, size)
                    current_directory.add_child(file)

    return root


def traverse_tree(tree: Folder):
    result = 0

    for child in tree.children.values():
        if isinstance(child, Folder):
            size = child.get_size()
            if size <= 100000:
                print(f"{child.name} has size {size}")
                result += size
            result += traverse_tree(child)

    return result


def main():
    tree = build_tree("input/day07.txt")
    result = traverse_tree(tree)
    print(result)


if __name__ == '__main__':
    main()
