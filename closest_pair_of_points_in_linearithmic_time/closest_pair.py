# code: utf-8
import itertools


def closest_pair(points):
    points = sorted(points)
    print(len(points))
    # if len(points) > 1000:
    #    return ((0, 0), (0, 0))
    # print(points[0:2000])
    return find_closest(points, 0, len(points))[0]
    pass


def find_closest(points, start, end):
    #print('finding:', [points[_] for _ in range(start, end)])
    if end - start < 10:
        closest_pair = (points[start], points[end-1])
        least_dist = dist(closest_pair)
        for j, k in itertools.combinations(range(start, end), 2):
            d = dist((points[j], points[k]))
            if d < least_dist:
                least_dist = d
                closest_pair = (points[j], points[k])
        return closest_pair, least_dist

    medium = (start + end) // 2
    left_closest_pair, least_dist_left = find_closest(points, start, medium)
    #print(left_closest_pair, least_dist_left)
    if least_dist_left == 0:
        return left_closest_pair, 0
    right_closest_pair, least_dist_right = find_closest(points, medium, end)
    #print(right_closest_pair, least_dist_right)
    if least_dist_right == 0:
        return right_closest_pair, 0
    min_left_right = min([least_dist_left, least_dist_right])

    closest_pair = (points[start], points[end-1])
    least_dist = dist(closest_pair)
    for j in range(medium-1, start-1, -1):
        left_point = points[j]
        if (left_point[0]-points[medium][0])**2 > min_left_right/4:
            break

        for k in range(medium, end):
            right_point = points[k]
            if (right_point[0]-points[medium-1][0])**2 > min_left_right/4:
                break

            d = dist((left_point, right_point))
            if d < least_dist:
                least_dist = d
                closest_pair = (left_point, right_point)

    if least_dist < min_left_right:
        return closest_pair, least_dist

    if least_dist_left < least_dist_right:
        return left_closest_pair, least_dist_left

    return right_closest_pair, least_dist_right


def dist(pair):
    return (pair[0][0]-pair[1][0]) ** 2 + (pair[0][1]-pair[1][1]) ** 2


points1 = (
    (2, 2),  # A
    (2, 8),  # B
    (5, 5),  # C
    (6, 3),  # D
    (6, 7),  # E
    (7, 4),  # F
    (7, 9)  # G
)

points2 = (
    (2, 2),  # A
    (2, 8),  # B
    (5, 5),  # C
    (5, 5),  # C
    (6, 3),  # D
    (6, 7),  # E
    (7, 4),  # F
    (7, 9)  # G
)

closest_pair(points1)

closest_pair([(2, 2), (6, 3)])
