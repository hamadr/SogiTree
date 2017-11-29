#!/usr/bin/python3

import fileinput
import random

matrix = []

#############
# Read file #
#############
for line in fileinput.input():
    line = line[0:-1]
    matrix.append(list(line))

####################
# Grow the trees ! #
####################
for l in range(1, len(matrix)-2):
    for c in range(1, len(matrix[l])-1):
        if matrix[l][c] == 'r':
            # Grow the root
            # R : new leaf
            growing_chance = 0.15
            n_of_new = 0
            n_of_new_allowed = 1
            if matrix[l+1][c-1] == '-':
                if random.random() < growing_chance - 0.1:
                    matrix[l+1][c-1] = 'R'
                    n_of_new += 1
            if matrix[l+1][c] == '-':
                if random.random() < growing_chance - 0.1:
                    matrix[l+1][c] = 'R'
                    n_of_new += 1
            if matrix[l+1][c+1] == '-' and n_of_new < n_of_new_allowed:
                if random.random() < growing_chance - 0.1:
                    matrix[l+1][c+1] = 'R'
                    n_of_new += 1
            if matrix[l][c-1] == '-' and n_of_new < n_of_new_allowed:
                if random.random() < growing_chance - 0.0:
                    matrix[l][c-1] = 'R'
                    n_of_new += 1
            if matrix[l][c+1] == '-' and n_of_new < n_of_new_allowed:
                if random.random() < growing_chance - 0.0:
                    matrix[l][c+1] = 'R'
                    n_of_new += 1

        elif matrix[l][c] == 'T':
            if random.random() < 0.07:
                # N : new trunc
                if matrix[l][c-1] == ' ':
                    matrix[l][c-1] = 'N'
                if matrix[l][c+1] == ' ':
                    matrix[l][c+1] = 'N'

        elif matrix[l][c] == 't':
            if random.random() < 0.15:
                matrix[l][c] = 'T'

        elif matrix[l][c] == 'F':
            if random.random() < 0.2:
                matrix[l][c] = 't'

        elif matrix[l][c] == 'f':
            if random.random() < 0.3:
                matrix[l][c] = 'F'

            # Grow the tree around the leaf
            # n : new leaf
            growing_chance = 0.3
            n_of_new = 0
            n_of_new_allowed = 2
            if matrix[l-1][c-1] == ' ':
                if random.random() < growing_chance:
                    matrix[l-1][c-1] = 'n'
                    n_of_new += 1
            if matrix[l-1][c] == ' ':
                if random.random() < growing_chance:
                    matrix[l-1][c] = 'n'
                    n_of_new += 1
            if matrix[l-1][c+1] == ' ' and n_of_new < n_of_new_allowed:
                if random.random() < growing_chance:
                    matrix[l-1][c+1] = 'n'
                    n_of_new += 1
            if matrix[l][c-1] == ' ' and n_of_new < n_of_new_allowed:
                if random.random() < growing_chance - 0.1:
                    matrix[l][c-1] = 'n'
                    n_of_new += 1
            if matrix[l][c+1] == ' ' and n_of_new < n_of_new_allowed:
                if random.random() < growing_chance - 0.1:
                    matrix[l][c+1] = 'n'
                    n_of_new += 1
            #if matrix[l+1][c-1] == ' ' and n_of_new < n_of_new_allowed:
            #    if random.random() < growing_chance - 0.2:
            #        matrix[l+1][c-1] = 'n'
            #        n_of_new += 1
            #if matrix[l+1][c] == ' ' and n_of_new < n_of_new_allowed:
            #    if random.random() < growing_chance - 0.2:
            #        matrix[l+1][c] = 'n'
            #        n_of_new += 1
            #if matrix[l+1][c+1] == ' ' and n_of_new < n_of_new_allowed:
            #    if random.random() < growing_chance - 0.2:
            #        matrix[l+1][c+1] = 'n'

# Replace the new leaf (n) by leaf (f) and the new trunc (N) by trunc (T) and the new root "R"
for l in range(1, len(matrix)-1):
    for c in range(1, len(matrix[l])-1):
        if matrix[l][c] == 'n':
            matrix[l][c] = 'f'
        elif matrix[l][c] == 'N':
            matrix[l][c] = 'T'
        elif matrix[l][c] == 'R':
            matrix[l][c] = 'r'

#######################
# Write modified file #
#######################
for line in matrix:
    for character in line:
        print(character, end = '')

    print('')
