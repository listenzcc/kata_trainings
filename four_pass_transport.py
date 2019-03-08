# code: utf-8

'''
The eccentric candy-maker, Billy Bonka, is building a new candy factory to produce his new 4-flavor sugar pops. The candy is made by placing a piece of candy base onto a conveyer belt which transports the candy through four separate processing stations in sequential order. Each station adds another layer of flavor.

Due to an error in the factory blueprints, the four stations have been constructed in incorrect locations. It's too costly to disassemble the stations, so you've been called in.

Arrange the directional path of the conveyer belt so that it passes through each of the stations in sequential order while also traveling the shortest distance possible.

Input
An array consisting of the locations of each station on the factory floor, in order. The factory floor is a `10` x `10` matrix (with `0` starting index).

Output
Your function should return the path of the conveyer belt as an array.
If a valid configuration is not possible, return `null` or `None`.

The position values in the input and output arrays will consist of integers in the range `0 - 99`, inclusive. These integers represent a position on the factory floor.
For example, the position `[0,8]` is given as `8`, and `[4,6]` is given as `46`

Technical Details
The conveyer belt must run through each station once and in ascending order
The conveyer belt must not intersect/overlap itself
The distance covered by the conveyer belt must be the minimum necessary to complete the task
Full Test Suite: `30` fixed tests, `100` random tests
Inputs will always be valid and each test will have zero or more possible solutions..
'''


def four_pass(stations):
    print(stations)
    sdict = parse(stations)
    print(sdict)

    pass


def parse(stations):
    sdict = dict()
    for j, s in enumerate(stations):
        sdict[(s//10, s % 10)] = j+1
    return sdict


def short_path(s1, s2):
    dist_dict = dict()
    dist_dict[s1] = 1


def mk_dist_dict(n=10):
    dist_dict = dict()
    for j in range(10):
        for k in range(10):
            dist_dict[(j, k)] = 0
    return dist_dict


example_tests = [
    [1, 69, 95, 70],
    [0, 49, 40, 99],
    [37, 61, 92, 36],
    [51, 24, 75, 57],
    [92, 59, 88, 11]]

four_pass(example_tests[0])
