import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()

for _ in range(2):
    turtlePen.left(45)
    for _ in range(4):
        turtlePen.left(90)
        for _ in range(4):
            turtlePen.forward(200)
            turtlePen.left(90)

window.mainloop()


