from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command with arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                then multiply the transform matrix by the translation matrix -
                takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""


def parse_file(fname, points, transform, screen, color):
    # Get all the commands
    fil = open(fname, "r")
    commands = []
    all_img = []
    for x in fil:
        commands.append(x.strip())
    curr = 0
    while curr < len(commands):
        print(curr, len(commands))
        if commands[curr] == "line":
            x0, y0, z0, x1, y1, z1 = [float(i) for i in commands[curr + 1].split(" ")]
            add_edge(points, x0, y0, z0, x1, y1, z1)
            curr += 2
        elif commands[curr] == "ident":
            ident(transform)
            curr += 1
        elif commands[curr] == "scale":
            sx, sy, sz = [float(i) for i in commands[curr + 1].split(" ")]
            matrix_mult(make_scale(sx, sy, sz), transform)
            curr += 2
        elif commands[curr] == "move":
            tx, ty, tz = [float(i) for i in commands[curr + 1].split(" ")]
            matrix_mult(make_translate(tx, ty, tz), transform)
            curr += 2
        elif commands[curr] == "rotate":
            axis, theta = commands[curr + 1].split(" ")
            rot = new_matrix()
            ident(rot)
            theta = float(theta)
            if axis == "x":
                rot = make_rotX(theta)
            elif axis == "y":
                rot = make_rotY(theta)
            elif axis == "z":
                rot = make_rotZ(theta)
            matrix_mult(rot, transform)
            curr += 2
        elif commands[curr] == "apply":
            matrix_mult(transform, points)
            curr += 1
        elif commands[curr] == "display":
            clear_screen(screen)
            for i in range(0, len(points), 2):
                draw_line(int(points[i][0]), int(points[i][1]),
                          int(points[i + 1][0]), int(points[i + 1][1]),
                          screen, color)
            display(screen)
            curr += 1
        elif commands[curr] == "save":
            clear_screen(screen)
            for i in range(0, len(points), 2):
                draw_line(int(points[i][0]), int(points[i][1]),
                          int(points[i + 1][0]), int(points[i + 1][1]),
                          screen, color)
            save_extension(screen, commands[curr + 1])
            curr += 2
        elif commands[curr] == "add_gif":
            clear_screen(screen)
            for i in range(0, len(points), 2):
                draw_line(int(points[i][0]), int(points[i][1]),
                          int(points[i + 1][0]), int(points[i + 1][1]),
                          screen, color)
            all_img.append(return_img(screen))
            curr += 1
        elif commands[curr] == "make_gif":
            print(len(all_img))
            make_gif(all_img)
            curr += 1
        elif commands[curr] == "print_trans":
            print_matrix(transform)
            curr += 1
        elif commands[curr] == "set_background":
            for i in range(len(screen)):
                for j in range(i):
                    screen[i][j] = [int(i) for i in commands[curr + 1].split(" ")]
            curr += 2
        else:
            print(f"Undefined command: {commands[curr]}")
            curr += 1
