import functools
import itertools
import operator


def is_visible_(height: int, row: int, column: int, forest: list[list[tuple[int, int, int]]]) -> bool:
    column_vals = [tree_row[column][0] < height for idx, tree_row in enumerate(forest)]
    row_vals = [tree[0] < height for idx, tree in enumerate(forest[row])]

    return row == 0 or row == len(forest)-1 or column == 0 or column == len(forest[0])-1 or all(column_vals[:row]) or all(column_vals[row+1:]) or all(row_vals[:column]) or all(row_vals[column+1:])


def task_1():
    return sum((lambda forest: [row == 0 or row == len(forest)-1 or column == 0 or column == len(forest[0])-1 or all((column_vals := [tree_row[column][0] < height for idx, tree_row in enumerate(forest)])[:row]) or all(column_vals[row+1:]) or all((row_vals := [tree[0] < height for idx, tree in enumerate(forest[row])])[:column]) or all(row_vals[column+1:]) for height, row, column in __import__("itertools").chain.from_iterable(forest)])([[(int(c), row, column) for column, c in enumerate(s)] for row, s in enumerate(open('input.txt', 'r').read().splitlines())]))


def task_1_prettier():
    return sum(
        (lambda forest:
         [row == 0 or row == len(forest)-1 or column == 0 or column == len(forest[0])-1 or  # if tree is at the edge
          all((column_vals := [tree_row[column][0] < height for idx, tree_row in enumerate(forest)])[:row]) or
          all(column_vals[row+1:]) or
          all((row_vals := [tree[0] < height for idx, tree in enumerate(forest[row])])[:column]) or
          all(row_vals[column+1:])
          for height, row, column
          in __import__("itertools").chain.from_iterable(forest)]
         )(
            [[(int(c), row, column) for column, c in enumerate(s)] for row, s in enumerate(open('input.txt', 'r').read().splitlines())]
          )
        )


def get_scenic_score(height: int, row: int, column: int, forest: list[list[tuple[int, int, int]]]):
    cur_column = [tree_row[column] for tree_row in forest]
    cur_row = forest[row]
    up = list(reversed(cur_column[:row]))
    down = cur_column[row+1:]

    left = list(reversed(cur_row[:column]))
    right = cur_row[column+1:]
    views = [up, down, left, right]
    temp = [(len(list(itertools.takewhile(lambda t: t[0] < height, view))), len(view)) for view in views]
    scores = [viewing_dist + (viewing_dist != forest_len) for viewing_dist, forest_len in temp]
    return functools.reduce(operator.mul, scores)


def task_2() -> int:
    return (lambda forest: max([(lambda cur_column, cur_row: functools.reduce(operator.mul, [viewing_dist + (viewing_dist != forest_len) for viewing_dist, forest_len in [(len(list(itertools.takewhile(lambda t: t[0] < height, view))), len(view)) for view in (list(reversed(cur_column[:row])), cur_column[row+1:], list(reversed(cur_row[:column])), cur_row[column+1:])]]))([tree_row[column] for tree_row in forest], forest[row]) for height, row, column in __import__("itertools").chain.from_iterable(forest)]))([[(int(c), row, column) for column, c in enumerate(s)] for row, s in enumerate(open('input.txt', 'r').read().splitlines())])


def task_2_prettier() -> int:
    return (
        lambda forest:
            max(
                [
                    (lambda cur_column, cur_row:
                     functools.reduce(
                         operator.mul,  # calc total score
                         [viewing_dist + (viewing_dist != forest_len)  # add one for the tree blocking the view if not seeing all trees
                          for viewing_dist, forest_len
                          in [
                              (len(list(itertools.takewhile(lambda t: t[0] < height, view))), len(view))  # get all the trees that can be seen (minus the one blocking view)
                              for view
                              in (list(reversed(cur_column[:row])),  # view up
                                  cur_column[row+1:],  # view down
                                  list(reversed(cur_row[:column])),  # view left
                                  cur_row[column+1:])  # view right
                          ]]
                     )
                     )([tree_row[column] for tree_row in forest], forest[row])  # current_column, current_row
                    for height, row, column
                    in __import__("itertools").chain.from_iterable(forest)
                ]
            )
    )(
        [[(int(c), row, column) for column, c in enumerate(s)] for row, s in enumerate(open('input.txt', 'r').read().splitlines())]  # parse forest
    )


assert task_1() == task_1_prettier()
print(task_1())
assert task_2() == task_2_prettier()
print(task_2())
