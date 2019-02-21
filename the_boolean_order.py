# code: utf-8


from functools import lru_cache
from operator import and_, or_, xor

FUNCS = {'|': or_, '&': and_, '^': xor}


def solve(s, ops):

    @lru_cache(None)
    def evaluate(s, ops):
        c = [0, 0]
        if not ops:
            c[s == 't'] += 1
        else:
            for i in range(len(ops)):
                for v, n in enumerate(evaluate(s[:i+1], ops[:i])):
                    for w, m in enumerate(evaluate(s[i+1:], ops[i+1:])):
                        c[FUNCS[ops[i]](v, w)] += n*m
        print(c)
        return c

    return evaluate(s, ops)

    return evaluate(s, ops)[True]


# r1 = solve('tft', '^&')
# r2 = solve("ttftff", "|&^&&")
# r3 = solve("ttftfftf", "|&^&&||")
# r4 = solve("ttftfftft", "|&^&&||^")
# r5 = solve("ttftfftftf", "|&^&&||^&")
# print(r1, r2, r3, r4, r5)
# print(r2)

# solve('tft', '^&')

solve("ttftff", "|&^&&")
