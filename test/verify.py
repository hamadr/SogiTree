#! /usr/bin/python3

import sys

###############################################################################
# HELPERS
###############################################################################

ELEMENTS="fFtTor- "
TREE_ELEMENTS="fFtTr"

def SUCCESS(msg):
    print("SUCCESS:" + msg)

def FAILED(msg):
    print("FAILED:" + msg)

def create_string_list_from_file(filename):
    rst=[]
    with open(filename) as inputfile:
        for line in inputfile:
            rst.append(line.strip('\n'))
    return rst

def count_elements(tree_file, elements):
    count = 0
    for line in tree_file:
        for c in line:
            if c in elements:
                count = count + 1
    return count

###############################################################################
# TESTS
###############################################################################

def test_size(tree_in, tree_out):
    in_height = len(tree_in)
    in_width = len(tree_in[0])

    if (in_height != len(tree_out)):
        return FAILED("Height changed")

    for line in tree_out:
        if (in_width != len(line)):
            return FAILED("line width modified : \"" + line + "\"")

    return SUCCESS("size")

def test_aliens(tree_in, tree_out):
    for line in tree_out:
        for c in line:
            if c not in ELEMENTS:
                return FAILED("Invalid element : \"" + c + "\"")

    return SUCCESS("Use only valid elements")

def test_desert(tree_in, tree_out):
    green_count_in = count_elements(tree_in, TREE_ELEMENTS)
    green_count_out = count_elements(tree_out, TREE_ELEMENTS)

    if (green_count_in == 0 and green_count_out != 0):
        return FAILED("No tree can grow from the desert")

    return SUCCESS("A desert can't create new trees")

def test_light(tree_in, tree_out):
    above = [True] * len(tree_in[0])
    light = []
    for line in tree_in:
        light_line = []
        for x in range(len(line)):
            rst = above[x] and line[x] not in "o-r"
            light_line.append(rst)
        above = light_line
        light.append(light_line)

    for y in range(len(tree_out)):
        for x in range(len(tree_out[0])):
            if (tree_out[y][x] in "fFtT" and not light[y][x]):
                return FAILED("Sun light is useful for trees you known pos="+str((y,x)) + "e=" +tree_out[y][x])

    return SUCCESS("Trees grow only when sun")

def test_root(tree_in, tree_out):
    for y in range(len(tree_out)):
        for x in range(len(tree_out[0])):
            if (tree_out[y][x] is "r" and tree_in[y][x] not in "r-"):
                return FAILED("Root can't developp without earth pos="+str((y,x)) + "e=" +tree_in[y][x])

    return SUCCESS("Roots grows in ground")

def test_old_trunk(tree_in, tree_out):
    for y in range(len(tree_in)):
        for x in range(len(tree_in[0])):
            if (tree_in[y][x] is "T" and tree_out[y][x] is not "T" ):
                return FAILED("Old trunk can't disapear !")

    return SUCCESS("Nothing like an old tree...")

def test_young_trunk(tree_in, tree_out):
    for y in range(len(tree_in)):
        for x in range(len(tree_in[0])):
            if (tree_in[y][x] is "t" and tree_out[y][x] not in "tT" ):
                return FAILED("young trunk can only become old")

    return SUCCESS("You have to care about ")

def test_ground_solidity(tree_in, tree_out):
    for y in range(len(tree_in)):
        for x in range(len(tree_in[0])):
            if (tree_in[y][x] is "-" and tree_out[y][x] not in "-r" ):
                return FAILED("Missing earth")

    for y in range(len(tree_in)):
        for x in range(len(tree_in[0])):
            if (tree_in[y][x] is "o" and tree_out[y][x] is not "o" ):
                return FAILED("Stop stealing my stones !")

    for y in range(len(tree_out)):
        for x in range(len(tree_out[0])):
            if (tree_out[y][x] in "o-" and tree_out[y][x] is not tree_in[y][x] ):
                return FAILED("You cant create ground from thin air !")

    return SUCCESS("Earth looks normal, boring like dirt")

###############################################################################
# MAIN
###############################################################################

def main():
    tree_in = create_string_list_from_file(sys.argv[1])
    tree_out = create_string_list_from_file(sys.argv[2])

    test_size(tree_in, tree_out)
    test_aliens(tree_in, tree_out)
    test_desert(tree_in, tree_out)
    test_light(tree_in, tree_out)
    test_root(tree_in, tree_out)
    test_old_trunk(tree_in, tree_out)
    test_young_trunk(tree_in, tree_out)
    test_ground_solidity(tree_in, tree_out)

main()
