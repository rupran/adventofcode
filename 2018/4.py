#!/usr/bin/env python3

import collections
import re
import lib.common as lib

def get_sleep_times(line_gen):
    s = sorted(line_gen)
    sleep_times = collections.defaultdict(list)
    cur_guard = -1
    start_min = -1
    for line in s:
        m = re.match(r'.*Guard #(\d+).*', line)
        if m:
            cur_guard = int(m.group(1))
            continue
        m = re.match(r'\[\d{4}-\d{2}-\d{2} 00:(\d{2})\] falls asleep', line)
        if m:
            start_min = int(m.group(1))
            continue
        m = re.match(r'\[\d{4}-\d{2}-\d{2} 00:(\d{2})\] wakes up', line)
        if m:
            sleep_times[cur_guard].append((start_min, int(m.group(1))))
    return sleep_times

def part_one(line_gen):
    sleep_times = get_sleep_times(line_gen)
    most_sleepy = sorted(sleep_times.items(),
                         key=lambda x: (-sum(b - a for a, b in x[1]), x[0]))[0][0]

    # Find the minute where most_sleepy was asleep most often
    max_minute = max((minute for minute in range(60)),
                     key=lambda m: sum(int(m in range(start, end)) for (start, end) in sleep_times[most_sleepy]))
    return most_sleepy * max_minute 
    

def part_two(line_gen):
    sleep_times = get_sleep_times(line_gen)
    guard_id, (max_minute, _) = max(((guard,        # Save the guard id for result calculation
                                      max(((minute, # Save the minute for result calculation
                                            sum(int(minute in range(start, end)) for (start, end) in times) # Calculate number of sleeps for the iterated minute
                                           ) for minute in range(60)), # Iterate over all minutes (inner loop)
                                          key=lambda x:x[1]            # max needs to find the maximum of slept minutes
                                         )
                                     ) for guard, times in sleep_times.items()),  # Iterate over guards and times (outer loop)
                                    key=lambda x: x[1][1]) # Compare guards by maximum overlapping number
    return guard_id * max_minute

print("A: " + str(part_one(lib.get_input(4))))
print("B: " + str(part_two(lib.get_input(4))))
