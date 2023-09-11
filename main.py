###Main.py

#Import Matplot library to do visual graph things
#Import numpy for math functions
import matplotlib.pyplot as plt
import numpy as np

shape = []

#a and b will be tuples holding coordinates
def side_length(a, b):
    pass

def invalid_input(coord):
    if coord in shape:
        return True




#User Input

A = shape.append(tuple(map(int, input("Vertex A: ").split(","))))
if invalid_input(A):
    A = shape.append(tuple(map(int, input("Error: Vertex A: ").split(","))))
B = shape.append(tuple(map(int, input("Vertex B: ").split(","))))
if invalid_input(B):
    B = shape.append(tuple(map(int, input("Error: Vertex B: ").split(","))))
C = shape.append(tuple(map(int, input("Vertex C: ").split(","))))
if invalid_input(C):
    C = shape.append(tuple(map(int, input("Error: Vertex C: ").split(","))))
D = shape.append(tuple(map(int, input("Vertex D: ").split(","))))
if invalid_input(D):
    D = shape.append(tuple(map(int, input("Error: Vertex D: ").split(","))))

print(shape)