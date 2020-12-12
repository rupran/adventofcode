#!/usr/bin/env python3

import lib.common as lib

def calc_waypoint_rotation(x, y, direction, degrees):
    if direction == 'R':
        degrees = 360 - degrees 
    if degrees == 90:
        waypoint_pos = (y, -x)
    elif degrees == 180:
        waypoint_pos = (-x, -y)
    elif degrees == 270:
        waypoint_pos = (-y, x)
    return waypoint_pos

def run_instructions(directions, part_two=False):
    pos = (0, 0)
    waypoint_pos = (10, -1)
    rot_idx = 0
    orientations = [(1,0), (0, 1), (-1, 0), (0, -1)]
    movements = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    for direction in directions:
        if direction[0] in movements.keys():
            steps = direction[1]
            delta_x, delta_y = movements[direction[0]]
            if part_two:
                waypoint_pos = (waypoint_pos[0] + steps * delta_x,
                                waypoint_pos[1] + steps * delta_y)        
            else:
                pos = (pos[0] + steps * delta_x, pos[1] + steps * delta_y)
        elif direction[0] == 'L':
            if part_two:
                waypoint_pos = calc_waypoint_rotation(*waypoint_pos, *direction)
            else:
                rot_idx = (rot_idx - (direction[1] // 90)) % 4
        elif direction[0] == 'R':
            if part_two:
                waypoint_pos = calc_waypoint_rotation(*waypoint_pos, *direction)
            else:
                rot_idx = (rot_idx + (direction[1] // 90)) % 4
        elif direction[0] == 'F':
            steps = direction[1]
            if part_two:
                delta_x, delta_y = waypoint_pos
            else:
                delta_x, delta_y = orientations[rot_idx]
            pos = (pos[0] + steps * delta_x, pos[1] + steps * delta_y)
    return abs(pos[0]) + abs(pos[1]) 

def part_one(line_gen):
    instructions = [(line[0], int(line[1:])) for line in line_gen]
    return run_instructions(instructions)

def part_two(line_gen):
    instructions = [(line[0], int(line[1:])) for line in line_gen]
    return run_instructions(instructions, part_two=True)

print("A: " + str(part_one(lib.get_input(12))))
print("B: " + str(part_two(lib.get_input(12))))
