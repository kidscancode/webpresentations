import turtle
import time
import random
fred = turtle.Pen()

def square(size):
    for i in range(4):
        fred.forward(size)
        fred.left(90)

def triangle(size):
    for i in range(3):
        fred.forward(size)
        fred.left(120)

def randshapes():
    fred.left(random.randrange(0, 45))
    for i in range(100):
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        fred.up()
        fred.goto(x, y)
        fred.down()
        fred.color(random.choice(colorlist))
        size = random.randrange(10, 100)
        fred.begin_fill()
        shape = random.choice([square, triangle, fred.circle])
        shape(size)
        fred.end_fill()

def spiral():
    fred.color(random.choice(colorlist))
    fred.width(3)
    for i in range(200):
        fred.forward(i*5)
        fred.left(92)

def rose():
    fred.color(random.choice(colorlist))
    fred.width(3)
    for i in range(100):
        fred.circle(i*5, 180)
        fred.right(45)

def nautilus():
    for x in range(random.randrange(1,4)):
        fred.color(random.choice(colorlist))
        fred.width(2)
        for i in range(100):
            fred.circle(i*8)
            fred.left(8)

def starburst():
    fred.color(random.choice(colorlist))
    fred.width(3)
    for i in range(18):
        square(100)
        fred.forward(20)
        fred.left(20)
    for i in range(18):
        square(200)
        fred.forward(20)
        fred.left(20)
    for i in range(18):
        square(300)
        fred.forward(20)
        fred.left(20)

def flag():
    flag_colors = ["red", "orange", "yellow", "seagreen", "orchid",
                   "royalblue", "dodgerblue"]
    fred.up()
    fred.goto(-320, -195)
    fred.width(70)
    for color in flag_colors:
        fred.color(color)
        fred.down()
        fred.forward(640)
        fred.up()
        fred.backward(640)
        fred.left(90)
        fred.forward(66)
        fred.right(90)
    fred.width(25)
    fred.color("white")
    fred.goto(0, -170)
    fred.down()
    fred.circle(170)
    fred.left(90)
    fred.forward(340)
    fred.left(180)
    fred.forward(170)
    fred.right(45)
    fred.forward(170)
    fred.back(170)
    fred.left(90)
    fred.forward(170)

colorlist = ["red", "green", "yellow", "blue", "red", "violet", "orange",
             "turquoise", "papaya whip", "pink", "purple", "orchid", "seagreen",
             "royalblue"]
patterns_list = [randshapes, spiral, nautilus, flag, rose, starburst]
while True:
    fred.reset()
    fred.speed(0)
    pattern = random.choice(patterns_list)
    pattern()
    time.sleep(5)
