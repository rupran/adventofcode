""" Commonly used functionality for Advent of Code """

import os
import sys

def find_filename(puzzle_num, folder, prefix):
    """ Find the filename for a given @puzzle_num. @prefix determines
        the basename of the file in the subfolder @folder. The result
        is a string of the format "@folder/@prefix_@puzzle_num. If the
        user specified in input file as sys.argv[1], then that file is
        used."""
    if puzzle_num != -1 and len(sys.argv) == 1:
        infile = folder + '/' + prefix + '_' + str(puzzle_num)
        if not os.path.exists(infile):
            print("Error: {0} does not exist!".format(infile), file=sys.stderr)
            sys.exit(1)
    elif len(sys.argv) == 1:
        print("Error: No argument, but no sys.argv[1]?", file=sys.stderr)
        sys.exit(1)
    else:
        infile = sys.argv[1]
    return infile

def get_input(puzzle_num=-1, folder="inputs", prefix="input", strip=True):
    """ Get the input lines for the puzzle @puzzle_num. Optionally,
        the folder to look in can be specified as @folder (default:
        "inputs") and the prefix for the searched file as @prefix
        (default: "input"). Note that the lines returned are already
        stripped of whitespaces."""
    infile = find_filename(puzzle_num, folder, prefix)
    with open(infile, 'r') as input_file:
        yield from (line.strip() if strip else line for line in input_file)

def get_sample_input(puzzle_num=-1, folder="inputs", strip=True):
    """ Get the sample input for the puzzle @puzzle_num. Optionally,
        the folder to look in can be specified as @folder (default:
        "inputs") and the prefix for the searched file as @prefix
        (default: "input")."""
    yield from get_input(puzzle_num, folder, prefix="sample", strip=strip)
