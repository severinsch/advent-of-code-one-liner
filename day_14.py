def visualize_board(board: dict[tuple[int, int], str]):
    output = ""
    for y in range(200):
        for x in range(400, 600):
            point = board.get((x, y))
            output += point if point else "."
        output += "\n"
    return output


def parse_input():
    get_line = lambda start_x, start_y, end_x, end_y: [
        (x, y) for x in range(start_x, end_x + (1 if start_x <= end_x else -1), 1 if start_x <= end_x else -1) for y in
        range(start_y, end_y + (1 if start_y <= end_y else -1), 1 if start_y <= end_y else -1)
    ]

    return list(__import__("itertools").chain.from_iterable(
           [get_line(start_x, start_y, end_x, end_y) for ((start_x, start_y), (end_x, end_y)) in
            __import__("itertools").chain.from_iterable([zip(line, line[1:]) for line in [
                [(int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in pairs] for pairs in
                [line.split(" ->") for line in open("input.txt", "r").read().splitlines()]]])]))


def simulate_sand(board: dict[tuple[int, int], str | None], sand_no: int) -> tuple[dict[tuple[int, int], str | None], int, bool]:
    until = lambda pred, f, x: x if pred(x) else until(pred, f, f(x))
    max_y = 9
    final_point = until(
        lambda p: (p[1] < max_y and all(
            (
                board[(p[0], p[1] + 1)],
                board[(p[0] - 1, p[1] + 1)],
                board[(p[0] + 1, p[1] + 1)],
            )) or p[1] >= max_y
                   ),
        lambda p: next(
            (move for move in ((p[0], p[1] + 1), (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1)) if not board.get(move)),
            p),
        (500, 0),
    )
    print(f'{final_point=}')
    return (board, sand_no + 1, True) if final_point[1] >= max_y else (board | {final_point: "o"}, sand_no + 1, False)


def task_1():
    return (until := lambda pred, f, x: x if pred(*x) else until(pred, f, f(*x)))(
        lambda board, sand_no, finished, max_y: finished,  # check if finished
        lambda board, sand_no, finished, max_y:
        (board, sand_no, True, max_y)  # if final point of falling sand is below lowest stone, we're finished
        if (final_point := until(
            lambda x, y: (y < max_y and all(  # check if sand is at rest or in void
                (
                    board[(x, y + 1)],
                    board[(x - 1, y + 1)],
                    board[(x + 1, y + 1)],
                )) or y >= max_y
                          ),
            lambda x, y: next(  # get next move for sand
                (move for move in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)) if not board.get(move)),
                (x, y)
            ),
            (500, 0),
        ))[1] >= max_y
        else (board | {final_point: "o"}, sand_no + 1, False, max_y),  # update board if we're not finished
        (
            initial_board :=
            (
                    {(x, y): None
                     for x in range(400, 600) for y in range(200)
                     } | {stone: "#"
                          for stone in
                          __import__("itertools").chain.from_iterable(
                              [
                                  [
                                      (x, y) for x in range(start_x, end_x + (1 if start_x <= end_x else -1),
                                                            1 if start_x <= end_x else -1) for y in
                                      range(start_y, end_y + (1 if start_y <= end_y else -1),
                                            1 if start_y <= end_y else -1)
                                  ] for ((start_x, start_y), (end_x, end_y))
                                  in
                                  __import__("itertools").chain.from_iterable(
                                      [
                                          zip(line, line[1:])
                                          for line in [
                                          [(int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in pairs]
                                          for pairs in
                                          [line.split(" ->") for line in open("input.txt", "r").read().splitlines()]
                                      ]
                                      ]
                                  )
                              ])
                          }
            ),
            0,  # sand no
            False,  # finished?
            max({point[1] for point, val in initial_board.items() if val == '#'})
        )
    )[1]


# this transforms a recursive function to optimize tail calls using an adapted version of the Y Combinator
# therefore very deep recursion depths can easily be evaluated
def bet(func):
    b = (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args))))(func)

    def wrapper(*args):
        out = b(*args)
        while callable(out):
            out = out()
        return out

    return wrapper


# not a one-liner because bet() is used, but I found the tail call optimization to cool to completely throw out
# one line version using itertools below
def task_2_with_tailrec_optimization():
    final_state = (bet(lambda until: lambda pred, f, x: x if pred(*x) else until(pred, f, f(*x))))(
        lambda board, sand_no, finished: finished,  # check if finished
        lambda board, sand_no, finished:
        (board | {final_point: "o"}, sand_no + 1, True)
        if (final_point := (bet(lambda until: lambda pred, f, x: x if pred(*x) else until(pred, f, f(*x))))(
            lambda x, y: all(  # check if sand is at rest
                (
                    board[(x, y + 1)],
                    board[(x - 1, y + 1)],
                    board[(x + 1, y + 1)],
                )
            ),
            lambda x, y: next(  # get next move for sand
                (move for move in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)) if not board.get(move)),
                (x, y)
            ),
            (500, 0),
        )) == (500, 0)
        else (board | {final_point: "o"}, sand_no + 1, False),  # update board if we're not finished
        (
            initial_board :=
            (
                    {(x, y): None
                     for x in range(200, 800) for y in range(172)
                     } | (stones := {stone: "#"
                                     for stone in
                                     __import__("itertools").chain.from_iterable(
                                         [
                                             [
                                                 (x, y)
                                                 for x in range(start_x, end_x + (1 if start_x <= end_x else -1), 1 if start_x <= end_x else -1)
                                                 for y in range(start_y, end_y + (1 if start_y <= end_y else -1), 1 if start_y <= end_y else -1)
                                             ] for ((start_x, start_y), (end_x, end_y))
                                             in
                                             __import__("itertools").chain.from_iterable(
                                                 [
                                                     zip(line, line[1:])
                                                     for line in [
                                                         [(int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in pairs]
                                                         for pairs in
                                                         [line.split(" ->") for line in open("input.txt", "r").read().splitlines()]
                                                    ]
                                                 ]
                                             )
                                         ])
                                     }
                          ) | (lambda bottom: {(x, bottom): "#" for x in range(200, 800)})(
                max(stones, key=lambda p: p[1])[1] + 2)

            ),
            0,  # sand no
            False,  # finished?
        )
    )
    vis = visualize_board(final_state[0])
    with open("output.txt", "w+") as f:
        f.write(vis)
    return final_state[1]


def task_2():
    return (
        lambda accumulated: sum(
            1
            for _ in
            (
                __import__("itertools").takewhile(
                    lambda b: b is not None,
                    accumulated
                )
            )
        )
    )(
        __import__("itertools").accumulate(
            __import__("itertools").count(),
            lambda board, no:
                None
                if (final_point := (
                    __import__("collections").deque(  # get last element of point path
                        __import__("itertools").takewhile(
                            lambda p: p is not None,
                            __import__("itertools").accumulate(
                                __import__("itertools").count(),
                                lambda p, _:
                                None
                                if all(  # check if sand is at rest
                                    targets := list(
                                        map(lambda m: board.get(m),
                                            moves := [
                                                (x := p[0], (y := p[1]) + 1),
                                                (x - 1, y + 1),
                                                (x + 1, y + 1),
                                            ]
                                            )
                                    )
                                )
                                else moves[targets.index(None)],  # get move that leads to free field
                                initial=(500, 0)
                            )
                        ),
                        maxlen=1
                    ).pop()
                )
                ) == (500, 0)  # check if sand reached top
            else board | {final_point: "o"},  # update board if we're not finished
            initial=(
                    {(x, y): None
                     for x in range(200, 800) for y in range(172)
                     } | (stones := {stone: "#"
                                     for stone in
                                     __import__("itertools").chain.from_iterable(
                                         [
                                             [
                                                 (x, y)
                                                 for x in
                                                 range(start_x, end_x + (1 if start_x <= end_x else -1), 1 if start_x <= end_x else -1)
                                                 for y in
                                                 range(start_y, end_y + (1 if start_y <= end_y else -1), 1 if start_y <= end_y else -1)
                                             ] for ((start_x, start_y), (end_x, end_y))
                                             in
                                             __import__("itertools").chain.from_iterable(
                                                 [
                                                     zip(line, line[1:])
                                                     for line in [
                                                        [(int(pair.split(",")[0]), int(pair.split(",")[1])) for pair in pairs]
                                                        for pairs in
                                                        [line.split(" ->") for line in open("input.txt", "r").read().splitlines()]
                                                     ]
                                                 ]
                                             )
                                         ])
                                     }
                          ) | (lambda bottom: {(x, bottom): "#" for x in range(200, 800)})(max(stones, key=lambda p: p[1])[1] + 2)
            )
        )
    )


# no asserts, this takes a while
print(task_1())
print(task_2())
