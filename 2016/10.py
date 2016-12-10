#!/usr/bin/env python3

import lib.common as lib
import re

def part_one(line_gen):
    global outputs
    bots = {}
    outputs = {}

    for line in line_gen: # multi line input
        match = re.match(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", line)
        if match:
            bot_no = int(match.group(1))
            low_out = (match.group(2), int(match.group(3)))
            high_out = (match.group(4), int(match.group(5)))

            if not bot_no in bots:
                bots[bot_no] = {"low_out": low_out, "high_out": high_out,
                                "low_val": None, "high_val": None, "inputs": []}
            else:
                bots[bot_no]["low_out"] = low_out
                bots[bot_no]["high_out"] = high_out
                bots[bot_no]["low_val"] = None
                bots[bot_no]["high_val"] = None
            continue
        match = re.match("value (\d+) goes to bot (\d+)", line)
        if match:
            bot_no = int(match.group(2))
            val = int(match.group(1))
            if not bot_no in bots:
                bots[bot_no] = {"inputs": [val]}
            else:
                bots[bot_no]["inputs"].append(val)

    worklist = []
    for bot_no in bots:
        if len(bots[bot_no]["inputs"]) == 2:
            worklist.append(bot_no)

    while worklist:
        cur_bot = bots[worklist.pop(0)]
        max_val = max(cur_bot["inputs"])
        min_val = min(cur_bot["inputs"])
        cur_bot["high_val"] = max_val
        cur_bot["low_val"] = min_val

        low_out_type = cur_bot["low_out"][0]
        low_out_idx = cur_bot["low_out"][1]
        high_out_type = cur_bot["high_out"][0]
        high_out_idx = cur_bot["high_out"][1]

        if low_out_type == "bot":
            bots[low_out_idx]["inputs"].append(min_val)
            if len(bots[low_out_idx]["inputs"]) == 2:
                worklist.append(low_out_idx)
        else:
            outputs[low_out_idx] = min_val

        if high_out_type == "bot":
            bots[high_out_idx]["inputs"].append(max_val)
            if len(bots[high_out_idx]["inputs"]) == 2:
                worklist.append(high_out_idx)
        else:
            outputs[high_out_idx] = max_val

    for bot_no in bots:
        if bots[bot_no]["low_val"] == 17 and bots[bot_no]["high_val"] == 61:
            return bot_no

def part_two(line_gen):
    global outputs
    return outputs[0] * outputs[1] * outputs[2]

print("A: " + str(part_one(lib.get_input(10))))
print("B: " + str(part_two(lib.get_input(10))))
