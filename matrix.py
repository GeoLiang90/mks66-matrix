"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for y in range(len(matrix[0])):
        out = ""
        for x in range(len(matrix)):
            out += str(matrix[x][y]) + "\t"
            if (x == len(matrix) - 1):
                print(out)
    print("")
    pass

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    lim = len(matrix)
    for r in range(lim):
        for c in range(lim):
            if (r == c):
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0
    pass

def getCol(matrix,col):
    ret = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r == col:
                ret.append(matrix[r][c])
    return ret
#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for c in range(len(m2)):
        column = getCol(m2, c)

        for r in range(len(m2[0])):
            sum = 0

            for val in range(4):
                sum += m1[val][r] * column[val]
            m2[c][r] = sum
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
