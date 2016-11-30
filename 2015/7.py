import sys
import re

wire_values = {}

def simulate():
    changed = True
    while changed:
        changed = False

        for gate in gates:
            if gate.can_have_signal():
                changed = changed | gate.calc_output()


class Gate:
    def __init__(self, g_type, in_1, in_2, out):
        self.g_type = g_type
        if self.g_type.startswith("RSHIFT "):
            self.shiftwidth = int(g_type[len("RSHIFT "):])
            self.g_type = "RSHIFT"
        elif self.g_type.startswith("LSHIFT "):
            self.shiftwidth = int(g_type[len("LSHIFT "):])
            self.g_type = "LSHIFT"
        self.in_1 = in_1
        self.in_2 = in_2
        self.out = out

    def calc_output(self):
        retval = 0
        if self.g_type == "RSHIFT":
            retval = (wire_values[self.in_1] >> self.shiftwidth) & 0xffff
        elif self.g_type == "LSHIFT":
            retval = (wire_values[self.in_1] << self.shiftwidth) & 0xffff
        elif self.g_type == "AND":
            retval = (wire_values[self.in_1] & wire_values[self.in_2]) & 0xffff
        elif self.g_type == "OR":
            retval = (wire_values[self.in_1] | wire_values[self.in_2]) & 0xffff
        elif self.g_type == "NOT":
            retval = (~wire_values[self.in_1]) & 0xffff
        elif self.g_type == "WIRE":
            retval = wire_values[self.in_1] & 0xffff

        if self.out in wire_values and wire_values[self.out] == retval:
            return False
        
        wire_values[self.out] = retval
        return True

    def can_have_signal(self):
        if self.in_2:
            return self.in_1 in wire_values and self.in_2 in wire_values
        else:
            return self.in_1 in wire_values

    def __str__(self):
        retval = "Gate(%s, %s, %s, %s" % (self.g_type, self.in_1, self.in_2, self.out)
        if "SHIFT" in self.g_type:
            retval += ", %s" % self.shiftwidth
        retval += ")"
        return retval

inp = [x.rstrip('\n') for x in sys.stdin.readlines()]

gates = set()

for line in inp:
    in_2_wire = None
    matcher = re.match("([a-z0-9]+) (AND|OR) ([a-z]+) -> ([a-z]+)", line)
    if matcher:
        g_type = matcher.group(2)
        in_1_wire = matcher.group(1)
        in_2_wire = matcher.group(3)
        out_wire = matcher.group(4)
        if re.match("[0-9]+", in_1_wire):
            wire_values[in_1_wire] = int(in_1_wire)
        gates.add(Gate(g_type, in_1_wire, in_2_wire, out_wire))
        continue

    matcher = re.match("([a-z]+) (LSHIFT|RSHIFT) ([0-9]+) -> ([a-z]+)", line)
    if matcher:
        g_type = matcher.group(2) + " " + matcher.group(3)
        in_1_wire = matcher.group(1)
        out_wire = matcher.group(4)
        gates.add(Gate(g_type, in_1_wire, None, out_wire))
        continue

    matcher = re.match("NOT ([a-z]+) -> ([a-z]+)", line)
    if matcher:
        in_1_wire = matcher.group(1)
        out_wire = matcher.group(2)
        gates.add(Gate("NOT", in_1_wire, None, out_wire))
        continue

    matcher = re.match("([a-z]+) -> ([a-z]+)", line)
    if matcher:
        in_1_wire = matcher.group(1)
        out_wire = matcher.group(2)
        gates.add(Gate("WIRE", in_1_wire, None, out_wire))
        continue
   
    matcher = re.match("([0-9]+) -> ([a-z]+)", line)
    if matcher:
        wire_values[matcher.group(2)] = int(matcher.group(1))
        continue

starting_wires = wire_values.copy()

simulate()
retval = wire_values['a']
print "Answer 1: " + str(retval)

wire_values = starting_wires
wire_values['b'] = retval
simulate()
print "Answer 2: " + str(wire_values['a'])
