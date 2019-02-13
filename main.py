from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print_matrix(A)
ident(A)
print_matrix(A)
draw_lines( matrix, screen, color )
display(screen)
