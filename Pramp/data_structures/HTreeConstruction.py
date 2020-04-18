# https://coderpad.io
# jordanlouiscarson@gmail.com
# linkedin -> https://www.linkedin.com/in/jordan-carson-0a87083a/

# https://www.linkedin.com/in/mathur-kunal/
from math import sqrt


def drawHTree(x, y, length, depth):
    if depth == 0:
        return
    x0 = x - length / 2
    x1 = x + length / 2
    y0 = y - length / 2
    y1 = y + length / 2

    drawLine(x0, y, x1, y)  # connecting segment
    drawLine(x0, y0, x0, y1)  # left segment
    drawLine(x1, y0, x1, y1)  # right segment

    # after drawLine the length of the line segments drawn at each stage by √2.
    drawHTree(x0, y0, length / sqrt(2), depth - 1)
    drawHTree(x0, y1, length / sqrt(2), depth - 1)
    drawHTree(x1, y0, length / sqrt(2), depth - 1)
    drawHTree(x1, y1, length / sqrt(2), depth - 1)


def drawLine(x, y, x1, y1):
    print(x, y, x1, y1)


print(drawHTree(0, 0, 6, 3))