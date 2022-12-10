def parse_filesystem() -> dict:
    inp = open("input.txt", "r").read().split("\n")
    # insert = lambda loc, val, data: data | functools.reduce(lambda x, y: {y, x}, reversed(loc), val)
    f = lambda acc, cmd: \
        ((acc[0] + [_dir], acc[1]) if (_dir := cmd.split()[2]) != ".." else (acc[0][:-1], acc[1])) \
            if cmd.startswith("$ cd") \
            else (acc[0], (insert := lambda loc, val, data: data | {loc[0]: val} if len(loc) == 1 else {
            k: (v if k != loc[0] else insert(loc[1:], val, v)) for k, v in data.items()}) \
            (acc[0] + ["_files"],
             (get := lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data))(
                 acc[0] + ["_files"], acc[1], []) + [int(size)],
             acc[1])) \
            if (size := cmd.split()[0]).isdigit() \
            else (acc[0], (insert := lambda loc, val, data: data | {loc[0]: val} if len(loc) == 1 else {
            k: (v if k != loc[0] else insert(loc[1:], val, v)) for k, v in data.items()}) \
            (cur_loc := (acc[0] + [cmd.split()[1]]),
             (get := lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data))(cur_loc,
                                                                                                             acc[1],
                                                                                                             {}),
             acc[1])) if cmd.startswith("dir") else acc
    return __import__("functools").reduce(f, inp, ([], {"/": {"_files": []}}))[1]


def get_total_size(dir: dict) -> tuple[int, int]:
    total_sizes, accumulated_relevant_sizes = list(zip(*sizes)) if (sizes := [get_total_size(v) for v in dir.values() if isinstance(v, dict)]) else [(0,), (0,)]
    return (curr_total, (sum(accumulated_relevant_sizes) + curr_total)) if (curr_total := (sum(total_sizes) + sum(dir.get("_files", [])))) <= 100000 else (curr_total, sum(accumulated_relevant_sizes))


def task_1_prettier() -> int:
    return \
    (f := lambda dir:
            (lambda total_sizes, accumulated_relevant_sizes:
             (curr_total, (sum(accumulated_relevant_sizes) + curr_total))
             if (curr_total := (sum(total_sizes) + sum(dir.get("_files", [])))) <= 100000
             else (curr_total, sum(accumulated_relevant_sizes))
             )(*list(zip(*sizes))
                if (sizes := [f(v) for v in dir.values() if isinstance(v, dict)])
                else [(0,), (0,)])
        )(__import__("functools").reduce(  # parsing
            lambda acc, cmd:
            ((acc[0] + [_dir], acc[1]) if (_dir := cmd.split()[2]) != ".." else (acc[0][:-1], acc[1]))
            if cmd.startswith("$ cd")
            else (acc[0],
                  (insert := lambda loc, val, data:
                    data | {loc[0]: val}
                    if len(loc) == 1
                    else {k: (v
                              if k != loc[0]
                              else insert(loc[1:], val, v))
                          for k, v in data.items()}
                  )(  # apply insert
                      *(  # choose parameter tuple for insert lambda (insert dir vs insert file) and unpack tuple
                          (
                              acc[0] + ["_files"],  # loc
                              (lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data)  # get val at loc from data
                               )(acc[0] + ["_files"], acc[1], []) + [int(size)],  # val
                              acc[1]  # data
                          )
                          if (size := cmd.split()[0]).isdigit()
                          else (
                            cur_loc := (acc[0] + [cmd.split()[1]]),  # loc
                            (lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data)  # get val at loc from data
                             )(cur_loc, acc[1], {}),  # val
                            acc[1])  # data

                       )
                  )
                  )
            if not cmd.startswith("$ ls")
            else acc,
            open("input.txt", "r").read().split("\n"),  # input to reduce
            ([], {"/": {"_files": []}})  # start acc
        )[1]["/"]  # get second element from result acc (= filesystem dict)
    )[1]  # get second element from result (=total relevant size)


def task_1() -> int:
    return (f := lambda dir: (lambda total_sizes, accumulated_relevant_sizes: (curr_total, (sum(accumulated_relevant_sizes) + curr_total)) if (curr_total := (sum(total_sizes) + sum(dir.get("_files", [])))) <= 100000 else (curr_total, sum(accumulated_relevant_sizes)))(*list(zip(*sizes)) if (sizes := [f(v) for v in dir.values() if isinstance(v, dict)]) else [(0,), (0,)]))(__import__("functools").reduce(lambda acc, cmd: ((acc[0] + [_dir], acc[1]) if (_dir := cmd.split()[2]) != ".." else (acc[0][:-1], acc[1])) if cmd.startswith("$ cd") else (acc[0], (insert := lambda loc, val, data: data | {loc[0]: val} if len(loc) == 1 else {k: (v if k != loc[0] else insert(loc[1:], val, v)) for k, v in data.items()})(*((acc[0] + ["_files"], (lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data))(acc[0] + ["_files"], acc[1], []) + [int(size)], acc[1]) if (size := cmd.split()[0]).isdigit() else (cur_loc := (acc[0] + [cmd.split()[1]]), (get := lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data))(cur_loc, acc[1], {}), acc[1])))) if not cmd.startswith("$ ls") else acc, open("input.txt", "r").read().split("\n"), ([], {"/": {"_files": []}}))[1]["/"])[1]


def task_2():
    return (lambda sizes: next(__import__("itertools").dropwhile(lambda size: 70000000 - sizes[-1][0] + size[0] < 30000000, sizes))[0])(sorted((get_sizes := lambda d, level: (all_sizes := list(__import__("itertools").chain.from_iterable([get_sizes(v, level + 1) for k, v in d.items() if k != "_files"]))) + [(sum([val for val, lvl in all_sizes if lvl == level + 1]) + sum(d.get("_files", [])), level)])(__import__("functools").reduce(lambda acc, cmd: ((acc[0] + [_dir], acc[1]) if (_dir := cmd.split()[2]) != ".." else (acc[0][:-1], acc[1])) if cmd.startswith("$ cd") else (acc[0], (insert := lambda loc, val, data: data | {loc[0]: val} if len(loc) == 1 else {k: (v if k != loc[0] else insert(loc[1:], val, v)) for k, v in data.items()})(*((acc[0] + ["_files"], (lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data))(acc[0] + ["_files"], acc[1], []) + [int(size)], acc[1]) if (size := cmd.split()[0]).isdigit() else (cur_loc := (acc[0] + [cmd.split()[1]]), (get := lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data))(cur_loc, acc[1], {}), acc[1])))) if not cmd.startswith("$ ls") else acc, open("input.txt", "r").read().split("\n"), ([], {"/": {"_files": []}}))[1]["/"], 0)))


def task_2_prettier():
    return (
        lambda sizes:
            next(__import__("itertools").dropwhile(
                lambda size: 70000000 - sizes[-1][0] + size[0] < 30000000, sizes
            ))[0])\
            (sorted(
                (get_sizes := lambda d, level:
                    (all_sizes := list(__import__("itertools").chain.from_iterable([get_sizes(v, level+1) for k, v in d.items() if k != "_files"]))) +
                    [(sum([val for val, lvl in all_sizes if lvl == level+1]) + sum(d.get("_files", [])), level)])
                (__import__("functools").reduce(  # parsing
                    lambda acc, cmd:
                    ((acc[0] + [_dir], acc[1]) if (_dir := cmd.split()[2]) != ".." else (acc[0][:-1], acc[1]))
                    if cmd.startswith("$ cd")
                    else (acc[0],
                          (insert := lambda loc, val, data:
                            data | {loc[0]: val}
                            if len(loc) == 1
                            else {k: (v
                                      if k != loc[0]
                                      else insert(loc[1:], val, v))
                                  for k, v in data.items()}
                          )(  # apply insert
                              *(  # choose parameter tuple for insert lambda (insert dir vs insert file) and unpack tuple
                                  (
                                      acc[0] + ["_files"],  # loc
                                      (lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data)  # get val at loc from data
                                       )(acc[0] + ["_files"], acc[1], []) + [int(size)],  # val
                                      acc[1]
                                  )
                                  if (size := cmd.split()[0]).isdigit()  # data
                                  else (
                                    cur_loc := (acc[0] + [cmd.split()[1]]),  # loc
                                    (get := lambda loc, data, default: __import__("functools").reduce(lambda d, k: d.get(k, default), loc, data)  # get val at loc from data
                                     )(cur_loc, acc[1], {}),  # val
                                    acc[1])  # data

                               )
                          )
                          )
                    if not cmd.startswith("$ ls")
                    else acc,
                    open("input.txt", "r").read().split("\n"),  # input to reduce
                    ([], {"/": {"_files": []}})  # start acc
        )[1]["/"], 0)))


assert task_1() == task_1_prettier()
assert task_2() == task_2_prettier()
print(task_1())
print(task_2())
