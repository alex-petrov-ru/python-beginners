import tkinter

WIDTH = 640
HEIGHT = 480
BG_COLLOR = 'white'
R_BALL = 30
COLLOR_BALL = 'blue'


class Balls:
    def __init__(self, x, y, r, collor, dx=0, dy=0):
        self.x = x  # координаты х
        self.y = y  # координаты у
        self.r = r  # радиус шарика
        self.collor = collor  # цвет шарика
        self.dx = dx  # смещение шарика по х
        self.dy = dy  # смещение шарика по у

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                           fill=self.collor)


def mouse_click(event):
    main_ball = Balls(event.x, event.y, R_BALL, COLLOR_BALL)
    main_ball.draw()


root = tkinter.Tk()
root.title('Coliding balls')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLLOR)
canvas.pack()
canvas.bind('<Button - 1>', mouse_click)
canvas.bind('<Button - 2>', mouse_click, '+')
canvas.bind('<Button - 3>', mouse_click, '+')
root.mainloop()