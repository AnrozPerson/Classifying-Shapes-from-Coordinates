# Main.py

# Import Matplot library to do visual graph things
# Import numpy for math functions
import matplotlib.pyplot as plt
import numpy as np
import math

# Shape list to store the coords of unkown shape
shape = []

global sides

shape_check_1 = {"square": ["1_parallel", "2_parallel", "all_sides_equal", "all_angle_90", "2_pair_equal_adjacent_side"],
                 "rhombus": ["1_parallel", "2_parallel", "all_sides_equal", "2_pair_equal_adjacent_side"],
                 "rectangle": ["1_parallel", "2_parallel", "all_angle_90"],
                 "parallelogram": ["1_parallel", "2_parallel"],
                 "kite": ["2_pair_equal_adjacent_side"],
                 "trapezium": ["1_parallel"]}
shape_check_2 = {"square": ["perpendicular_diagonals", "1_diagonal_bisect_other", "2_diagonal_bisects_others", "1_bisect_angle", "2_bisect_angles", "diagonals_equal_length"],
                 "rhombus": ["perpendicular_diagonals", "1_diagonal_bisect_other", "2_diagonal_bisects_others", "1_bisect_angle", "2_bisect_angles"],
                 "rectangle": ["1_diagonal_bisect_other", "2_diagonal_bisects_others", "diagonals_equal_length"],
                 "parallelogram": ["1_diagonal_bisect_other", "2_diagonal_bisects_others"],
                 "kite": ["perpendicular_diagonals", "1_diagonal_bisect_other", "1_bisect_angle"],
                 "trapezium": []}

# 2 lists below for each shape_check respectively
# Each list will slowly be built up as properties are identified

shape_1 = []
shape_2 = []
# a and b will be tuples holding coordinates


def side_length(a, b):
    side_a = a[0] - b[0]
    side_b = a[1] - b[1]
    side_c = math.sqrt(side_a**2 + side_b**2)
    return side_c

# AB, BC, CD and DA are all sides
# shape[0] to shape[1], shape[1] to shape[2] etc.


def all_side_equal(coord):
    if side_length(coord[0], coord[1]) == side_length(coord[1], coord[2]) == side_length(coord[2], coord[3]) == side_length(coord[3], coord[0]):
        return "all_sides_equal"
    pass
# Find angle should take 3 points and find angle for centre point
# Use the law of cosines
# Find Angle of point_b


def find_angle(point_a, point_b, point_c):
    side_a = side_length(point_a, point_b)
    side_b = side_length(point_b, point_c)
    side_c = side_length(point_c, point_a)
    angle = np.degrees(np.arccos((side_a**2 + side_b**2 - side_c**2)/(2*side_b*side_c)))
    return angle


def find_all_angles(coord):
    angles = []
    angles.append(find_angle(coord[3], coord[0], coord[1]))
    angles.append(find_angle(coord[0], coord[1], coord[2]))
    angles.append(find_angle(coord[1], coord[2], coord[3]))
    angles.append(find_angle(coord[2], coord[3], coord[0]))
    return angles


def find_gradient(point_a, point_b):
    try:
        m = (float(point_a[1])-float(point_b[1]))/(float(point_a[0])-float(point_b[0]))
    except:
        m = "up"
    return m
# Parallel lines have same GRADIENT!
# Current code does not work with trapezium, only parallelograms, rhombuses, squares and rectangles


def find_parallel_1(coord):
    if find_gradient(coord[0], coord[1]) == find_gradient(coord[2], coord[3]):
        return "1_parallel"
    elif find_gradient(coord[0], coord[3]) == find_gradient(coord[1], coord[2]):
        return "1_parallel"
    pass


def find_parallel_2(coord):
    if find_gradient(coord[0], coord[1]) == find_gradient(coord[2], coord[3]) and find_gradient(coord[0], coord[3]) == find_gradient(coord[1], coord[2]):
        return "2_parallel"
    pass

# Determine that AB = BC


def adjacent_sides_equal(point_a, point_b, point_c):
    if side_length(point_a, point_b) == side_length(point_b, point_c):
        return True
    pass

# Cycle through all side pairs, if there are 2 side paits equal it will return that


def adjacent_sides_equal_2(shape):
    count = 0
    if adjacent_sides_equal(shape[3], shape[0], shape[1]):
        count += 1
    if adjacent_sides_equal(shape[0], shape[1], shape[2]):
        count += 1
    if adjacent_sides_equal(shape[1], shape[2], shape[3]):
        count += 1
    if adjacent_sides_equal(shape[2], shape[3], shape[0]):
        count += 1
    if count > 1:
        return "2_pair_equal_adjacent_side"
    pass


def all_angles_90(coord):
    count = 0
    a = find_all_angles(coord)
    for i in a:
        if round(float(i), 2) == 90.00:
            count += 1
    if count == 4:
        return "all_angle_90"
    pass

####Code for diagonal
def find_diagonal_lengths(coord):
    if side_length(coord[0],coord[2]) == side_length(coord[1],coord[2]):
        return "diagonals_equal_length"
    pass

###Find midpoint of a segment through "averaging" the points
###(x1 + x2)/(y1+y2), do for both diagonals, if they are both the same, then both intersect
def find_intersection(point_a, point_b):
    x = (point_a[0] + point_b[0])/2
    y = (point_a[1] + point_b[1])/2
    return (x,y)

def find_2_bisection(coord):
    bisect_1 = find_intersection(coord[0], coord[2])
    bisect_2 = find_intersection(coord[1], coord[3])
    if bisect_2 == bisect_1:
        return "2_diagonal_bisects_others"
    pass

###If a line bisects another line, the point of intersection and a corner of reference should have the same gradient as the original diagonal
###Find gradient of diagonal, then gradient of smaller "line" -> challenge of finding whether midpoint of segment actually lies on the other line.
def find_1_bisect(coord):
    ###Check for first line
    count = 0
    half_1 = find_intersection(coord[0], coord[2])
    half_2 = find_intersection(coord[1], coord[3])
    if find_gradient(half_1, coord[3]) == find_gradient(coord[1], coord[3]):
        count += 1
    if find_gradient(half_2, coord[2]) == find_gradient(coord[0], coord[2]):
        count += 1
    if count > 2:
        return "1_diagonal_bisect_other"
    pass

def find_diagonal_angle_bisection(coord):
    a1 = find_angle(coord[2], coord[0], coord[3])
    a2 = find_angle(coord[0], coord[1], coord[3])
    check_1 = 0.5*find_angle(coord[1], coord[0], coord[3])
    check_2 = 0.5*find_angle(coord[0], coord[1], coord[2])
    if a1 == check_1 :
        return "1_bisect_angle"
    if a2 == check_2:
        return "1_bisect_angle"
    pass

def find_2_diagonal_angle_bisection(coord):
    a1 = find_angle(coord[2], coord[0], coord[3])
    a2 = find_angle(coord[0], coord[1], coord[3])
    check_1 = 0.5*find_angle(coord[1], coord[0], coord[3])
    check_2 = 0.5*find_angle(coord[0], coord[1], coord[2])
    if a1 == check_1 and a2 == check_2:
        return "2_bisect_angles"
    pass



def find_perpendicular(coord):
    if find_1_bisect(shape):
        w = find_intersection(coord[1], coord[3])
        if find_angle(coord[1], w, coord[2]) == 90:
            return "perpendicular_diagonals"
        else:
            pass
    pass

def invalid_input(coord):
    if coord in shape:
        return True
    return False


# Invalid Shape check


def invalid_shape(coord):
    try:
        find_angle(coord[3], coord[0], coord[1])
        find_angle(coord[0], coord[1], coord[2])
        find_angle(coord[1], coord[2], coord[3])
        find_angle(coord[2], coord[3], coord[0])
    except:
        return True
    return False


# User Input

shape = []
try:
    A = tuple(map(int, input("Vertex A: ").split(",")))
except:
    A = tuple(map(int, input("Error: Vertex A: ").split(",")))
while invalid_input(A) is True:
    A = tuple(map(int, input("Error: Vertex A: ").split(",")))
shape.append(A)
try:
    B = tuple(map(int, input("Vertex B: ").split(",")))
except:
    A = tuple(map(int, input("Error: Vertex A: ").split(",")))
while invalid_input(B) is True:
    B = tuple(map(int, input("Error: Vertex B: ").split(",")))
    invalid_input(B)
shape.append(B)
try:
    C = tuple(map(int, input("Vertex C: ").split(",")))
except:
    C = tuple(map(int, input("Error: Vertex C: ").split(",")))
while invalid_input(C) is True:
    C = tuple(map(int, input("Error: Vertex C: ").split(",")))
    invalid_input(C)
shape.append(C)
try:
    D = tuple(map(int, input("Vertex D: ").split(",")))
except:
    D = tuple(map(int, input("Error: Vertex D: ").split(",")))
while invalid_input(D) is True:
    D = tuple(map(int, input("Error: Vertex D: ").split(",")))
    invalid_input(D)
shape.append(D)
if invalid_shape(shape):
    print("Shape Error. Redo.")


# Test for check 1
if find_parallel_1(shape):
    shape_1.append(find_parallel_1(shape))
if find_parallel_2(shape):
    shape_1.append(find_parallel_2(shape))
if all_side_equal(shape):
    shape_1.append(all_side_equal(shape))
if all_angles_90(shape):
    shape_1.append(all_angles_90(shape))
if adjacent_sides_equal_2(shape):
    shape_1.append(adjacent_sides_equal_2(shape))

for i in shape_1:
    print(i)
for i in shape_check_1:
    if shape_check_1[i] == shape_1:
        print(i)
        break