# code: utf-8


def calc(expression):
    print(expression)
    replace_dict = {
        '*': ' * ',
        '/': ' / ',
        '+': ' + ',
        '-': ' - ',
        '(': ' ( ',
        ')': ' ) '
    }
    print('-' * 20)
    expression = expression.replace(' ', '')
    for e in replace_dict.items():
        expression = expression.replace(e[0], e[1])
    print(expression)
    elements = expression.split()
    print(elements)
    if elements[0] is '-':
        elements[1] = '-' + elements[1]
        elements.pop(0)
    for j in range(1, len(elements)):
        if elements[j] is '-' and elements[j-1] in ['+', '-', '*', '/', '(', '-(']:
            elements[j] = ''
            elements[j+1] = '-' + elements[j+1]
    while '' in elements:
        elements.pop(elements.index(''))
    print(' '.join(elements))

    num_stack = []
    opt_stack = []
    for e in elements:
        print(num_stack, opt_stack)
        print('>>:', e, end=': ')
        if e == ')':
            new_num_stack = [num_stack.pop()]
            new_opt_stack = []
            while True:
                o = opt_stack.pop()
                if o in ['(', '-(']:
                    break
                new_opt_stack.append(o)
                new_num_stack.append(num_stack.pop())
            print('            ', new_num_stack, new_opt_stack, end='| ')
            if not new_opt_stack == []:
                new_opt_stack.reverse()
                for e in new_opt_stack:
                    do(new_num_stack, e, r=True)
            if o == '(':
                num_stack.append(new_num_stack.pop())
            if o == '-(':
                num_stack.append(-new_num_stack.pop())
            print('             ', num_stack[-1])
            if len(opt_stack) == 0:
                continue
            if opt_stack[-1] in ['*', '/']:
                do(num_stack, opt_stack.pop())
            continue
        if e in ['+', '-', '*', '/', '(', '-(']:
            opt_stack.append(e)
            continue
        num_stack.append(float(e))
        if len(opt_stack) == 0:
            continue
        if opt_stack[-1] in ['*', '/']:
            do(num_stack, opt_stack.pop())
            continue
    print(num_stack, opt_stack)

    num_stack.reverse()
    print(num_stack, opt_stack)
    for e in opt_stack:
        do(num_stack, e, r=True)

    return num_stack[0]


def do(num_stack, o, r=False):
    if o == '(':
        return False
    if o == '-(':
        num_stack[-1] *= -1
        return False
    assert(o in ['+', '-', '*', '/'])
    assert(len(num_stack) > 1)
    if r:
        a = num_stack.pop()
        b = num_stack.pop()
    else:
        b = num_stack.pop()
        a = num_stack.pop()
    if o is '+':
        num_stack.append(a + b)
    if o is '-':
        num_stack.append(a - b)
    if o is '*':
        num_stack.append(a * b)
    assert(not b == 0)
    if o is '/':
        num_stack.append(a / b)
    return True


tests = [
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14],
    ['1+2-3*(3+4*2+2)-3', 0],
    ['-(-1)', 0],
    ['26 + -5 + 93 - 95 / -89 * -36 + 21 + 8', 0],
    ['-(56) / (49 - -34 - (21)) + (61 - ((((-82 / 46)))) * -21)', 0],
    ['-( 31 ) * ( -82 + 44 / ( 63 ) ) * ( 31 + -( ( ( ( 18 - -27 ) ) ) ) - 95 )', 0]
]

for test in tests:
    print(calc(test[0]), '=', eval(test[0]))
