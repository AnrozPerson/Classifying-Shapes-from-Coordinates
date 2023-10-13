# Y9-CAT-Inv2-Arun-Rajayogan

Given Problem:

In a not-too-distant future, (friendly) bipedal robots will be part of daily life. As they navigate a human-centered environment, they will need to detect affordances such as walls, windows, doors, tables, fridges, dishwashers and other objects with quadrilateral faces. One such robot will likely ‘see’ quadrilaterals at an angle so that a square tabletop might look like a rhombus, and a rectangular TV might look like a trapezium or a parallelogram. This is due to how squares and rectangles are projected onto retinas and image sensors. Quadrilateral detection is therefore an important area of computer vision research in industry and academia (online-search “Real-time quadrilateral object corner detection algorithm based on deep learning” if interested).
For this investigation, we will imagine that a robot is surveying a visual scene (you’ve asked it to load the dishwasher) and it is able to detect edges and corners using its neural networks. These corner coordinates will be superimposed on a Cartesian plane and an algorithm will be required to identify the quadrilateral faces that are detected.
You will be given four sets of Cartesian coordinates that represent an abstract quadrilateral. These can be joined together to form some of the convex polygons shown below.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The program takes in 4 coordinates and considers what shape they are.

Uses two sets of shape checks, usesside and angle properties and diagonal properties of quadrilaterals.

Code will run as follows:

###########################

Vertex A: 0,0

Vertex B: w,1

Error: Vertex B: 1,1

Vertex C: 1,1

Error: Vertex B: 1,-1

Vertex D: 2,0

###########################

Side and angle properties for (0, 0), (1, 1), (2, 0) and (1, -1)

One pair of parallel sides       AB and CD

Two pairs of parallel sides       also AD and BC

All sides equal       AB, BC, CD and DA are 1.4

All angles 90 degrees       DAB, ABC, BCD, CDA

Two pairs of adjacent equal sides       AD and AB, AB and BC, BC and CD, CD and AD

CONCLUSION: The quadrilateral is a SQUARE



Diagonal properties for (0, 0), (1, 1), (2, 0) and (1, -1)      

Diagonals are perpendicular     AC and BD are perpendicular     

One diagonal bisects the other     AC bisects BD

Both diagonals bisect each other     AC and BD both bisect each other

One diagonal bisects the angles it passes through     AC and BD 

Both diagonals bisect the angles they pass through     AC and BD

Diagonals are equal in length     AC and BD are 2.0

CONCLUSION: The quadrilateral is a SQUARE
Test again (Y/N): 
