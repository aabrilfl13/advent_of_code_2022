from typing import Any, Tuple
from dataclasses import dataclass, field

DIR_PATH = "Day 7 - No Space Left On Device"


@dataclass
class File:
    name: str
    size: int

    def __str__(self) -> str:
        return f"{self.name} (file, size={self.size})"


@dataclass
class Dir:
    name: str
    parent: Any | None = None
    items: dict[str, Any | File] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"{self.name} (dir, size={self.size})"

    @property
    def size(self):
        size = 0
        for item in self.items:
            size += item.size
        return size

    def find_dir(self, dir_name: str):
        for item in self.items:
            if isinstance(item, Dir) and item.name == dir_name:
                return item
        raise Exception("Dir not found")

    # def add_item(self, item: list[Any, File]):
    #     self.items.append(item)


def next_command(fptr) -> list:
    return fptr.readline().strip().split()


def print_tree(
    directory: Dir, level: int = 0, total_size: int = 0, only_dirs: bool = False
) -> int | None:
    tabs = "\t" * level
    print(f"{tabs}- {directory}")

    if isinstance(directory, Dir):
        for item in directory.items:
            if isinstance(item, Dir):
                if item.size <= 100000:
                    total_size += item.size
                total_size = print_tree(
                    directory=item,
                    level=level + 1,
                    total_size=total_size,
                    only_dirs=only_dirs,
                )
            elif not only_dirs:
                total_size = print_tree(
                    directory=item, level=level + 1, total_size=total_size
                )
    return total_size


def find_dir_to_delete(
    directory: Dir,
    level: int = 0,
    unused_size: int = 0,
    needed_size: int = 0,
    dir_to_delete: Dir = None,
) -> int | None:
    if isinstance(directory, Dir):
        for item in directory.items:
            if isinstance(item, Dir):
                if (
                    unused_size + item.size >= needed_size
                    and item.size < dir_to_delete.size
                ):
                    dir_to_delete = item
                dir_to_delete = find_dir_to_delete(
                    directory=item,
                    level=level + 1,
                    needed_size=needed_size,
                    unused_size=unused_size,
                    dir_to_delete=dir_to_delete,
                )
    return dir_to_delete


def read_ls(directory: Dir, actions) -> Tuple[list, str]:
    items = []
    while command := next_command(actions):
        if command[0] == "$":
            return items, command

        if command[0] == "dir":
            item = Dir(name=command[1], parent=directory)
        if command[0].isdigit():
            item = File(name=command[1], size=int(command[0]))

        items.append(item)
    return items, None


if __name__ == "__main__":
    with open(f"./{DIR_PATH}/input", "r") as fptr:
        command = fptr.readline()

        root = Dir("/")  # firs iteration is creating the root dir
        root.parent = root

        current_dir = root
        command = next_command(fptr)
        while command:
            if command[0] == "$":  # command
                match command[1]:
                    case "ls":
                        items, command = read_ls(current_dir, actions=fptr)
                        current_dir.items = items
                    case "cd":
                        if command[2] == "..":
                            current_dir = current_dir.parent
                        else:
                            current_dir = current_dir.find_dir(dir_name=command[2])
                        command = next_command(fptr)

    # PART 1
    # print(print_tree(root))

    # PART 2
    DISK_SIZE = 70000000
    UPDATE_SIZE = 30000000
    used_size = root.size
    unused_size = DISK_SIZE - used_size
    needed_size = UPDATE_SIZE - unused_size

    print(
        find_dir_to_delete(
            root, unused_size=unused_size, needed_size=UPDATE_SIZE, dir_to_delete=root
        )
    )
