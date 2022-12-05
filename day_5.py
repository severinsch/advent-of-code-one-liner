
# trying out the parsing of the stack half of the input
def get_start_stacks(stack_input: str) -> list[list[str]]:
    return [list(filter(None, stack)) for stack in list(map(list, zip(*[[line[i:i+4].strip("[] ") for i in range(0, len(line), 4)] for line in stack_input.splitlines() if "[" in line])))]


# trying out the parsing of the instruction half of the input
def get_instructions(instruction_input: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, (s.split(" ")[1], s.split(" ")[3], s.split(" ")[5]))) for s in instruction_input.splitlines() if s]


def reduce_fun(stacks_acc: list[list[str]], instruction: tuple[int, int, int]) -> list[list[str]]:
    return [
        list(reversed(stacks_acc[instruction[1]-1][:instruction[0]])) + stack
        if instruction[2] == number + 1
        else stack[instruction[0]:]
             if number + 1 == instruction[1]
             else stack
        for number, stack in
        enumerate(stacks_acc)
    ]


def task_1() -> str:
    return "".join(stack[0] for stack in [__import__("functools").reduce(lambda stacks_acc, instruction: [list(reversed(stacks_acc[instruction[1]-1][:instruction[0]])) + stack if instruction[2] == number + 1 else stack[instruction[0]:] if number + 1 == instruction[1] else stack for number, stack in enumerate(stacks_acc)], instructions, stacks) for stacks, instructions in [([list(filter(None, stack)) for stack in list(map(list, zip(*[[line[i:i+4].strip("[] ") for i in range(0, len(line), 4)] for line in stack_input.splitlines() if "[" in line])))], [tuple(map(int, (s.split(" ")[1], s.split(" ")[3], s.split(" ")[5]))) for s in instruction_input.splitlines() if s]) for (stack_input, instruction_input) in [tuple(open("input.txt", "r").read().split("\n\n"))]]].pop())


def task_1_prettier() -> str:
    return "".join(
        stack[0]  # get top element from each stack
        for stack
        in [
            __import__("functools").reduce(  # fold over list of instructions using the current stack setup as the accumulator
                lambda stacks_acc, instruction: [
                    list(reversed(stacks_acc[instruction[1]-1][:instruction[0]])) + stack  # take crates from "from" stack, reverse them and add them to "to" stack
                    if instruction[2] == number + 1  # make sure current `stack` is the to stack
                    else stack[instruction[0]:]  # remove moved crates from "from" stack
                         if number + 1 == instruction[1]
                         else stack  # do nothing if current stack is neither "from" nor "to" stack
                    for number, stack in
                    enumerate(stacks_acc)
                ],
                instructions,
                stacks)
            for stacks, instructions in
                [
                    (
                        [list(filter(None, stack))   # filter empty symbols from stacks
                         for stack in
                         list(map(list, zip(*[  # transpose parsed stacks
                             [
                                 line[i:i+4].strip("[] ")   # split stack lines into the crates
                                  for i in
                                  range(0, len(line), 4)
                             ]
                             for line in
                             stack_input.splitlines()
                             if "[" in line])))],  # remove line with stack indices
                        [tuple(map(int, (s.split(" ")[1], s.split(" ")[3], s.split(" ")[5])))  # parse instruction input
                         for s in
                         instruction_input.splitlines() if s]
                    )  # tuple[start_stack, list[instruction]]
                    for (stack_input, instruction_input)
                    in [tuple(open("input.txt", "r").read().split("\n\n"))]
                ]
        ].pop()  # using the single element list comprehension to bind variables trick again
    )


# equal to task_1, just without reversing the list removed from each "from" stack
def task_2() -> str:
    return "".join(stack[0] for stack in [__import__("functools").reduce(lambda stacks_acc, instruction: [list(stacks_acc[instruction[1]-1][:instruction[0]]) + stack if instruction[2] == number + 1 else stack[instruction[0]:] if number + 1 == instruction[1] else stack for number, stack in enumerate(stacks_acc)], instructions, stacks) for stacks, instructions in [([list(filter(None, stack)) for stack in list(map(list, zip(*[[line[i:i+4].strip("[] ") for i in range(0, len(line), 4)] for line in stack_input.splitlines() if "[" in line])))], [tuple(map(int, (s.split(" ")[1], s.split(" ")[3], s.split(" ")[5]))) for s in instruction_input.splitlines() if s]) for (stack_input, instruction_input) in [tuple(open("input.txt", "r").read().split("\n\n"))]]].pop())


assert task_1() == task_1_prettier()

print(task_1())
print(task_2())
