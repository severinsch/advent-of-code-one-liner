
def task_1():
    return (
        # perform bellman ford algorithm
        lambda nodes, edges, goal:
           __import__("functools").reduce(
               lambda distances, r: __import__("functools").reduce(
                   lambda dist, edge:
                   dist | {edge[1]: dist[edge[0]] + 1}  # update distance of v
                   if dist[edge[0]] != __import__("sys").maxsize and dist[edge[0]] + 1 < dist[edge[1]]
                   else dist,
                   edges,
                   distances
               ),
               range(len(nodes)),
               {coords: __import__("sys").maxsize if h != 'S' else 0 for (h, coords) in nodes}  # initial distances
           )[goal]
           )(
        nodes := list(
            __import__("itertools").chain.from_iterable(
                    board := [
                        [(c, (column_no, row_no)) for column_no, c in enumerate(line)]
                        for row_no, line in
                        enumerate(open("input.txt", "r").read().splitlines())
                    ]
                )
        ),  # nodes
        list(
            __import__("itertools").chain.from_iterable(  # edges
                [
                    [((x, y), (nb_x, nb_y))
                     for nb_x, nb_y
                     in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                     if 0 <= nb_x < len(board[0]) and 0 <= nb_y < len(board) and
                     (get_height := lambda c: 97 if c == 'S' else (122 if c == 'E' else ord(c)))(board[nb_y][nb_x][0]) <= get_height(h) + 1
                     ]
                    for (h, (x, y)) in
                    list(nodes)
                ]
            )
        ),
        [(x, y) for h, (x, y) in nodes if h == 'E'].pop()  # goal
    )


# same as task 1, only every 'a' also has initial distance 0
def task_2():
    return (
        lambda nodes, edges, goal:
           __import__("functools").reduce(
               lambda distances, r: __import__("functools").reduce(
                   lambda dist, edge:
                   dist | {edge[1]: dist[edge[0]] + 1}
                   if dist[edge[0]] != __import__("sys").maxsize and dist[edge[0]] + 1 < dist[edge[1]]
                   else dist,
                   edges,
                   distances
               ),
               range(len(nodes)),
               {coords: __import__("sys").maxsize if h not in ['S', 'a'] else 0 for (h, coords) in nodes}  # initial distances
           )[goal]
           )(
        nodes := list(
            __import__("itertools").chain.from_iterable(
                    board := [
                        [(c, (column_no, row_no)) for column_no, c in enumerate(line)]
                        for row_no, line in
                        enumerate(open("input.txt", "r").read().splitlines())
                    ]
                )
        ),  # nodes
        list(
            __import__("itertools").chain.from_iterable(  # edges
                [
                    [((x, y), (nb_x, nb_y))
                     for nb_x, nb_y
                     in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                     if 0 <= nb_x < len(board[0]) and 0 <= nb_y < len(board) and
                     (get_height := lambda c: 97 if c == 'S' else (122 if c == 'E' else ord(c)))(board[nb_y][nb_x][0]) <= get_height(h) + 1
                     ]
                    for (h, (x, y)) in
                    list(nodes)
                ]
            )
        ),
        [(x, y) for h, (x, y) in nodes if h == 'E'].pop()  # goal
    )


def visualize_distances(distances, rows: int, columns: int):
    res = ""
    for row in range(rows):
        for column in range(columns):
            d = distances[(column, row)]
            res += f"{d if d < __import__('sys').maxsize else '.':^3}|"
        res += "\n"
    return res


print(task_1())
print(task_2())
