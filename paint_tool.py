from tkinter import ROUND, TRUE

DEFAULT_PEN_SIZE = 5
DEFAULT_COLOR = 'black'

class PaintTool:
    """Отвечает за логику рисования (кисть, цвет, ластик)."""

    def __init__(self, canvas):
        self.canvas = canvas
        self.old_x = None
        self.old_y = None
        self.line_width = DEFAULT_PEN_SIZE
        self.color = DEFAULT_COLOR
        self.eraser_on = False

    def set_pen_size(self, size):
        self.line_width = size

    def set_color(self, color):
        self.eraser_on = False
        self.color = color

    def use_eraser(self):
        self.eraser_on = True

    def paint(self, event):
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(
                self.old_x, self.old_y, event.x, event.y,
                width=self.line_width, fill=paint_color,
                capstyle=ROUND, smooth=TRUE, splinesteps=36
            )
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None