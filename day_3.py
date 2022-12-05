def task_1() -> int:
    return sum((comp1 & comp2).pop() for comp1, comp2 in ((set(ls[:len(ls) // 2]), set(ls[len(ls) // 2:])) for ls in map(lambda s: [ord(c) - (38 if c <= 'Z' else 96) for c in s], open('input.txt', 'r').read().splitlines())))


def task_1_prettier() -> int:
    return sum(
        (comp1 & comp2).pop()  # get the common char from both sets
        for comp1, comp2
        in (
            (set(ls[:len(ls) // 2]), set(ls[len(ls) // 2:]))  # split list into two sets in the middle
            for ls in
            map(
                lambda s: [ord(c) - (38 if c <= 'Z' else 96) for c in s],  # map to priorities
                open('input.txt', 'r').read().splitlines()
            )
        )
    )


def task_2() -> int:
    return sum((group[0] & group[1] & group[2]).pop() for group in [(all_elf_prios[i:i + 3] for i in range(0, len(all_elf_prios), 3)) for all_elf_prios in [list(map(lambda s: {ord(c) - (38 if c <= 'Z' else 96) for c in s}, open('input.txt', 'r').read().splitlines()))]].pop())


def task_2_prettier() -> int:
    return sum(
        (group[0] & group[1] & group[2]).pop()  # get the common char from the 3 sets
        for group in
        [
            (  # split list into chunks of 3
                all_elf_prios[i:i + 3]
                for i in range(0, len(all_elf_prios), 3)
            )
            for all_elf_prios
            in [  # create single element list to bind expression below to all_elf_prios using comprehension
                list(map(
                        lambda s: {ord(c) - (38 if c <= 'Z' else 96) for c in s},  # map to priorities
                        open('input.txt', 'r').read().splitlines()
                        ))
                ]
        ].pop()  # get element from single element list after transformation
    )


print(task_1())
assert task_2() == task_2_prettier()
print(task_2())
