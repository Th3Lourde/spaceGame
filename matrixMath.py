import numpy

t = numpy.pi/2
u = 5
T = numpy.pi/2

Rotate = numpy.array([[numpy.cos(t),-numpy.sin(t),0], [numpy.sin(t), numpy.cos(t), 0],[0,0,1]])
Rotate_Neg = numpy.array([[numpy.cos(t),numpy.sin(t),0], [-numpy.sin(t), numpy.cos(t), 0],[0,0,1]])

Shift = numpy.array([[1,0, u*numpy.cos(T)], [0,1,u*numpy.sin(T)], [0,0,1]])

i = numpy.array([[0, 0],[0, 2],[1, 1]])

Shift_T = numpy.array([[1,0, i[0][0]],[0,1,i[1][0]], [0,0,1]])
Shift_A = numpy.array([[1,0, i[0][0]],[0,1, i[1][0]], [0,0,1]])

i

def moveForwards(coord,T):
    shift = numpy.array([[1,0, u*numpy.cos(T)], [0,1,u*numpy.sin(T)], [0,0,1]])
    coord = shift.dot(coord)
    return coord

def getPosition():
    # (0,0), (0,2)
    p1 = i[0][0]

    pos = [(i[0][0] + i[1][0])/2,  (i[0][1] + i[1][1])/2]

    print("position is: {}".format(pos))

def rotate(coord,T):
    Rotate = numpy.array([[numpy.cos(t),-numpy.sin(t),0], [numpy.sin(t), numpy.cos(t), 0],[0,0,1]])
    To = numpy.array([[1,0, -1*(coord[0][0])],[0,1,-1*(coord[1][0])], [0,0,1]])
    Back = numpy.array([[1,0, coord[0][0]],[0,1, coord[1][0]], [0,0,1]])

    coord  = Back.dot(Rotate.dot(To.dot(coord)))

    T+=t

    return coord, T


def rotate_neg(coord,T):
    Rotate = numpy.array([[numpy.cos(t),numpy.sin(t),0], [-numpy.sin(t), numpy.cos(t), 0],[0,0,1]])
    To = numpy.array([[1,0, -1*(coord[0][0])],[0,1,-1*(coord[1][0])], [0,0,1]])
    Back = numpy.array([[1,0, coord[0][0]],[0,1, coord[1][0]], [0,0,1]])

    coord  = Back.dot(Rotate.dot(To.dot(coord)))

    T-=t

    return coord, T


def main():
    t = numpy.pi/2
    u = 5
    T = numpy.pi/2
    i = numpy.array([[0, 0],[0, 2],[1, 1]])

    i,T = rotate_neg(i,T)

    i = moveForwards(i,T)

    i,T = rotate(i,T)

    i =moveForwards(i,T)

    print(i)
main()
