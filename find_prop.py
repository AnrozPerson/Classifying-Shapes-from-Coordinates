import numpy as np

global sides_1
global sides_2

sides_1 = {}
sides_2 = {}

shape = []

def side_length(a, b):
    side_a = a[0] - b[0]
    side_b = a[1] - b[1]
    side_c = np.sqrt(side_a**2 + side_b**2)
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
    angle = np.degrees(np.arccos((side_a**2 + side_b**2 - side_c**2)/(2*side_b*side_a)))
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
        comment = "AC and BD are " + str(round(side_length(coord[1],coord[3]), 1))
        sides_2["diagonals_equal_length"] = comment
        return "diagonals_equal_length"
    pass

###Find midpoint of a segment through "averaging" the points
###(x1 + x2)/2, (y1+y2)/2, do for both diagonals, if they are both the same, then both intersect
def find_intersection(point_a, point_b):
    x = (point_a[0] + point_b[0])/2
    y = (point_a[1] + point_b[1])/2
    return (x,y)

def find_2_bisection(coord):
    bisect_1 = find_intersection(coord[0], coord[2])
    bisect_2 = find_intersection(coord[1], coord[3])
    if bisect_2 == bisect_1:
        sides_2["2_diagonal_bisects_others"] = "AC and BD both bisect each other"
        return "2_diagonal_bisects_others"
    pass

###If a line bisects another line, the point of intersection and a corner of reference should have the same gradient as the original diagonal
###Find gradient of diagonal, then gradient of smaller "line" -> challenge of finding whether midpoint of segment actually lies on the other line.
def find_1_bisect(coord):
    ###Check for first line
    side = []
    count = 0
    half_1 = find_intersection(coord[0], coord[2])
    half_2 = find_intersection(coord[1], coord[3])
    if find_gradient(half_1, coord[3]) == find_gradient(coord[1], coord[3]):
        sides_2["1_diagonal_bisect_other"] = "AC bisects BD"
        count += 1
    elif find_gradient(half_2, coord[2]) == find_gradient(coord[0], coord[2]):
        sides_2["1_diagonal_bisect_other"] = "BD bisects AC"
        count += 1
    if count >= 1:

        return "1_diagonal_bisect_other"
    pass

def find_diagonal_angle_bisection(coord):
    count = 0
    side = ""
    a1 = find_angle(coord[2], coord[0], coord[3])
    a2 = find_angle(coord[2], coord[3], coord[1])
    a3 = find_angle(coord[1], coord[2], coord[0])
    a4 = find_angle(coord[0], coord[1], coord[3])
    check_1 = 0.5*find_angle(coord[1], coord[0], coord[3])
    check_2 = 0.5*find_angle(coord[2], coord[3], coord[0])
    check_3 = 0.5*find_angle(coord[1], coord[2], coord[3])
    check_4 = 0.5*find_angle(coord[0], coord[1], coord[2])
    if round(a1, 2) == round(check_1, 2) and round(a3, 2) == round(check_3, 2):
        count += 1 
        side = "A"
    if round(a2, 2) == round(check_2, 2) and round(a4, 2) == round(check_4, 2):
        count += 1
        side = "B"
    if count == 1:
        if side == "A":
            sides_2["1_bisect_angle"] = "AC"
            return "1_bisect_angle"
        elif side == "B":
            sides_2["1_bisect_angle"] = "BD"
            return "1_bisect_angle"
    elif count == 2:
        sides_2["1_bisect_angle"] = "AC and BD"
        return "1_bisect_angle"

def find_2_diagonal_angle_bisection(coord):
    a1 = find_angle(coord[2], coord[0], coord[3])
    a2 = find_angle(coord[2], coord[3], coord[1])
    check_1 = 0.5*find_angle(coord[3], coord[2], coord[1])
    check_2 = 0.5*find_angle(coord[0], coord[1], coord[2])
    if a1 == check_1 and a2 == check_2:
        sides_2["2_bisect_angles"] = "AC and BD"
        return "2_bisect_angles"
    pass



def find_perpendicular(coord):
    m1 = find_gradient(coord[1], coord[3])
    m2 = find_gradient(coord[0], coord[2])
    if m1 == "up" or m2 == "up" and m1 == 0 or m2 == 0:
        sides_2["perpendicular_diagonals"] = "AC and BD are perpendicular"
        return "perpendicular_diagonals"
    elif m1*m2 == -1:
        sides_2["perpendicular_diagonals"] = "AC and BD are perpendicular"
        return "perpendicular_diagonals"
    else:
        pass


def invalid_input(coord):
    if coord in shape:
        return True
    return False


# Invalid Shape check


def invalid_shape(coord):
    try:
        a = find_angle(coord[3], coord[0], coord[1])
        b = find_angle(coord[0], coord[1], coord[2])
        c = find_angle(coord[1], coord[2], coord[3])
        d = find_angle(coord[2], coord[3], coord[0])
        if a == 180 or b == 180 or c == 180 or d == 180:
            return True
        elif a == 0 or b == 0 or c == 0 or d == 0:
            return True
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
    if angles[0] == c1:
        return [coord[0], coord[2], coord[1], coord[3]]
    elif angles[0] ==  c2:
        return [coord[0], coord[1], coord[3], coord[2]]
    elif angles[0] == c3:
        return [coord[0], coord[3], coord[2], coord[1]]
    pass
