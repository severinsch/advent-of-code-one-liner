
def task_1() -> int:
    return next(filter(lambda seq: len(set(seq[1:])) == 4, zip(range(4, len(inp := [c for c in open('input.txt', 'r').read()]) + 1), inp, inp[1:], inp[2:], inp[3:])))[0]


def task_2() -> int:
    return next(filter(lambda seq: len(set(seq[1:])) == 14, zip(range(14, len(inp := [c for c in open('input.txt', 'r').read()]) + 1), *(inp[i:] for i in range(14)))))[0]


def task_all_in_one() -> list[int]:
    return list(map(lambda n: next(filter(lambda seq: len(set(seq[1:])) == n, zip(range(n, len(inp := [c for c in open('input.txt', 'r').read()]) + 1), *(inp[i:] for i in range(n)))))[0], (4, 14)))


def task_2_prettier() -> int:
    return next(
        filter(
            lambda seq: len(set(seq[1:])) == 14,
            zip(
                range(14, len(inp := [c for c in open('input.txt', 'r').read()]) + 1),
                *(inp[i:] for i in range(14))
            )
        )
    )[0]


print(task_1())
assert task_2() == task_2_prettier()
print(task_2())
print(task_all_in_one())
