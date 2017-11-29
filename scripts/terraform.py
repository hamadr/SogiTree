#!/bin/env python3

import random
import sys

width = 640
height = 480
sky_height = height - 100

def base_world():
    world = [ [ '-' for w in range(width) ] for h in range(height) ]
    for h in range(sky_height):
        world[h] = [ ' ' for w in range(width) ]
    return world

def living_tree(box_width, box_height, roots_height):
    trunk_height = (box_height - roots_height) / 3
    leaves_height = box_height - roots_height - trunk_height

    trunk_width = int(box_width / 2);
    trunk_w_start = int((box_width - trunk_width) / 2)

    tree = [ [ ' ' for w in range(box_width) ] for h in range(box_height) ]

    for h in range(box_height - roots_height):
        for w in range(trunk_w_start, trunk_width):
            tree[h][w] = 't'

    for h in range(box_height - roots_height, box_height):
        for w in range(box_width):
            tree[h][w] = '-'
        for w in range(trunk_w_start, trunk_width):
            tree[h][w] = 'T' # r doesnt work, T is also dark brown

    for h in range(random.randint(50, box_height - roots_height)):
        for w in range(box_width):
            tree[h][w] = 'f'

    return tree

def dead_tree(box_width, box_height):
    tree = [ [ 'T' for w in range(box_width) ] for h in range(box_height) ]
    return tree

def rock(box_width, box_height):
    rock = [ [ 'o' for w in range(box_width) ] for h in range(box_height) ]
    return rock

def put_object(world, origin_h, origin_w, obj):
    height = len(obj)
    width = len(obj[0])

    #print('putting object [%s %s]' % (height, width))
    #print('starting at [%s %s]' % (origin_h, origin_w))
    for h in range(height):
        for w in range(width):
            #print('Putting at [%s %s]' % (origin_h - h, origin_w - w))
            #print('From [%s %s]' % (height - h - 1, width - w - 1))
            #print(obj)
            world[origin_h - h][origin_w - w] = obj[height - h - 1][width - w - 1]
    return world

def print_world(world):
    for h in range(height):
        for w in range(width):
            print(world[h][w], end='')
        print('\n', end='')

def randomize_world(world):
    plant_head = 0
    for x in range(width - 3):
        obj_type = random.randint(1, 11)
        next_space = random.randint(10, 50)

        plant_line = sky_height - 1
        if 1 <= obj_type <= 3 :
            obj_width = random.randint(20, 100)
            obj_height = random.randint(20, 40)
            obj = rock(obj_width, obj_height)
        elif 4 <= obj_type <= 5:
            obj_width = random.randint(3, 5)
            obj_height = random.randint(3, int(sky_height / 2))
            obj = dead_tree(obj_width, obj_height)
        else:
            roots_height = random.randint(5, height - sky_height - 20)
            obj_width = random.randint(30, 40)
            obj_height = random.randint(3, sky_height - 50) + roots_height
            plant_line += roots_height
            obj = living_tree(obj_width, obj_height, roots_height)

        world = put_object(world, plant_line, plant_head, obj)
        plant_head += obj_width + next_space

        if plant_head > width - next_space:
            break
    return world

world = base_world()
world = randomize_world(world)
print_world(world)
