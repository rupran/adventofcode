import sys

def count_characters(string):
    chars = [c for c in string[1:len(string)-1]]
    index = 0
    escaped = 0
    while index < len(chars):
        if chars[index] == "\\":
            index += 1
            if chars[index] == "\\" or chars[index] == "\"":
                escaped += 1
            elif chars[index] == "x":
                index += 2
                escaped += 1
        else:
            escaped += 1
        index += 1
    return (len(string), escaped)

def encode_characters(string):
    chars = [c for c in string]
    out_num = 2 # surrounding quotes
    for char in chars:
        if char == "\"" or char == "\\":
            out_num += 1 # escape char
        out_num += 1 # regular char
    return out_num
        
inp = [x.rstrip('\n') for x in sys.stdin.readlines()]

number_of_code = 0
number_in_memory = 0
encoded_chars = 0

for line in inp:
    this_code, this_memory = count_characters(line)
    number_of_code += this_code
    number_in_memory += this_memory

for line in inp:
    encoded_chars += encode_characters(line)

print "A: " + str(number_of_code - number_in_memory)
print "B: " + str(encoded_chars - number_of_code)
