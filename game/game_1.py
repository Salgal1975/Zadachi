# -*- coding: utf-8 -*-

import tkinter

# constans
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'

# balls class
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

# mause events
def mause_click(event):
    print(event.num, event.x, event.y)


root = tkinter.Tk()
root.title("Coding balls")
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()
canvas.bind('<Button-1>', mause_click)
canvas.bind('<Button-2>', mause_click, '+' )
canvas.bind('<Button-3>', mause_click, '*')
root.mainloop()


