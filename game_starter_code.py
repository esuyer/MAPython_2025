import turtle

# One game tick
def tick():


  turtle.update()            # update the canvas

  turtle.ontimer(tick, 17)   # scheduling the next tick in 17 ms


turtle.setup(600, 400)
turtle.tracer(0)             # 0 means do not update the canvas until function turtle.update() is called

# Game objects: paddle and ball 


# Starting the game loop (the first tick)
tick()

turtle.mainloop()