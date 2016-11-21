import random
import Visualization

array = []

n = 128
size = 2 * n + 1
roughness = 5


def init():
    global array
    array = [0] * size
    for i in range(size):
        array[i] = [0] * size
    array[0][0] = random.uniform(0.3, 0.8)
    array[0][size - 1] = random.uniform(0.3, 1.5)
    array[size - 1][0] = random.uniform(0.3, 1.5)
    array[size - 1][size - 1] = random.uniform(0.3, 0.8)


def square(lx, ly, rx, ry):
    global array

    def average():
        sum = array[lx][ly] + array[lx][ry] + array[rx][ly] + array[rx][ry]
        return sum / 4.0 + random.uniform(-2 * half_size * roughness, 2 * half_size * roughness)

    half_size = int((rx - lx) / 2)
    cx = lx + half_size
    cy = ly + half_size
    array[cx][cy] = average()


def Sdiamond(lx, ly, rx, ry):
    def diamond(cx, cy, length):
        global array
        half_size = int(length / 2)

        def average():
            sum = array[(cx - half_size) % size][cy] + array[(cx + half_size) % size][cy] + array[
                cx][(cy - half_size) % size] + array[cx][(cy + half_size) % size]
            return sum / 4.0 + random.uniform(-2 * half_size * roughness, 2 * half_size * roughness)

        array[cx][cy] = average()

    length = rx - lx
    diamond(lx, int((ry + ly) / 2), length)
    diamond(rx, int((ry + ly) / 2), length)
    diamond(int((rx + lx) / 2), ly, length)
    diamond(int((rx + lx) / 2), ry, length)


def diamond_square():
    length = size - 1
    border = 1
    while length > 1:
        x, y = 0, 0
        for i in range(0, border):
            y = 0
            for j in range(0, border):
                square(x, y, x + length, y + length)
                y += length
            x += length

        x, y = 0, 0
        for i in range(0, border):
            y = 0
            for j in range(0, border):
                Sdiamond(x, y, x + length, y + length)
                y += length
            x += length

        length = int(length / 2)
        border *= 2


maxValue = 0


def smooth():
    global array, maxValue
    for i in range(size):
        for j in range(size):
            array[i][j] *= array[i][j]
            if array[i][j] > maxValue:
                maxValue = array[i][j]


def print_matrix():
    for i in range(size):
        print(array[i])


init()
diamond_square()
smooth()
Visualization.visualize_color_grad(array, size, maxValue)
Visualization.visualize(array, size, maxValue)
