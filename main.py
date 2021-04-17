from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

x = open("per_script", "w")
x.write("line\n")
x.write("150 150 0 350 150 0\n")
x.write("line\n")
x.write("150 350 0 350 150 0\n")
x.write("line\n")
x.write("150 150 0 350 350 0\n")
x.write("line\n")
x.write("150 350 0 350 350 0\n")

for i in range(10):
    x.write("line\n")
    x.write(f"150 {350 + i} 0 350 {350 + i} 0\n")
    x.write("line\n")
    x.write(f"150 {140 + i} 0 350 {140 + i} 0\n")

x.write("display\n")

for i in range(42):
    x.write("ident\n")
    x.write("move\n")
    x.write("-250 -250 0\n")
    x.write("rotate\n")
    x.write(f"z {(42 - i) / 5}\n")
    x.write("move\n")
    x.write("250 250 0\n")
    x.write("apply\n")
    x.write("add_gif\n")
x.write("make_gif\n")

x.close()
imgs = parse_file('per_script', edges, transform, screen, color)


