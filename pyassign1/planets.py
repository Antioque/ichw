"""planets.py: A rough model of the solar system.In order to emphsize that all those orbits are ellipse, I didn't use equal propotion models.I've to say that it is a little slow.

__author__ = "Xuruosen"
__pkuid__  = "1700011757"
__email__  = "xhycentre@pku.edu.cn"
"""

def main():
    """main module
    """
    import turtle
    import math
    Cosmos = turtle.Screen()
    Cosmos.bgcolor("black")
    Sun = turtle.Turtle()
    Sun.color("yellow")
    Sun.shape("circle")
    Mercury = turtle.Turtle()
    Mercury.color("blue")
    Venus = turtle.Turtle()
    Venus.color("brown")
    Earth = turtle.Turtle()
    Earth.color("blue")
    Mars = turtle.Turtle()
    Mars.color("red")
    Jupiter = turtle.Turtle()
    Jupiter.color("green")
    Saturn = turtle.Turtle()
    Saturn.color("white")
    Sun.shapesize(2)
    Sun.stamp()
    Count = 50
    for a in [Mercury,Venus,Earth,Mars,Jupiter,Saturn]:
        a.shapesize(1)
        a.shape("circle")
        a.pensize(5)
        a.up()
        a.forward(Count)
        Count+=30
        a.down()
        a.speed(0)
    BigInt = 1000
    for i in range(BigInt):
        Cosine = math.cos(math.pi/BigInt*(i+1))
        Sine = math.sin(math.pi/BigInt*(i+1))
        c1 = 50
        c2 = 0.6
        for a in [Mercury,Venus,Earth,Mars,Jupiter,Saturn]:
            A = c1/(1-c2)
            C = A*c2
            a.goto(A*Cosine-C,math.sqrt(A**2-C**2)*Sine)
            c1+=30
            c2+=0.05
    Cosmos.exitonclick()

if __name__ == '__main__':
    main()