# coding: utf-8


def count_patterns_from(firstPoint, length):
    count = [0]

    go([firstPoint], length, count)

    return count


def go(path, length, count):
    if len(path) == length:
        print(''.join(path))
        count[0] += 1
        return -1

    for c in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        if is_good(c, path):
            p = path.copy()
            p.append(c)
            go(p, length, count)

    return


def is_good(c, path):
    # no repeat
    if c in path:
        return False

    p = path[-1]
    # across 'E' requires passed 'E'
    if set((c, p)) == set(('A', 'I')):
        return 'E' in path
    if set((c, p)) == set(('C', 'G')):
        return 'E' in path
    if set((c, p)) == set(('B', 'H')):
        return 'E' in path
    if set((c, p)) == set(('D', 'F')):
        return 'E' in path

    # across 'B' requires passed 'B'
    if set((c, p)) == set(('A', 'C')):
        return 'B' in path

    # across 'D' requires passed 'D'
    if set((c, p)) == set(('A', 'G')):
        return 'D' in path

    # across 'F' requires passed 'F'
    if set((c, p)) == set(('C', 'I')):
        return 'F' in path

    # across 'H' requires passed 'H'
    if set((c, p)) == set(('G', 'I')):
        return 'H' in path

    # we are good
    return True


count_patterns_from('E', 4)
