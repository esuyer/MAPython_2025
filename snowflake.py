import turtle

def draw_line(length, depth) :
    if depth == 1 :
        turtle.forward(length)
    else:
        draw_line(length / 3, depth - 1)
        turtle.right(60)
        draw_line(length / 3, depth - 1)
        turtle.left(120)
        draw_line(length / 3, depth - 1)
        turtle.right(60)
        draw_line(length / 3, depth - 1)



def draw_Koch_snowflake(length, depth):
    draw_line(length, depth)
    turtle.left(120)
    draw_line(length, depth)
    turtle.left(120)
    draw_line(length, depth)


turtle.speed(0)
turtle.color("blue")
turtle.width(2)
turtle.up()
turtle.goto(-150, 0)
turtle.down()

depth = turtle.numinput("Koch snowflake",
                        "Enter max depth (up to 5)",
                        3,
                        1,
                        5)
if depth == None:
    turtle.bye()

##draw_line(300, depth)
draw_Koch_snowflake(300, depth)

turtle.mainloop()