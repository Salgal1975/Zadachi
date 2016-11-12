# -*- coding: utf-8 -*-

import tkinter
import random

# constans
WIDTH = 640
HEIGHT = 480
BLACK_COLOR = 'black'
BG_COLOR = 'white'
BAD_COLOR = 'red'
ZERO = 0
MAIN_BALL_RADIUS = 30
MAIN_BALL_COLOR = 'blue'
INIT_DX = 1
INIT_DY = 1
DELAY = 1
COLORS = [BAD_COLOR, 'aqua', 'fuchsia', 'pink', BAD_COLOR, 'yellow', 'gold', BAD_COLOR, 'chartreuse']
NUM_OF_BALLS = 5

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
                           fill=self.color,
                           outline=self.color
                           if self.color != BAD_COLOR else BLACK_COLOR)    # цвет заполнения круга

    # метод прячем круг
    def hide(self):
        canvas.create_oval (self.x - self.r,
                            self.y - self.r,
                            self.x + self.r,
                            self.y + self.r,
                            fill=BG_COLOR,      # цвет заполнения круга
                            outline=BG_COLOR)   # цвет линии окружности

    # метод проверки сталкновений
    def is_collision(self, ball):
            a = abs (self.x + self.dx - ball.x)
            b = abs (self.y + self.dy - ball.y)
            return (a * a + b * b) ** 0.5 <= self.r + ball.r

    # метод движения круга
    def move(self):
        # callding with walls
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERO):
           self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
           self.dy = -self.dy
        # callding with ball
        for ball in balls:
            if self.is_collision(ball):
                if ball.color != BAD_COLOR:
                    ball.hide()
                    balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:
                    self.dx = self.dy = 0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()

# mause events
def mause_click(event):
    global main_ball # экземпляр класса Balls(), обьявляем глобальной
    if event.num == 1:
        if 'main_ball'not in globals():
            main_ball = Balls(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, INIT_DX, INIT_DY)
            main_ball.draw()
        else:  # turn left
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3:  # turn right
        if main_ball.dx * main_ball.dy > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy

# create list of ball
def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        next_ball = Balls(random.choice(range(0, WIDTH)),
                          random.choice(range(0, HEIGHT)),
                          random.choice(range(15, 35)),
                          random.choice(COLORS))
        lst.append(next_ball)
        next_ball.draw()
    return lst

# count of bad ball
def count_bad_balls(list_of_balls):
    res = 0
    for ball in list_of_balls:
        if ball.color == BAD_COLOR:
            res += 1
    return res


# main cicle game
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(balls) - num_of_bad_balls == 0:
            canvas.create_text(WIDTH / 2,
                               HEIGHT / 2,
                               text='Вы выиграли!!',
                               font="Arial 20",
                               fill=MAIN_BALL_COLOR)
            main_ball.dx = main_ball.dy = 0
        elif main_ball.dx == 0:
            canvas.create_text (WIDTH / 2,
                                HEIGHT / 2,
                                text='Вы проиграли!!',
                                font="Arial 20",
                                fill=BAD_COLOR)
    root.after(DELAY, main)

root = tkinter.Tk()  # экземпляр класса tkinter.Tk()-главне окно
root.title("Coding balls")  # название окна
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)  # свойства рабочего поля
canvas.pack()  # создает рабочее поле
canvas.bind('<Button-1>', mause_click)  # назначаем события кнопкам мыши - ЛЕВАЯ
canvas.bind('<Button-3>', mause_click, '*')  # назначаем события кнопкам мыши - ПРАВАЯ
if 'main_ball' in globals():
    del main_ball
balls = create_list_of_balls(NUM_OF_BALLS)
num_of_bad_balls = count_bad_balls(balls)

main()
root.mainloop()  # запуск главного окна


