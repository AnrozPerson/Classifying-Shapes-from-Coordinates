# Main.py

# Import Matplot library to do visual graph things
# Import numpy for math functions
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Back, Style
from find_prop import *
from properties import *


# Shape list to store the coords of unkown shape
shape = []
shape_1 = []
shape_2 = []


#global sides_1
#global sides_2

#sides_1 = {}
#sides_2 = {}




# User Input
def main():
    shape = []
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "#"*50 + Style.RESET_ALL)
    try:
        A = tuple(map(int, input(Fore.GREEN + "Vertex A: " + Style.RESET_ALL).split(",")))
    except:
        A = tuple(map(int, input("Error: Vertex A: ").split(",")))
    while invalid_input(A) is True:
        A = tuple(map(int, input("Error: Vertex A: ").split(",")))
    shape.append(A)
    try:
        B = tuple(map(int, input(Fore.GREEN + "Vertex B: "  + Style.RESET_ALL).split(",")))
    except:
        A = tuple(map(int, input("Error:" + " Vertex A: ").split(",")))
    while invalid_input(B) is True:
        B = tuple(map(int, input("Error: Vertex B: ").split(",")))
        invalid_input(B)
    shape.append(B)
    try:
        C = tuple(map(int, input(Fore.GREEN + "Vertex C: " + Style.RESET_ALL).split(",")))
    except:
        C = tuple(map(int, input("Error: Vertex C: ").split(",")))
    while invalid_input(C) is True:
        C = tuple(map(int, input("Error: Vertex C: ").split(",")))
        invalid_input(C)
    shape.append(C)
    try:
        D = tuple(map(int, input(Fore.GREEN + "Vertex D: " + Style.RESET_ALL).split(",")))
    except:
        D = tuple(map(int, input("Error: Vertex D: ").split(",")))
    while invalid_input(D) is True:
        D = tuple(map(int, input("Error: Vertex D: ").split(",")))
        invalid_input(D)
    shape.append(D)

    shape = sort_vertices(shape)

    if invalid_shape(shape):
        print(Style.BRIGHT + Fore.RED + "Shape Error. Redo." + Style.RESET_ALL)
        main()
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "#"*50 + Style.RESET_ALL)

    print(Style.RESET_ALL + "")

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
    print(Style.BRIGHT + Fore.RED + "Side and angle properties for " + str(shape[0]) + ", " + str(shape[1]) + ", " + str(shape[2]) + " and " + str(shape[3]) + Style.RESET_ALL)

    for i in shape_1:
        print(prop_1[i], 5*" ", Fore.RED + sides_1[i] + Style.RESET_ALL)
    for i in shape_check_1:
        if shape_check_1[i] == shape_1:
            print("")
            print(f"CONCLUSION: The quadrilateral is a {Fore.CYAN + i.upper()}" + Style.RESET_ALL)
            stat_1 = False
            break
    if stat_1:
        print("Unknown Shape")

    print("""

    """)

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
    print(Style.BRIGHT + Fore.RED + "Diagonal properties for " + str(shape[0]) + ", " + str(shape[1]) + ", " + str(shape[2]) + " and " + str(shape[3]) + Style.RESET_ALL)
    for i in shape_2:
        print(prop_2[i] + 5*" " + Fore.RED + sides_2[i] + Style.RESET_ALL)
    for i in shape_check_2:
        if shape_check_2[i] == shape_2:
            print("")
            print(f"CONCLUSION: The quadrilateral is a {Fore.CYAN + i.upper()}" + Style.RESET_ALL)
            stat_2 = False
    if stat_2:
        print("Unknown Shape")
    exit()
main()