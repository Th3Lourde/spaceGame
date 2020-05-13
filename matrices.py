import numpy

t = numpy.pi/36
u = 1
T = 0

Rotate = numpy.array([[numpy.cos(t),-numpy.sin(t),0], [numpy.sin(t), numpy.cos(t), 0],[0,0,1]])
Rotate_Neg = numpy.array([[numpy.cos(t),numpy.sin(t),0], [-numpy.sin(t), numpy.cos(t), 0],[0,0,1]])

Shift = numpy.array([[1,0, u*numpy.cos(T)], [0,1,u*numpy.sin(T)], [0,0,1]])

i = numpy.array([[0, 0],[0, 2],[1, 1]])

shift_towards = numpy.array([[1,0, i[0][0]],[0,1,i[1][0]], [0,0,1]])
shift_away = numpy.array([[1,0, i[0][0]],[0,1, i[1][0]], [0,0,1]])

i

def moveForwards(coord):
    shift = numpy.array([[1,0, u*numpy.cos(T)], [0,1,u*numpy.sin(T)], [0,0,1]])
    coord = shift@coord
    return coord

def getPosition():
    # (0,0), (0,2)
    p1 = i[0][0]
    
    pos = [(i[0][0] + i[1][0])/2,  (i[0][1] + i[1][1])/2]
    
    print("position is: {}".format(pos))
    
getPosition()

i = moveForwards(i)
print(i)