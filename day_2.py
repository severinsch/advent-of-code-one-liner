def game_score(op: int, me: int) -> int:
    # draw
    if me == op:
        print("draw")
        return 3 + me + 1
    else:
        # op wins
        if (me + 1) % 3 == op:
            print("op win")
            return me + 1
        else:
            # op wins
            print("i win")
            return 6 + me + 1


# A = 0, B = 1, C = 2, X = 0, Y = 1, Z = 2
def get_shape_number(input: str) -> tuple[int, int]:
    res = ord(input.split()[0]) - 65, ord(input.split()[1]) - 88
    return res


# return sum(game_score(me, op) for (me, op) in map(get_shape_number, rounds))
def task1():
    return sum(me + (3 if (me-1) == op else 0 if me % 3 == op else 6) for (op, me) in map(lambda s: (ord(s.split()[0]) - 65, ord(s.split()[1]) - 87), open('input.txt', 'r').read().splitlines()))


# A = Rock = 0
# B = Paper = 1
# C = Scissors = 2
# outcome: 0 = lose, 1 = draw, 2 = win
def get_my_score(op: int, outcome: int) -> int:
    correct_move = (op + (outcome-1)) % 3
    return 3 * outcome + (correct_move + 1)


# 3 * outcome + (op_move + (outcome - 1)) % 3 + 1
# 3 * outcome: 0 for loss, 3 for draw, 6 for win
# (op_move + (outcome - 1)) % 3: returns correct move to get desired result
# + 1: to get score for correct move
def task2():
    return sum(3 * outcome + (op_move + (outcome-1)) % 3 + 1 for op_move, outcome in map(lambda s: (ord(s.split()[0]) - 65, ord(s.split()[1]) - 88), open('input.txt', 'r').read().splitlines()))


print(f'task 1:  {task1()}')
print(f'task 2:  {task2()}')
