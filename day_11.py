def parse_input():
    # items, op, test, true_monkey, false_monkey
    monkeys = [
        (lambda monkey_lines: {  # weird lambda trick to close scopes to prevent eval lambdas from interfering with each other
            "items": [int(part) for part in monkey_lines[1].replace(",", "").split() if part.isdigit()],
            "operation": lambda old: eval(" ".join(monkey_lines[2].split()[3:]), {}, {"old": old}),
            "test": lambda val: val % int(monkey_lines[3].split()[-1]) == 0,
            "trueM": int(monkey_lines[4].split()[-1]),
            "falseM": int(monkey_lines[5].split()[-1]),
            "timesInspected": 0,
        })(ml)
            for ml in (monkey.splitlines() for monkey in open('input.txt', 'r').read().split("\n\n"))
    ]
    return monkeys


def task_1():
    return (lambda final_state: __import__("functools").reduce(__import__("operator").mul, sorted([monkey["timesInspected"] for monkey in final_state])[-2:]))(__import__("functools").reduce(lambda monkeys, _: __import__("functools").reduce(lambda monkeys, current_monkey_no: __import__("functools").reduce(lambda monkeys, _: ((lambda monkeys, sender, recipient, item: [((monkey | {"items": monkey["items"][1:], "timesInspected": monkey["timesInspected"] + 1}) if n == sender else (monkey | {"items": monkey["items"] + [item]} if n == recipient else monkey)) for n, monkey in enumerate(monkeys)])(monkeys, current_monkey_no, current_monkey["trueM"] if (current_monkey := monkeys[current_monkey_no])["test"](new_item := (current_monkey["operation"](current_monkey["items"][0]) // 3)) else current_monkey["falseM"], new_item)) if monkeys[current_monkey_no]["items"] else monkeys, range(len(monkeys[current_monkey_no]["items"])), monkeys), range(len(monkeys)), monkeys), range(20), [(lambda monkey_lines: {"items": [int(part) for part in monkey_lines[1].replace(",", "").split() if part.isdigit()], "operation": lambda old: eval(" ".join(monkey_lines[2].split()[3:]), {}, {"old": old}), "test": lambda val: val % int(monkey_lines[3].split()[-1]) == 0, "trueM": int(monkey_lines[4].split()[-1]), "falseM": int(monkey_lines[5].split()[-1]), "timesInspected": 0,})(ml) for ml in (monkey.splitlines() for monkey in open('input.txt', 'r').read().split("\n\n"))]))


def task_1_prettier():
    return (lambda final_state:  __import__("functools").reduce(
        __import__("operator").mul,
        sorted(
            [monkey["timesInspected"]
             for monkey
             in final_state]
        )[-2:]
    ))(
        __import__("functools").reduce(
            lambda monkeys, _:
                __import__("functools").reduce(
                    lambda monkeys, current_monkey_no: __import__("functools").reduce(
                        lambda monkeys, _:
                            (
                                (
                                    lambda monkeys, sender, recipient, item:
                                        [
                                            (  # apply operation: move item from sender to reciever and update times inspected for sender
                                                (monkey | {"items": monkey["items"][1:], "timesInspected": monkey["timesInspected"] + 1})
                                                if n == sender
                                                else (
                                                    monkey | {"items": monkey["items"] + [item]}
                                                    if n == recipient
                                                    else monkey)
                                            )
                                            for n, monkey in enumerate(monkeys)
                                        ]
                                )(
                                    monkeys,
                                    current_monkey_no,
                                    # calculate reciever
                                    current_monkey["trueM"]
                                    if (current_monkey := monkeys[current_monkey_no])["test"](
                                        new_item := (current_monkey["operation"](
                                            current_monkey["items"][0]) // 3))
                                    else current_monkey["falseM"],
                                    new_item
                                )
                            ) if monkeys[current_monkey_no]["items"] else monkeys,
                        range(len(monkeys[current_monkey_no]["items"])),
                        monkeys
                    ),
                    range(len(monkeys)),
                    monkeys
                ),
            range(20),
            [
                (lambda monkey_lines: {
                    # weird lambda trick to close scopes to prevent eval lambdas from interfering with each other
                    "items": [int(part) for part in monkey_lines[1].replace(",", "").split() if part.isdigit()],
                    "operation": lambda old: eval(" ".join(monkey_lines[2].split()[3:]), {}, {"old": old}),
                    "test": lambda val: val % int(monkey_lines[3].split()[-1]) == 0,

                    "trueM": int(monkey_lines[4].split()[-1]),
                    "falseM": int(monkey_lines[5].split()[-1]),
                    "timesInspected": 0,
                })(ml)
                for ml in (monkey.splitlines() for monkey in open('input.txt', 'r').read().split("\n\n"))
            ]
        )
    )


def task_2():
    return (lambda final_state: __import__("functools").reduce(__import__("operator").mul, sorted([monkey["timesInspected"] for monkey in final_state])[-2:]))((lambda monkeys, threshold: __import__("functools").reduce(lambda monkeys, _: __import__("functools").reduce(lambda monkeys, current_monkey_no: __import__("functools").reduce(lambda monkeys, _: ((lambda monkeys, sender, recipient, item: [((monkey | {"items": monkey["items"][1:], "timesInspected": monkey["timesInspected"] + 1}) if n == sender else (monkey | {"items": monkey["items"] + [item]} if n == recipient else monkey)) for n, monkey in enumerate(monkeys)])(monkeys, current_monkey_no, current_monkey["trueM"] if (current_monkey := monkeys[current_monkey_no])["test"](new_item := (current_monkey["operation"](current_monkey["items"][0]))) else current_monkey["falseM"], new_item % threshold)) if monkeys[current_monkey_no]["items"] else monkeys, range(len(monkeys[current_monkey_no]["items"])), monkeys), range(len(monkeys)), monkeys), range(10000), monkeys))(ms := [(lambda monkey_lines: {"items": [int(part) for part in monkey_lines[1].replace(",", "").split() if part.isdigit()], "operation": lambda old: eval(" ".join(monkey_lines[2].split()[3:]), {}, {"old": old}), "test": lambda val: val % int(monkey_lines[3].split()[-1]) == 0, "trueM": int(monkey_lines[4].split()[-1]), "falseM": int(monkey_lines[5].split()[-1]), "timesInspected": 0, "divBy": int(monkey_lines[3].split()[-1])})(ml) for ml in (monkey.splitlines() for monkey in open('input.txt', 'r').read().split("\n\n"))], __import__("functools").reduce(__import__("operator").mul, (m["divBy"] for m in ms))))


def task_2_prettier():
    return (
        lambda final_state:
            __import__("functools").reduce(
                __import__("operator").mul,
                sorted(
                    [monkey["timesInspected"]
                     for monkey
                     in final_state]
                )[-2:]
            )
        )(
        (
            lambda monkeys, threshold:
                __import__("functools").reduce(
                    lambda monkeys, _:
                        __import__("functools").reduce(
                            lambda monkeys, current_monkey_no: __import__("functools").reduce(
                                lambda monkeys, _:
                                    (
                                        (
                                            lambda monkeys, sender, recipient, item:
                                                [
                                                    (
                                                        (monkey | {"items": monkey["items"][1:], "timesInspected": monkey["timesInspected"] + 1})
                                                        if n == sender
                                                        else (
                                                            monkey | {"items": monkey["items"] + [item]}
                                                            if n == recipient
                                                            else monkey)
                                                    )
                                                    for n, monkey in enumerate(monkeys)
                                                ]
                                        )(
                                            monkeys,
                                            current_monkey_no,
                                            current_monkey["trueM"]
                                            if (current_monkey := monkeys[current_monkey_no])["test"](
                                                new_item := (current_monkey["operation"](
                                                    current_monkey["items"][0])))
                                            else current_monkey["falseM"],
                                            new_item % threshold
                                        )
                                    ) if monkeys[current_monkey_no]["items"] else monkeys,
                                range(len(monkeys[current_monkey_no]["items"])),
                                monkeys
                            ),
                            range(len(monkeys)),
                            monkeys
                        ),
                    range(10000),
                    monkeys
                )
        )(
            ms := [
                (lambda monkey_lines: {
                    # weird lambda trick to close scopes to prevent eval lambdas from interfering with each other
                    "items": [int(part) for part in monkey_lines[1].replace(",", "").split() if part.isdigit()],
                    "operation": lambda old: eval(" ".join(monkey_lines[2].split()[3:]), {}, {"old": old}),
                    "test": lambda val: val % int(monkey_lines[3].split()[-1]) == 0,
                    "trueM": int(monkey_lines[4].split()[-1]),
                    "falseM": int(monkey_lines[5].split()[-1]),
                    "timesInspected": 0,
                    "divBy": int(monkey_lines[3].split()[-1])
                })(ml)
                for ml in (monkey.splitlines() for monkey in open('input.txt', 'r').read().split("\n\n"))
            ],
            __import__("functools").reduce(__import__("operator").mul, (m["divBy"] for m in ms))
        )
    )


def print_monkeys(monkeys):
    print("\n".join([f"monkey no: {i}, items: {monkey['items']}, {monkey['timesInspected']=}" for i, monkey in enumerate(monkeys)]))


assert task_1() == task_1_prettier()
print(task_1())

task_2_res = task_2()
assert task_2_res == task_2_prettier()
print(task_2_res)
