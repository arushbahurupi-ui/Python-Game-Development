import pgzrun
import random

HEIGHT = 750
WIDTH = 500
random_shape = []

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


def draw():
    screen.clear()
    matrix_draw()
    for i in range(len(random_shape)):
        for j in range(len(random_shape[i])):
            if random_shape[i][j] == 1:
                screen.draw.filled_rect(Rect(j * 50 + x_shape,i * 50 + y_shape, 50, 50), "red")


def pickshape():
    global random_shape, x_shape, y_shape, index, rotate_counter

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

def hit_print(xhit, y, shape):
    x = xhit//50
    y = y//50
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
                screen.draw.filled_rect(Rect(j*50, i*50,50,50), "red")

def update():
    global y_shape, x_shape
    if hit_position - y_shape > 50 * len(random_shape):
        y_shape +=5
    if hit_position - y_shape == 50 * len(random_shape):
        hit_print(x_shape, y_shape, random_shape)
        x_shape = 0
        y_shape = 0
        pickshape()





pickshape()
pgzrun.go()
