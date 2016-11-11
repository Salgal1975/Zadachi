# -*- coding: utf-8 -*-

import tkinter

# constans
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'

# balls class
class Balls():
    # конструктор
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    # метод рисуем круг
    def draw(self):
        canvas.create_oval(self.x - self.r,
                           self.y - self.r,
                           self.x + self.r,
                           self.y + self.r,
                           fill=self.color)    # цвет заполнения круга


    # метод прячем круг
    def hide(self):
        canvas.create_oval (self.x - self.r,
                            self.y - self.r,
                            self.x + self.r,
                            self.y + self.r,
                            fill=BG_COLOR,      # цвет заполнения круга
                            outline=BG_COLOR)   # цвет линии окружности


# mause events
def mause_click(event):
    global main_ball
    if event.num == 1:
        main_ball = Balls(event.x, event.y, 30, 'blue')
        main_ball.draw()
    else:
        main_ball.hide()
    #print(event.num, event.x, event.y)


root = tkinter.Tk()  # экземпляр класса tkinter.Tk()-главне окно
root.title("Coding balls")  # название окна
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)  # свойства рабочего поля
canvas.pack()  # создает рабочее поле
canvas.bind('<Button-1>', mause_click)  # назначаем события кнопкам мыши - ПРАВАЯ
canvas.bind('<Button-2>', mause_click, '+')  # назначаем события кнопкам мыши - ЛЕВАЯ
canvas.bind('<Button-3>', mause_click, '*')  # назначаем события кнопкам мыши - СРЕДНЯЯ
root.mainloop()  # запуск главного окна


