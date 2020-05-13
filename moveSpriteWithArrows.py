import curses
from turtle import *

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

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

def moveRight(x):
    tom.right(int(x))

    marker.undo()  # erase previous position
    tom.setposition(int(tom.xcor()), int(tom.ycor()))

    marker.write(tom.position(), align='center', font=FONT)

try:
    # color('red', 'yellow')
    # begin_fill()
    while True:
        char = screen.getch()
        if char == ord('q'):
            break

        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right')
            moveRight(50)

        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            moveLeft(50)

        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up   ')
            moveForward(50)

        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down, no mapping ')

    # end_fill()
    done()
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
