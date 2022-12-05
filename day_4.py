

def task_1_ranges() -> int:
    return sum(s1 <= s2 or s2 <= s1 for s1, s2 in ((set(range(start1, end1+1)), set(range(start2, end2+1))) for start1, end1, start2, end2 in [tuple(map(int, l.split(",")[0].split("-") + l.split(",")[1].split("-"))) for l in open('input.txt', 'r').read().splitlines()]))


def task_1_ranges_prettier() -> int:
    return sum(  # use that sum counts True values in bool list
        s1 <= s2 or s2 <= s1
        for s1, s2 in
        (
            (set(range(start1, end1+1)), set(range(start2, end2+1)))  # set of a range contains all the contained numbers
            for start1, end1, start2, end2 in
            [
                tuple(
                    map(
                        int,  # map numbers to int
                        l.split(",")[0].split("-") + l.split(",")[1].split("-")  # split lines into numbers
                    )
                )
                for l
                in open('input.txt', 'r').read().splitlines()])
    )


def task_1_math() -> int:
    return sum(start1 <= start2 and end1 >= end2 or start2 <= start1 and end2 >= end1 for start1, end1, start2, end2 in [tuple(map(int, l.split(",")[0].split("-") + l.split(",")[1].split("-"))) for l in open('input.txt', 'r').read().splitlines()])


def task_1_math_prettier() -> int:
    return sum(
        start1 <= start2 and end1 >= end2 or start2 <= start1 and end2 >= end1
        for start1, end1, start2, end2 in
        [
            tuple(
                map(
                    int,
                    l.split(",")[0].split("-") + l.split(",")[1].split("-")
                )
            )
            for l in
            open('input.txt', 'r').read().splitlines()])


# TASK 2

def task_2() -> int:
    return sum(max(start1, start2) <= min(end1, end2) for start1, end1, start2, end2 in [tuple(map(int, l.split(",")[0].split("-") + l.split(",")[1].split("-"))) for l in open('input.txt', 'r').read().splitlines()])


def task_2_prettier() -> int:
    return sum(
        max(start1, start2) <= min(end1, end2)
        for start1, end1, start2, end2 in
        [
            tuple(
                map(
                    int,
                    l.split(",")[0].split("-") + l.split(",")[1].split("-")
                )
            )
            for l in
            open('input.txt', 'r').read().splitlines()])


assert task_1_math() == task_1_ranges() == task_1_math_prettier() == task_1_ranges_prettier()
print(task_1_math())
assert task_2() == task_2_prettier()
print(task_2())
