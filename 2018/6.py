#!/usr/bin/env python3

import lib.common as lib

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def part_one(line_gen):
    coordinates = []
    for line in line_gen:
        coordinates.append(tuple(int(k) for k in line.split(',')))

    max_y = max(t[1] for t in coordinates)
    min_y = min(t[1] for t in coordinates)
    min_x = min(t[0] for t in coordinates)
    max_x = max(t[0] for t in coordinates)
    inner_points = [(x, y) for x, y in coordinates \
                    if x > min_x and x < max_x and y > min_y and y < max_y]

    max_fill = 0
    for x, y in inner_points:
        cur_fill = set()
        worklist = set([(x, y)])
        while worklist:
            x_c, y_c = worklist.pop()
            cur_fill.add((x_c, y_c))
            # We reached outside the border, will become infinite
            if x_c not in range(min_x, max_x + 1) or y_c not in range(min_y, max_y + 1):
                cur_fill = set()
                break
            # Extend set of belonging points for (x, y)
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_x, next_y = (x_c + dx, y_c + dy)
                if (next_x, next_y) in cur_fill:
                    continue
                min_d = 9999999
                min_c = None
                for cx, cy in coordinates:
                    d = distance(next_x, next_y, cx, cy)
                    if d < min_d:
                        min_d = d
                        min_c = (cx, cy)
                if min_c == (x, y):
                    worklist.add((next_x, next_y))
        max_fill = max(max_fill, len(cur_fill))
    return max_fill

def part_two(line_gen):
    coordinates = []
    for line in line_gen:
        coordinates.append(tuple(int(k) for k in line.split(',')))

    m_x = int(sum(t[0] for t in coordinates)/len(coordinates))
    m_y = int(sum(t[1] for t in coordinates)/len(coordinates))
    max_sum = 10000

    worklist = set([(m_x, m_y)])
    fill = set()
    while worklist:
        cur_x, cur_y = worklist.pop()
        fill.add((cur_x, cur_y))
        
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            next_x, next_y = (cur_x + dx, cur_y + dy)
            sum_d = sum(distance(next_x, next_y, cx, cy) for cx, cy in coordinates)
            if sum_d < max_sum and (next_x, next_y) not in fill:
                worklist.add((next_x, next_y))

    return len(fill)

print("A: " + str(part_one(lib.get_input(6))))
print("B: " + str(part_two(lib.get_input(6))))
