import pgzrun
import random

HEIGHT = 750
WIDTH = 500
random_shape = []
topline = None
x_shape = 200
y_shape = 0
index = 0
rotate_counter = 0
index_1 = 0
last_x_shape = 0
last_y_shape = 0
hit_position = 750

shapes_list = [[[1],[1],[1],[1]],
               [[1,1,1],[0,1,0]],
               [[1,0],[1,0],[1,1]],
               [[0,1],[0,1],[1,1]],
               [[1,0],[1,1],[0,1]],
               [[0,1],[1,1],[1,0]]]


shape_rotation = [[[[1],[1],[1],[1]], [[1,1,1,1]]],

                  [[[1,1,1],[0,1,0]], [[1,0], [1,1], [1,0]], [[0,1,0], [1,1,1]], [[0,1],[1,1],[0,1]]],

                  [[[1,0],[1,0],[1,1]], [[0,0,1], [1,1,1]], [[1,1],[0,1],[0,1]], [[1,1,1], [1,0,0]]],

                  [[[0,1],[0,1],[1,1]], [[1,1,1], [0,0,1]], [[1,1],[1,0],[1,0]], [[1,0,0], [1,1,1]]],

                  [[[1,0],[1,1],[0,1]], [[0,1,1], [1,1,0]]],

                  [[[0,1],[1,1],[1,0]], [[1,1,0], [0,1,1]]]]

matrix_list = [[0 for i in range(10)] for j in range(15)]


colors = ["red", "blue", "green", "yellow", "gray", "brown", "orange", "purple", "pink"]


def draw():
    screen.clear()
    matrix_draw()

    for i in range(len(random_shape)):
        for j in range(len(random_shape[i])):
            if random_shape[i][j] == 1:
                screen.draw.filled_rect(Rect(j * 50 + x_shape,i * 50 + y_shape, 50, 50), color)


def pickshape():
    global random_shape, x_shape, y_shape, index, rotate_counter,color
    color = random.choice(colors)
    index = random.randint(0,5)
    random_shape = shapes_list[index]
    x_shape = 200
    y_shape = 0
    rotate_counter = 0

def rotate():
    global rotate_counter, index, index_1, random_shape

    rotate_counter += 1

    index_1 = rotate_counter % len(shape_rotation[index])

    random_shape = shape_rotation[index][index_1]

def hit_print(xhit, yhit, shape):
    x = xhit//50
    y = yhit//50
    for i in shape:
        print(i)
        if i != [0,0,0,0]:
            for j in i:
                if j == 1:
                    matrix_list[y][x] = 1
                x += 1
            x = xhit//50
            y += 1
    print(matrix_list)



def on_key_down(key):
    global  x_shape, y_shape
    if key == keys.A  and x_shape > 0 :
        x_shape -= 50
    if key == keys.D and 500 - x_shape > 50 * len(random_shape[0]):
        x_shape += 50
    if key == keys.SPACE and 500 - x_shape > 50 * len(random_shape[0]):
        rotate()


def matrix_draw():

    for i in range(len(matrix_list)):
        for j in range(len(matrix_list[i])):
            if matrix_list[i][j] == 1:
                screen.draw.filled_rect(Rect(j*50, i*50,50,50), "white")


def rowsearch():
    for rowindex in range(len(matrix_list)):
        if matrix_list[rowindex] != [0,0,0,0,0,0,0,0,0,0]:
            return rowindex
    return None


def define_hitpositionlocal(x_current):
    topline = rowsearch()
    if topline is None:
        return 750

    columnhitpos = x_current / /50


    while topline < len(matrix_list):
        if matrix_list[topline][columnhitpos] == 1:
            localhitposition = 750 - ((15 - topline) * 50)
            return localhitposition
        topline += 1
    return 750

def deleteAdd():
    for row in range(len(matrix_list)):
        if matrix_list[row] == [1,1,1,1,1,1,1,1,1,1]:
            print(matrix_list[row])
            del matrix_list[row]
            matrix_list.insert(0,[0,0,0,0,0,0,0,0,0,0])

def collision():
    pass





def update():
    global y_shape, x_shape, hit_position
    hit_position = define_hitpositionlocal(x_shape)

    if hit_position - y_shape > 50 * len(random_shape):
        y_shape +=2
    if hit_position - y_shape == 50 * len(random_shape):
        hit_print(x_shape, y_shape, random_shape)
        x_shape = 0
        y_shape = 0
        pickshape()
    deleteAdd()




pickshape()
pgzrun.go()
