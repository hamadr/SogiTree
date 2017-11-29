#!/usr/bin/python3

import fileinput

matrix = []

#############
# Read file #
#############
for line in fileinput.input():
    line = line[0:-1]
    matrix.append(list(line))

for i in range(0, 10):
    ####################
    # Grow the trees ! #
    ####################
    for l in range(0, len(matrix)):
        for c in range(0, len(matrix[l])):
            if matrix[l][c] == 't':
                matrix[l][c] = 'T'
            elif matrix[l][c] == 'F':
                matrix[l][c] = 't'
            elif matrix[l][c] == 'f':
                matrix[l][c] = 'F'

#######################
# Write modified file #
#######################
for line in matrix:
    for character in line:
        print(character, end = '')

    print('')
