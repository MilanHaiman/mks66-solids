from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color )

# red=[255,0,0]
# blue=[0,0,255]
# draw_triangle(0,0,0,0,100,0,100,50,100,screen,zbuffer,red)
# draw_triangle(100,0,0,100,100,0,0,50,100,screen,zbuffer,blue)
# draw_triangle(0,65,0,100,65,0,50,100,100,screen,zbuffer,blue)
# save_extension(screen, "test.png")
