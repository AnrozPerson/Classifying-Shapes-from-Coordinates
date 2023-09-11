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

A = input("Vertex A: ")
if invalid_input(A):
    A = input("Error: Vertex A: ")
B = input("Vertex B: ")
if invalid_input(B):
    B = input("Error: Vertex B: ")
C = input("Vertex C: ")
if invalid_input(C):
    C = input("Error: Vertex C: ")
D = input("Vertex D: ")
if invalid_input(D):
    D = input("Error: Vertex D: ")

print(tuple(A.split(",")))