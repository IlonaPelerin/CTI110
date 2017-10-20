# CTI-110
# M5LAB1 - Turtle Square & Triangle
# Ilona Pelerin
# October 20, 2017


def main():


    import turtle

    wn = turtle.Screen()
    pico = turtle.Turtle()
    pico.shape('turtle')

    wn.bgcolor('blue')

    pico.color('yellow')
    pico.pensize(5)

    for i in range(4):
        pico.forward(200)
        pico.right(90)

    pico.left(60)
    pico.forward(200)
    pico.right(120)
    pico.forward(200)


    wn.exitonclick()

main()
                     
