import turtle


def draw_line(length, depth):
    if depth == 1:
        turtle.forward(length)
    else:
        draw_line(length / 3, depth - 1)
        turtle.right(60)
        draw_line(length / 3, depth - 1)
        turtle.left(120)
        draw_line(length / 3, depth - 1)
        turtle.right(60)


draw_line(100, 2)

turtle.mainloop()
