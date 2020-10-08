import turtle
'''

turtle.setup(500,600)
turtle.hideturtle()

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140


turtle.penup()

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.write("Betelgeuse")
turtle.pendown()


turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.write("Alnitak")

turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.write("Saiph")


turtle.penup()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)


turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.dot()
turtle.write("Alnilam")

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.write("Mintaka")

turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()
turtle.write("Rigel")
turtle.penup()

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.write("Meissa")

turtle.bgcolor("Pink")
'''


turtle.penup()
turtle.fillcolor("Red")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.penup()
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

turtle.bgcolor("pink")
