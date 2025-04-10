from tkinter import Button, Scale, HORIZONTAL
from tkinter.colorchooser import askcolor

class Toolbar:
    """Создаёт панель управления инструментами."""

    def __init__(self, root, tool):
        self.root = root
        self.tool = tool

    def create_toolbar(self):
        self.pen_button = Button(self.root, text='Карандаш', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.eraser_button = Button(self.root, text='Ластик', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='Цвет', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.size_slider = Scale(self.root, from_=1, to=10, orient=HORIZONTAL, command=self.change_size)
        self.size_slider.set(5)
        self.size_slider.grid(row=0, column=3)

    def use_pen(self):
        self.tool.eraser_on = False

    def use_eraser(self):
        self.tool.use_eraser()

    def choose_color(self):
        color = askcolor(color=self.tool.color)[1]
        if color:
            self.tool.set_color(color)

    def change_size(self, value):
        self.tool.set_pen_size(int(value))