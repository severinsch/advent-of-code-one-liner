def visualize_coords(coords: list[tuple[int, int]], symbol: str = 'X') -> None:
    output = ""
    print(f'{coords}')
    for row in range(16, -10, -1):
        output += f"\n{row:>3}: "
        for column in range(-11, 15, 1):
            output += (("s" if (column, row) == coords[0] else symbol) if (column, row) in coords else ".")
    output += "\n"
    print(output)


def task_1():
    return len(set(__import__("functools").reduce(lambda tail_coords_acc, head_coords: [(t_x, t_y) if all([abs((t_x := tail_coords_acc[0][0]) - (h_x := head_coords[0])) <= 1, abs((t_y := tail_coords_acc[0][1]) - (h_y := head_coords[1])) <= 1]) else (t_x + (__import__("math").ceil(val) if (val := abs(t_x - h_x) / (2 if t_x < h_x else -2)) > 0 else __import__("math").floor(val)), t_y + (__import__("math").ceil(val) if (val := abs(t_y - h_y) / (2 if t_y < h_y else -2)) > 0 else __import__("math").floor(val)))] + tail_coords_acc, __import__("functools").reduce(lambda head_coords_acc, step: head_coords_acc + list(__import__("itertools").accumulate(range(step[1]), lambda coords, _: (coords[0] + (1 if (direction := step[0]) == "R" else (-1 if direction == 'L' else 0)), coords[1] + (1 if direction == "U" else (-1 if direction == 'D' else 0))), initial=(head_coords_acc[-1]))), ((line.split()[0], int(line.split()[1])) for line in open('input.txt', 'r').read().splitlines()), [(0, 0)]), [(0, 0)])))


def task_1_prettier():
    return len(
        set(
            __import__("functools").reduce(  # accumulate coords of tail from list of head coords
                lambda tail_coords_acc, head_coords:
                    [
                        (t_x, t_y)
                        if
                        all(  # use all([a, b]) instead of a and b to avoid "and" short circuit to make sure t_y and h_y are bound
                            [abs((t_x := tail_coords_acc[0][0]) - (h_x := head_coords[0])) <= 1,
                             abs((t_y := tail_coords_acc[0][1]) - (h_y := head_coords[1])) <= 1]
                        )
                        else
                        (t_x + (__import__("math").ceil(val) if (val := abs(t_x - h_x) / (2 if t_x < h_x else -2)) > 0 else __import__("math").floor(val)),  # new x
                         t_y + (__import__("math").ceil(val) if (val := abs(t_y - h_y) / (2 if t_y < h_y else -2)) > 0 else __import__("math").floor(val)))  # new y
                    ] + tail_coords_acc,
                    __import__("functools").reduce(
                        lambda head_coords_acc, step:  # create list of head coords from list of movement instructions
                            head_coords_acc + list(
                                __import__("itertools").accumulate(
                                    range(step[1]),  # n steps
                                    lambda coords, _:
                                        (coords[0] + (1 if (direction := step[0]) == "R" else (-1 if direction == 'L' else 0)),
                                         coords[1] + (1 if direction == "U" else (-1 if direction == 'D' else 0))),
                                    initial=(head_coords_acc[-1])  # old coords
                                )
                            ),
                            ((line.split()[0], int(line.split()[1])) for line in open('input.txt', 'r').read().splitlines()),
                            [(0, 0)]
                    ),
                [(0, 0)]
            )
        )
    )


def task_2():
    return len(set(__import__("functools").reduce(lambda previous_coords, _: __import__("functools").reduce(lambda new_coords_acc, prev_coords: new_coords_acc + [(t_x, t_y) if all([abs((t_x := new_coords_acc[-1][0]) - (h_x := prev_coords[0])) <= 1, abs((t_y := new_coords_acc[-1][1]) - (h_y := prev_coords[1])) <= 1]) else (t_x + max(min((h_x - t_x), 1), -1), t_y + max(min((h_y - t_y), 1), -1))], previous_coords, [(0, 0)]), range(9), __import__("functools").reduce(lambda head_coords_acc, step: head_coords_acc + list(__import__("itertools").accumulate(range(step[1]), lambda coords, _: (coords[0] + (1 if (direction := step[0]) == "R" else (-1 if direction == 'L' else 0)), coords[1] + (1 if direction == "U" else (-1 if direction == 'D' else 0))), initial=(head_coords_acc[-1]))), ((line.split()[0], int(line.split()[1])) for line in open('input.txt', 'r').read().splitlines()), [(0, 0)]))))


def task_2_prettier():
    return len(
        set(
            __import__("functools").reduce(
                lambda previous_coords, _: __import__("functools").reduce(  # accumulate coords of tail from list of head coords
                    lambda new_coords_acc, prev_coords:
                    new_coords_acc + [
                        (t_x, t_y)
                        if
                        all(  # use all([a, b]) instead of a and b to avoid "and" short circuit to make sure t_y and h_y are bound
                            [abs((t_x := new_coords_acc[-1][0]) - (h_x := prev_coords[0])) <= 1,
                             abs((t_y := new_coords_acc[-1][1]) - (h_y := prev_coords[1])) <= 1]
                        )
                        else
                        (t_x + max(min((h_x - t_x), 1), -1),  # new x
                         t_y + max(min((h_y - t_y), 1), -1))  # new y
                    ],
                    previous_coords,
                    [(0, 0)]
                ),
                range(9),
                __import__("functools").reduce(  # get coords of head
                    lambda head_coords_acc, step:  # create list of head coords from list of movement instructions
                    head_coords_acc + list(
                        __import__("itertools").accumulate(
                            range(step[1]),  # n steps
                            lambda coords, _:
                            (coords[0] + (1 if (direction := step[0]) == "R" else (-1 if direction == 'L' else 0)),
                             coords[1] + (1 if direction == "U" else (-1 if direction == 'D' else 0))),
                            initial=(head_coords_acc[-1])  # old coords
                        )
                    ),
                    ((line.split()[0], int(line.split()[1])) for line in open('input.txt', 'r').read().splitlines()),
                    [(0, 0)]
                )
            )
        )
    )


def get_next_coords(previous_coords: list[tuple[int, int]], n: int) -> list[tuple[int, int]]:
    visualize_coords(previous_coords, symbol=str(n))
    return __import__("functools").reduce(  # accumulate coords of tail from list of head coords
        lambda new_coords_acc, prev_coords:
        new_coords_acc + [
            (t_x, t_y)
            if
            all(  # use all([a, b]) instead of a and b to avoid "and" short circuit to make sure t_y and h_y are bound
                [abs((t_x := new_coords_acc[-1][0]) - (h_x := prev_coords[0])) <= 1,
                 abs((t_y := new_coords_acc[-1][1]) - (h_y := prev_coords[1])) <= 1]
            )
            else
            (t_x + max(min((h_x - t_x), 1), -1),  # new x
             t_y + max(min((h_y - t_y), 1), -1))  # new y
        ],
        previous_coords,
        [(0, 0)]
    )


# x, y
# U -> y+
# D -> y-
# R -> x+
# L -> x-
def get_head_coords(old_coords: tuple[int, int], direction: str, amount: int) -> list[tuple[int, int]]:
    res = list(__import__("itertools").accumulate(
        range(amount),
        lambda coords, _:
        (coords[0] + (1 if direction == "R" else (-1 if direction == 'L' else 0)),
         coords[1] + (1 if direction == "U" else (-1 if direction == 'D' else 0))),
        initial=old_coords))
    return res


def get_tail_coords(old_tail_coords: tuple[int, int], head_coords: tuple[int, int]) -> tuple[int, int]:
    t_x, t_y = old_tail_coords
    h_x, h_y = head_coords
    # res = (t_x, (t_y + (1 if t_y < t_x else -1)) if t_x == h_x else ()
    res_x = t_x + (__import__("math").ceil(val) if (val := abs(t_x - h_x) / (2 if t_x < h_x else -2)) > 0 else __import__("math").floor(val))
    res_y = t_y + (__import__("math").ceil(val) if (val := abs(t_y - h_y) / (2 if t_y < h_y else -2)) > 0 else __import__("math").floor(val))
    res = old_tail_coords if abs(t_x - h_x) <= 1 and abs(t_y - h_y) <= 1 else (res_x, res_y)
    print(f'{old_tail_coords=}, {head_coords=}, {res=}')
    return res


assert task_1() == task_1_prettier()
print(task_1())

assert task_2() == task_2_prettier()
print(task_2())
