###Main.py

#Import Matplot library to do visual graph things
#Import numpy for math functions
import matplotlib.pyplot as plt
import numpy as np
import math

###Shape list to store the coords of unkown shape
shape = []

shape_check_1 = {"square": ["1_parallel", "2_parallel,", "all_sides_equal", "all_angle_90", "2_pair_equal_adjacent_side"], 
               "rhombus": ["1_parallel", "2_parallel,", "all_sides_equal", "2_pair_equal_adjacent_side"],
               "rectangle": ["1_parallel", "2_parallel,", "all_angle_90"],
               "parallelogram": ["1_parallel", "2_parallel,"],
               "kite": ["2_pair_equal_adjacent_side"],
               "trapezium": ["1_parallel"]}
shape_check_2 = {"square": ["perpendicular_diagonals", "1_diagonal_bisect_other", "2_diagonal_bisects_others", "1_bisect_angle", "2_bisect_angles", "diagonals_equal_length"],
                 "rhombus": ["perpendicular_diagonals", "1_diagonal_bisect_other", "2_diagonal_bisects_others", "1_bisect_angle", "2_bisect_angles"],
                 "rectangle": ["1_diagonal_bisect_other", "2_diagonal_bisects_others", "diagonals_equal_length"],
                 "parallelogram": ["1_diagonal_bisect_other", "2_diagonal_bisects_others"],
                 "kite": ["perpendicular_diagonals", "1_diagonal_bisect_other", "1_bisect_angle"],
                 "trapezium": []}

###2 lists below for each shape_check respectively
###Each list will slowly be built up as properties are identified

shape_1 = []
shape_2 = []
#a and b will be tuples holding coordinates
def side_length(a, b):
    side_a = a[0] - b[0]
    side_b = a[1] - b[1]
    side_c = math.sqrt(side_a**2 + side_b**2)
    return side_c

###AB, BC, CD and DA are all sides
###shape[0] to shape[1], shape[1] to shape[2] etc.
def all_side_equal(coord):
    if side_length(coord[0], coord[1]) == side_length(coord[1], coord[2]) == side_length(coord[2], coord[3]) == side_length(coord[3], coord[0]):
        return "all_sides_equal"
    pass
###Find angle should take 3 points and find angle for centre point
###Use the law of cosines
###Find Angle of point_b
def find_angle(point_a, point_b, point_c):
    side_a = side_length(point_a, point_b)
    side_b = side_length(point_b, point_c)
    side_c = side_length(point_c, point_a)
    angle = np.degrees(np.arccos((side_a**2 + side_b**2 - side_c**2)/(2*side_b*side_c)))
    return angle

def find_all_angles(coord):
    angles = []
    angles.append(round(5, find_angle(coord[3], coord[0], coord[1])))
    angles.append(round(5, find_angle(coord[0], coord[1], coord[2])))
    angles.append(round(5, find_angle(coord[1], coord[2], coord[3])))
    angles.append(round(5, find_angle(coord[2], coord[3], coord[0])))
    return angles

###Parallel lines will have equal alternate angles
###Current code does not work with trapezium, only parallelograms, rhombuses, squares and rectangles
def find_parallel_1(angle_list):
    if angle_list[0] == angle_list[2]:
        return "1_parallel"
    elif angle_list[1] == angle_list[3]:
        return "1_parallel"
    pass

def find_parallel_2(angle_list):
    if angle_list[0] == angle_list[2] and angle_list[1] == angle_list[3]:
        return "2_parallel"
    pass

###Determine that AB = BC

def adjacent_sides_equal(point_a, point_b, point_c):
    if side_length(point_a, point_b) == side_length(point_a, point_b):
        return True
    pass

###Cycle through all side pairs, if there are 2 side paits equal it will return that
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
        if i == 90.00000:
            count += 1
    if count == 4:
        return "all_angle_90"
    pass


def invalid_input(coord):
    if coord in shape:
        return True




#User Input

### "Empty" Variables, simply to make code more understandable
### Inputs not dusted up for exceptions yet, will fix later
A = shape.append(tuple(map(int, input("Vertex A: ").split(","))))
if invalid_input(A) is True:
    A = shape.append(tuple(map(int, input("Error: Vertex A: ").split(","))))
B = shape.append(tuple(map(int, input("Vertex B: ").split(","))))
if invalid_input(B) is True:
    B = shape.append(tuple(map(int, input("Error: Vertex B: ").split(","))))
C = shape.append(tuple(map(int, input("Vertex C: ").split(","))))
if invalid_input(C) is True:
    C = shape.append(tuple(map(int, input("Error: Vertex C: ").split(","))))
D = shape.append(tuple(map(int, input("Vertex D: ").split(","))))
if invalid_input(D) is True:
    D = shape.append(tuple(map(int, input("Error: Vertex D: ").split(","))))

###Tests

print(find_all_angles(shape))