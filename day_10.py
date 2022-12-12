def task_1():
    return (lambda values, relevant_values: sum(next_vals[0] * v1 for (c1, v1), (c2, _) in zip(values, values[1:]) if (next_vals := [val for val in relevant_values if c1 < val <= c2])))(values := list(__import__("itertools").accumulate((None if line == "noop" else int(line.split()[1]) for line in open('input.txt', 'r').read().splitlines()), lambda acc, add: (acc[0] + 1, acc[1]) if add is None else (acc[0] + 2, acc[1] + add), initial=(0, 1))), set(__import__("itertools").takewhile(lambda v: v <= values[-1][0], __import__("itertools").count(20, 40))))


# works for arbitrary program sizes with n signal measuring times (not just 6)
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
        values := list(__import__("itertools").accumulate(
            (None if line == "noop" else int(line.split()[1])
             for line in open('input.txt', 'r').read().splitlines()),
            lambda acc, add:
                (acc[0] + 1, acc[1])
                if add is None
                else (acc[0] + 2, acc[1] + add),
            initial=(0, 1)
            )
        ),
        set(__import__("itertools").takewhile(lambda v: v <= values[-1][0], __import__("itertools").count(20, 40)))
    )


def task_2():
    return "\n".join((lambda total_output: [total_output[i:i+40] for i in range(0, len(total_output), 40)])(__import__("functools").reduce(lambda acc, op: acc + ('#' if op[0] % 40 in {op[1] - 1, op[1], op[1] + 1} else '.'), (lambda values: list(__import__("itertools").chain.from_iterable(([(c1, v1)] if c2 - c1 == 1 else [(c1, v1), (c1 + 1, v1)] for (c1, v1), (c2, v2) in zip(values, values[1:])))))(list(__import__("itertools").accumulate((None if line == "noop" else int(line.split()[1]) for line in open('input.txt', 'r').read().splitlines()), lambda acc, add: (acc[0] + 1, acc[1]) if add is None else (acc[0] + 2, acc[1] + add), initial=(0, 1)))), "")))


def task_2_prettier():
    return "\n".join(
        (
            lambda total_output:
                [total_output[i:i+40] for i in range(0, len(total_output), 40)]
        )(
            __import__("functools").reduce(
                lambda acc, op:
                    acc + ('#' if op[0] % 40 in {op[1] - 1, op[1], op[1] + 1} else '.'),
                (
                    lambda values:  # interpolate missing cycles
                        list(__import__("itertools").chain.from_iterable(
                            ([(c1, v1)]
                             if c2 - c1 == 1 else [(c1, v1), (c1 + 1, v1)]
                             for (c1, v1), (c2, v2) in
                             zip(values, values[1:]))
                        ))
                )(
                    list(
                        __import__("itertools").accumulate(
                            (None if line == "noop" else int(line.split()[1])
                             for line in open('input.txt', 'r').read().splitlines()
                             ),
                            lambda acc, add:
                                (acc[0] + 1, acc[1])
                                if add is None
                                else (acc[0] + 2, acc[1] + add),
                            initial=(0, 1)
                        )
                    )
                ),
                ""
            )
        )
    )


assert task_1() == task_1_prettier()
print(task_1())
assert task_2() == task_2_prettier()
print(task_2())
