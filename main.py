import pygame as pg
from pygame import *
import random

width = 800
height = 800
gap = 10
screen = [width, height]

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
brown = (165, 42, 42)
green = (0, 128, 0)

pg.init()
window = pg.display.set_mode(screen)

squares = [[random.randint(0, 1) for i in range(width // gap)] for j in range(height // gap)]


"""
class game():
    def __init__(self, width, height):
        window.fill(white)
        for i in range(width // gap):
            for j in range(height // gap):
                if squares[i][j] == 1:
                    pg.draw.rect(window, black, Rect(i * gap, j * gap, gap, gap))
        pg.display.update()

    def repeat(self):
        next = [["" for i in range(width // gap)] for j in range(height // gap)]
        for i in range(width // gap):
            for j in range(height // gap):
                self.new(i, j, next)
        squares = next
        

    def new(self, x, y, next):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i <= width // gap and 0 <= y + j <= height // gap:
                    sum += squares[x + i][y + j]
        sum -= squares[x][y]
        if squares[x][y] == 1 and (sum == 2 or sum == 3):
            next[x][y] = 1
        else:
            next[x][y] = 0
        if squares[x][y] == 0 and sum == 3:
            next[x][y] = 1
        else:
            next[x][y] = 0
            
game(width, height)
"""

window.fill(white)


def start(width, height, squares):
    for i in range(width // gap):
        for j in range(height // gap):
            if squares[i][j] == 1:
                pg.draw.rect(window, black, Rect(i * gap, j * gap, gap, gap))
    pg.time.delay(120)
    pg.display.update()


def repeat(next1):
    for i in range(width // gap):
        for j in range(height // gap):
            #if not(i == 0 or i == (width // gap) - 1 or j == 0 or j == (height // gap)- 1):
            next1[i][j] = new(i, j, next1)
    # print("This is next1", next1)
    return next1


def new(x, y, next):
    sum = 0
    current = squares[x][y]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i <= (width // gap) - 1 and 0 <= y + j <= (height // gap) - 1:
                sum += squares[x + i][y + j]
    sum -= current

    if current == 0 and sum == 3:
        return 1
    elif current == 1 and(sum < 2 or sum > 3):
        return 0
    return current


while True:
    window.fill(white)
    next1 = squares
    # print("this is next2", squares)
    # pg.display.update()
    start(width, height, next1)
    squares = repeat(next1)
