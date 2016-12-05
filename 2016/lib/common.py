""" Commonly used functionality for Advent of Code """

import os
import sys

def find_filename(puzzle_num, folder, prefix):
    """ Find the filename for a given @puzzle_num. @prefix determines
        the basename of the file in the subfolder @folder. The result
        is a string of the format "@folder/@prefix_@puzzle_num. If the
        user specified in input file as sys.argv[1], then that file is
        used."""
    if len(sys.argv) == 1:
        infile = folder + '/' + prefix + '_' + str(puzzle_num)
        if not os.path.exists(infile):
            print "Error: %s does not exist!" % infile
            sys.exit(1)
    else:
        infile = sys.argv[1]
    return infile

def get_input(puzzle_num, folder="inputs", prefix="input"):
    """ Get the input for the puzzle @puzzle_num. Optionally, the
        folder to look in can be specified as @folder (default:
        "inputs") and the prefix for the searched file as @prefix
        (default: "input")."""
    infile = find_filename(puzzle_num, folder, prefix)
    with open(infile, 'r') as input_file:
        for line in input_file:
            yield line.strip()

def get_sample_input(puzzle_num, folder="inputs"):
    """ Get the sample input for the puzzle @puzzle_num. Optionally,
        the folder to look in can be specified as @folder (default:
        "inputs") and the prefix for the searched file as @prefix
        (default: "input")."""
    for line in get_input(puzzle_num, folder, prefix="sample"):
        yield line
