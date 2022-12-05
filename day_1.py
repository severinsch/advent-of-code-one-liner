
def task():
    return max(map(lambda s: sum(map(int, s.split('\n'))),  open('input.txt', 'r').read().split('\n\n')))


def task2():
    return sum(sorted(map(lambda s: sum(map(int, s.split('\n'))),  open('input.txt', 'r').read().split('\n\n')))[-3:])


print(task())
print(task2())
