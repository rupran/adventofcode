import sys
import re
import json
from StringIO import StringIO

global_sum = 0

def evaluate_object(in_obj):
    global global_sum
    if type(in_obj) == dict:
        for key in in_obj.keys():
            if in_obj[key] == "red":
                return
        for key in in_obj.keys():
            evaluate_object(in_obj[key])
    elif type(in_obj) == list:
        for item in in_obj:
            evaluate_object(item)
    elif type(in_obj) == int:
        global_sum += in_obj


inp = [x.strip() for x in sys.stdin.readlines()]
total_sum = 0

for line in inp:
    matcher = re.findall("(-?[0-9]+)", line)
    total_sum += sum(int(x) for x in matcher)

print "A: " + str(total_sum)

js = json.loads(inp[0])
evaluate_object(js)
print "B: " + str(global_sum)
