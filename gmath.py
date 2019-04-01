import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    a = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])
    vector[0] = vector[0]/a
    vector[1] = vector[1]/a
    vector[2] = vector[2]/a


#Return the dot porduct of a . b
def dot_product(a, b):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]*b[i]
    return sum

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p = polygons[i]
    p1 = polygons[i+1]
    p2 = polygons[i+2]

    a = [p1[0]-p[0], p1[1]-p[1], p1[2]-p[2]]
    b = [p2[0]-p[0], p2[1]-p[1], p2[2]-p[2]]

    return [a[1]*b[2] - b[1]*a[2], a[2]*b[0] - b[2]*a[0], a[0]*b[1] - b[0]*a[1]]
