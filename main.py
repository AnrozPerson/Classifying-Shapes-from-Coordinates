# Main.py

# Import Matplot library to do visual graph things
# Import numpy for math functions
import matplotlib.pyplot as plt
import numpy as np
import math
from colorama import Fore, Back, Style

# Shape list to store the coords of unkown shape
shape = []

global sides_1
global side2_2

sides_1 = {}
sides_2 = {}

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

###Respective output for each property

prop_1 = {"1_parallel": "One pair of parallel sides", "2_parallel": "Two pairs of parallel sides", "all_sides_equal": "All sides equal", "all_angle_90": "All angles 90 degrees", "2_pair_equal_adjacent_side": "Two pairs of adjacent equal sides"}
prop_2 = {"perpendicular_diagonals": "Diagonals are perpendicular", "1_diagonal_bisect_other": "One diagonal bisects the other", "2_diagonal_bisects_others": "Both diagonals bisect each other", "1_bisect_angle": "One diagonal bisects the angles it passes through", "2_bisect_angles": "Both diagonals bisect the angles they pass through", "diagonals_equal_length": "Diagonals are equal in length"}

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
        comment = "AB, BC, CD and DA are " + str(round(side_length(coord[0], coord[1]), 1))
        sides_1["all_sides_equal"] = comment
        return "all_sides_equal"
    pass
# Find angle should take 3 points and find angle for centre point
# Use the law of cosines
# Find Angle of point_b


def find_angle(point_a, point_b, point_c):
    side_a = side_length(point_a, point_b)
    side_b = side_length(point_b, point_c)
    side_c = side_length(point_c, point_a)
    angle = math.degrees(math.acos((side_a**2 + side_b**2 - side_c**2)/(2*side_b*side_a)))
    return round(float(angle), 2)


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
        sides_1["1_parallel"] = "AB and CD"
        return "1_parallel"
    elif find_gradient(coord[0], coord[3]) == find_gradient(coord[1], coord[2]):
        sides_1["1_parallel"] = "AD and BC"
        return "1_parallel"
    pass


def find_parallel_2(coord):
    if find_gradient(coord[0], coord[1]) == find_gradient(coord[2], coord[3]) and find_gradient(coord[0], coord[3]) == find_gradient(coord[1], coord[2]):
        if "1_parallel" in sides_1:
            if sides_1["1_parallel"] == "AB and CD":
                sides_1["2_parallel"] = "also AD and BC"
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
    side = []
    if adjacent_sides_equal(shape[3], shape[0], shape[1]):
        side.append("AD and AB")
        count += 1
    if adjacent_sides_equal(shape[0], shape[1], shape[2]):
        side.append("AB and BC")
        count += 1
    if adjacent_sides_equal(shape[1], shape[2], shape[3]):
        side.append("BC and CD")
        count += 1
    if adjacent_sides_equal(shape[2], shape[3], shape[0]):
        side.append("CD and AD")
        count += 1
    if count > 1:
        sides_1["2_pair_equal_adjacent_side"] = ", ".join(side)
        return "2_pair_equal_adjacent_side"
    pass


def all_angles_90(coord):
    count = 0
    a = find_all_angles(coord)
    for i in a:
        if round(float(i), 2) == 90.00:
            count += 1
    if count == 4:
        sides_1["all_angle_90"] = "DAB, ABC, BCD, CDA"
        return "all_angle_90"
    pass

####Code for diagonal
def find_diagonal_lengths(coord):
    if side_length(coord[0],coord[2]) == side_length(coord[1],coord[3]):
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
    if count >= 2:
        return "1_diagonal_bisect_other"
    pass

def find_diagonal_angle_bisection(coord):
    a1 = find_angle(coord[2], coord[0], coord[3])
    a2 = find_angle(coord[2], coord[3], coord[1])
    check_1 = 0.5*find_angle(coord[3], coord[2], coord[1])
    check_2 = 0.5*find_angle(coord[0], coord[1], coord[2])
    if a1 == check_1 :
        return "1_bisect_angle"
    if a2 == check_2:
        return "1_bisect_angle"
    pass

def find_2_diagonal_angle_bisection(coord):
    a1 = find_angle(coord[2], coord[0], coord[3])
    a2 = find_angle(coord[2], coord[3], coord[1])
    check_1 = 0.5*find_angle(coord[3], coord[2], coord[1])
    check_2 = 0.5*find_angle(coord[0], coord[1], coord[2])
    if a1 == check_1 and a2 == check_2:
        return "2_bisect_angles"
    pass



def find_perpendicular(coord):
    if find_2_bisection(shape):
        w = find_intersection(coord[1], coord[3])
        if find_angle(coord[1], w, coord[2]) == 90:
            return "perpendicular_diagonals"
        else:
            pass
    if find_2_bisection(shape):
        w = find_intersection(coord[0], coord[2])
        if find_angle(coord[0], w, coord[3]) == 90:
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


def sort_vertices(coord):
    c1 = find_angle(coord[3], coord[0], coord[2])
    c2 = find_angle(coord[1], coord[0], coord[2])
    c3 = find_angle(coord[3], coord[0], coord[1])
    angles = [c1, c2, c3]
    angles.sort()
    angles.reverse()
    print(angles)
    if angles[0] == c1:
        return [coord[0], coord[2], coord[1], coord[3]]
    elif angles[0] ==  c2:
        return [coord[0], coord[1], coord[3], coord[2]]
    elif angles[0] == c3:
        return [coord[0], coord[3], coord[2], coord[1]]
    pass

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

shape = sort_vertices(shape)
print(shape)
if invalid_shape(shape):
    print("Shape Error. Redo.")

print("")

#print(find_angle(shape[3], shape[0], shape[2]))
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

stat_1 = True
print(Fore.RED + "Side and angle properties for " + str(shape[0]) + ", " + str(shape[1]) + ", " + str(shape[2]) + " and " + str(shape[3]) + Style.RESET_ALL)

for i in shape_1:
    print(prop_1[i], 5*" ", Fore.RED + sides_1[i] + Style.RESET_ALL)
for i in shape_check_1:
    if shape_check_1[i] == shape_1:
        print(f"CONCLUSION: The quadrilateral is a {Fore.RED + i.upper()}" + Style.RESET_ALL)
        stat_1 = False
        break
if stat_1:
    print("Unknown Shape")

print("")

if find_perpendicular(shape):
    shape_2.append(find_perpendicular(shape))
if find_1_bisect(shape):
    shape_2.append(find_1_bisect(shape))
if find_2_bisection(shape):
    shape_2.append(find_2_bisection(shape))
if find_diagonal_angle_bisection(shape):
    shape_2.append(find_diagonal_angle_bisection(shape))
if find_2_diagonal_angle_bisection(shape):
    shape_2.append(find_2_diagonal_angle_bisection(shape))
if find_diagonal_lengths(shape):
    shape_2.append(find_diagonal_lengths(shape))

stat_2 = True
print(Fore.RED + "Diagonal properties for " + str(shape[0]) + ", " + str(shape[1]) + ", " + str(shape[2]) + " and " + str(shape[3]) + Style.RESET_ALL)
for i in shape_2:
    print(prop_2[i])
for i in shape_check_2:
    if shape_check_2[i] == shape_2:
        print(f"CONCLUSION: The quadrilateral is a {Fore.RED + i.upper()}" + Style.RESET_ALL)
        stat_2 = False
if stat_2:
    print("Unknown Shape")

