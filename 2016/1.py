import re
import sys

with open(sys.argv[1], "r") as infile:
    for line in infile:
        instrs = re.split(", ", line.strip())
        # X, Y -> positive means up/north and right/east
        loc = [0, 0]
        directions = ['north', 'east', 'south', 'west']
        cur_dir_ind = 0

        # Location tracking for part B
        visited = set()
        visited.add((0, 0))
        first_twice = None

        # Go the path
        for instr in instrs:
            match = re.match("([LR])([0-9]+)", instr)
            turn_dir = match.group(1)
            steps = int(match.group(2))
            if turn_dir == 'L':
                cur_dir_ind = (cur_dir_ind - 1) % len(directions)
            else:
                cur_dir_ind = (cur_dir_ind + 1) % len(directions)

            for _ in range(0, steps):
                if directions[cur_dir_ind] == 'north':
                    loc = [loc[0] + 1, loc[1]]
                elif directions[cur_dir_ind] == 'east':
                    loc = [loc[0], loc[1] + 1]
                elif directions[cur_dir_ind] == 'south':
                    loc = [loc[0] - 1, loc[1]]
                elif directions[cur_dir_ind] == 'west':
                    loc = [loc[0], loc[1] - 1]

                if not first_twice:
                    if (loc[0], loc[1]) in visited:
                        first_twice = loc
                    else:
                        visited.add((loc[0], loc[1]))
                

        print "A: " + str(sum(abs(x) for x in loc))
        print "B: " + str(sum(abs(x) for x in first_twice))
