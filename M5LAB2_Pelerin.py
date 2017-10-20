# CTI-110
# M5LAB2 - Turtle Initials
# Ilona Pelerin
# October 20, 2017


def main():


    import turtle

    wn = turtle.Screen()
    pico = turtle.Turtle()
    pico.shape('turtle')

    wn.bgcolor('lightyellow')

    pico.color('purple')
    pico.pensize(10)

    pico.backward(200)
    pico.right(360)
    pico.forward(100)
    pico.left(90)
    pico.forward(300)
    pico.left(90)
    pico.forward(100)
    pico.backward(100)
    pico.left(360)
    pico.backward(100)
    pico.left(360)
    pico.forward(100)
    pico.left(90)
    pico.forward(300)
    pico.left(90)
    pico.forward(110)

    pico.color('lightyellow')
    pico.forward(30)

    pico.color('green')
    pico.left(90)
    pico.forward(300)
    

    for i in range(3):
           pico.right(90)
           pico.forward(120)

    pico.left(90)
    pico.forward(190)
    pico.left(90)

    pico.color('lightyellow')
    pico.forward(150)

    pico.color('hotpink')
 


    wn.exitonclick()

main()
                     
