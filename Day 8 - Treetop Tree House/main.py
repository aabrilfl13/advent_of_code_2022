DIR_PATH = "Day 8 - Treetop Tree House"


def visible_trees(trees: list[int]):
    visible_trees = (len(trees[0]) * 2 + (len(trees)) * 2) - 4  # 4 corners
    for i in range(1, len(trees) - 1):
        row = trees[i]
        for j in range(1, len(row) - 1):
            tree = trees[i][j]

            right = row[:j]
            left = row[j + 1 :]

            col = []
            for k in range(0, len(trees)):
                col.append(trees[k][j])

            up = col[:i]
            down = col[i + 1 :]

            if (
                tree > max(right)
                or tree > max(left)
                or tree > max(up)
                or tree > max(down)
            ):
                visible_trees += 1

    print(f"There're {visible_trees} visible trees")


if __name__ == "__main__":
    with open(f"./{DIR_PATH}/input", "r") as fptr:
        trees_matrix = fptr.readlines()

        rows = len(trees_matrix)
        trees_in_row = len(trees_matrix[0])

        trees = []

        # Init Matrix
        for i, row_of_trees in enumerate(trees_matrix):
            row = []
            for j, tree in enumerate(row_of_trees.strip()):
                row.append(int(tree))
            trees.append(row)

        # PART 1
        # visible_trees(trees)

        # PART 2
        scores = {}
        for i in range(1, len(trees) - 1):
            row = trees[i]
            for j in range(1, len(row) - 1):
                if trees[i][j] == 0:
                    continue

                tree = trees[i][j]
                score = 0

                col = []
                for k in range(0, len(trees)):
                    col.append(trees[k][j])

                right = row[:j][::-1]
                left = row[j + 1 :]
                up = col[:i][::-1]
                down = col[i + 1 :]

                view_r = 0
                for tree_view in right:
                    view_r += 1
                    if tree <= tree_view:
                        break

                view_l = 0
                for tree_view in left:
                    view_l += 1
                    if tree <= tree_view:
                        break

                view_u = 0
                for tree_view in up:
                    view_u += 1
                    if tree <= tree_view:
                        break

                view_d = 0
                for tree_view in down:
                    view_d += 1
                    if tree <= tree_view:
                        break

                score = view_r * view_l * view_d * view_u
                scores[score] = f"{tree} [{i}][{j}]"

        print(
            f"There best spot has obtain {max(scores)} points. - {scores[max(scores)]}"
        )
