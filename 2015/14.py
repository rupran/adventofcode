import sys
import re

cur_dist = {} # Travelled distance
speeds = {}
speed_times_fixed = {}
speed_times_now = {}
rest_times_fixed = {}
rest_times_now = {}

# Part 2
lead_points = {}

inp = [x.rstrip() for x in sys.stdin.readlines()]

def simulate(steps):
    for _ in range(0, steps):
        for deer in speeds.keys():
            if speed_times_now[deer] == 0:
                # Must rest now
                rest_times_now[deer] -= 1
                if rest_times_now[deer] == 0:
                    # If finished resting, restore speed
                    speed_times_now[deer] = speed_times_fixed[deer]
                    rest_times_now[deer] = rest_times_fixed[deer]
                continue
            else:
                # Run one step
                cur_dist[deer] += speeds[deer]
                speed_times_now[deer] -= 1

        # Part 2
        max_val = max(cur_dist.values())
        leaders = [x for x in cur_dist if cur_dist[x] == max_val]
        for l in leaders:
            lead_points[l] += 1

for line in inp:
    matcher = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    if matcher:
        name = matcher.group(1)
        speed = int(matcher.group(2))
        speed_time = int(matcher.group(3))
        rest_time = int(matcher.group(4))

        cur_dist[name] = 0
        speeds[name] = speed
        speed_times_fixed[name] = speed_time
        speed_times_now[name] = speed_time
        rest_times_fixed[name] = rest_time
        rest_times_now[name] = rest_time
        lead_points[name] = 0

simulate(2503)
print "A: " + str(max(cur_dist.values()))
print "B: " + str(max(lead_points.values()))
