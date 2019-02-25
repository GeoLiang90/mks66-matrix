from display import *
from draw import *
from matrix import *

screen = new_screen()
r = 0
g = 200
b = 200
color = [ r, g, b ]
matrix = new_matrix(0,0)
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
IDENT = new_matrix()
ident(IDENT)
matrix_mult(A,B)
print_matrix (A)
print_matrix(B)

matrix_mult(B,A)
print_matrix(A)
print_matrix(B)

matrix_mult(IDENT,A)
print_matrix(A)

m2 = []
m1 = new_matrix()

print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 = ")
add_edge(m2,1,2,3,4,5,6)
print_matrix(m2)

print("Testing ident. m1 =")
ident(m1)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)

print("Testing Matrix mult. m1 =")
m1 = []
add_edge(m1,1,2,3,4,5,6)
add_edge(m1,7,8,9,10,11,12)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)

add_edge(matrix,0,0,0,32,0,0)
add_edge(matrix,16,32,0,32,0,0)
add_edge(matrix,0,0,0,16,32,0)
draw_lines( matrix, screen, color )


i = 0
while (i < 15):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] +=  2
            matrix[r][c] = int(matrix[r][c] * 1.2)

    draw_lines( matrix, screen, color )
    i+=1

display(screen)
