import itertools


def task_1():
    return (lambda values, relevant_values: sum(next_vals[0] * v1 for (c1, v1), (c2, _) in zip(values, values[1:]) if (next_vals := [val for val in relevant_values if c1 < val <= c2])))(values := list(itertools.accumulate((None if line == "noop" else int(line.split()[1]) for line in open('input.txt', 'r').read().splitlines()), lambda acc, add: (acc[0] + 1, acc[1]) if add is None else (acc[0] + 2, acc[1] + add), initial=(0, 1))), set(itertools.takewhile(lambda v: v <= values[-1][0], itertools.count(20, 40))))


def task_1_prettier():
    return (
        lambda values, relevant_values:
            sum(
                next_vals[0] * v1
                for (c1, v1), (c2, _) in
                zip(values, values[1:])
                if (next_vals := [val for val in relevant_values
                                  if c1 < val <= c2])
            )
    )(
        values := list(itertools.accumulate(
            (None if line == "noop" else int(line.split()[1])
             for line in open('input.txt', 'r').read().splitlines()),
            lambda acc, add:
                (acc[0] + 1, acc[1])
                if add is None
                else (acc[0] + 2, acc[1] + add),
            initial=(0, 1)
            )
        ),
        set(itertools.takewhile(lambda v: v <= values[-1][0], itertools.count(20, 40)))
    )


assert task_1() == task_1_prettier()
print(task_1_prettier())
