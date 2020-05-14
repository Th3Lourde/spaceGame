import curses
import numpy
from turtle import *

# get the curses screen window
screen = curses.initscr()
#
# # turn off input echoing
curses.noecho()
#
# # respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)


i = numpy.array([[0, 0],[0, 10],[1, 1]])

playground = Screen()

playground.bgcolor("black")

tom = Turtle()              # use nouns for objects, run is a verb

FONT = ('Arial', 24, 'normal')

tom.color("white")
tom.speed("slowest")
tom.penup()

marker = Turtle(visible=False)  # our virtual magic marker
marker.penup()
marker.color("yellow")
marker.setposition(390, 370)
marker.write(tom.position(), align='center', font=FONT)

def rotate_neg(coord,T):
    Rotate = numpy.array([[numpy.cos(t),numpy.sin(t),0], [-numpy.sin(t), numpy.cos(t), 0],[0,0,1]])
    To = numpy.array([[1,0, -1*(coord[0][0])],[0,1,-1*(coord[1][0])], [0,0,1]])
    Back = numpy.array([[1,0, coord[0][0]],[0,1, coord[1][0]], [0,0,1]])

    coord = Back.dot(Rotate.dot(To.dot(coord)))

    T -= t

    return coord, T


def moveForward(x):
    tom.forward(int(x))
    marker.undo()  # erase previous position

    tom.setposition(int(tom.xcor()), int(tom.ycor()))

    marker.write(tom.position(), align='center', font=FONT)


def moveLeft(x):
    tom.left(int(x))

    marker.undo()  # erase previous position
    tom.setposition(int(tom.xcor()), int(tom.ycor()))

    marker.write(tom.position(), align='center', font=FONT)

def moveRight(i, T):

    tom.left(int(10))

    i,T = rotate_neg(i,T)

    pos = getPosition(i)

    # tom.right(int(x))

    # print(pos)
    # screen.addstr(0, 0, '{}'.format(pos))


    marker.undo()  # erase previous position
    tom.setposition(int(tom.xcor()), int(pos[1]))

    marker.write(tom.position(), align='center', font=FONT)

    return i, pos

def getPosition(i):
    pos = [(i[0][0] + i[1][0])/2,  (i[0][1] + i[1][1])/2]
    return pos



try:
    t = numpy.pi/36
    u = 5
    T = numpy.pi/2

    # color('red', 'yellow')
    # begin_fill()
    while True:
        char = screen.getch()

        if char == ord('q'):
            break

        elif char == curses.KEY_RIGHT:
            # screen.addstr(0, 0, 'right')
            screen.addstr(0, 0, '{}'.format(i))

            i, r = moveRight(i, T)

            screen.addstr(0, 0, '{}   {}  {}'.format(r, i, tom.position()))



        elif char == curses.KEY_LEFT:
            # screen.addstr(0, 0, 'left ')
            moveLeft(50)

        elif char == curses.KEY_UP:
            # screen.addstr(0, 0, 'up   ')
            moveForward(50)

        elif char == curses.KEY_DOWN:
            ...
            # screen.addstr(0, 0, 'down, no mapping ')

    # end_fill()
    done()

finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
