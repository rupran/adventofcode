#!/usr/bin/env python3

import collections
import itertools
import lib.common as lib

def do_bfs(grid, start, distances):
    seen = set()
    seen.add(start)
    start_val = grid[start[0]][start[1]]
    worklist = collections.deque()
    worklist.append((start, 0))

    while worklist:
        cur, cur_dist = worklist.popleft()
        cur_y, cur_x = cur

        if grid[cur_y][cur_x].isdigit() and cur != start:
            found_val = grid[cur_y][cur_x]
            distances[start_val][found_val] = cur_dist
            distances[found_val][start_val] = cur_dist

        for delta_y, delta_x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (cur_y + delta_y, cur_x + delta_x)
            if neighbor not in seen and grid[neighbor[0]][neighbor[1]] != "#":
                seen.add(neighbor)
                worklist.append((neighbor, cur_dist + 1))

def read_grid(line_gen):
    grid = []
    for line in line_gen:
        cur_row = [x for x in line]
        grid.append(cur_row)

    target_coords = []
    for y, _ in enumerate(grid):
        for x, _ in enumerate(grid[y]):
            if grid[y][x].isdigit():
                target_coords.append((y, x))

    return grid, target_coords

def calc_min_distance(line_gen, second_part=False):
    grid, target_coords = read_grid(line_gen)

    distances = collections.defaultdict(dict)
    for cur_start in target_coords:
        do_bfs(grid, cur_start, distances)

    min_dist = int(1e10)
    for order in itertools.permutations(list(distances.keys())):
        if order[0] != "0":
            continue

        cur_dist = 0
        for walk in zip(order, order[1:]):
            cur_dist += distances[walk[0]][walk[1]]

        if second_part:
            cur_dist += distances[order[-1]][order[0]]

        if cur_dist < min_dist:
            min_dist = cur_dist

    return min_dist

def part_one(line_gen):
    return calc_min_distance(line_gen)

def part_two(line_gen):
    return calc_min_distance(line_gen, second_part=True)

print("A: " + str(part_one(lib.get_input(24))))
print("B: " + str(part_two(lib.get_input(24))))
