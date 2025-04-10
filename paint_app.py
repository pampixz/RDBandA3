from tkinter import Tk, Canvas
from tools.paint_tool import PaintTool
from ui.toolbar import Toolbar

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

class PaintApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Paint Application")

        self.canvas = Canvas(self.root, bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.grid(row=1, columnspan=4)

        self.tool = PaintTool(self.canvas)

        self.toolbar = Toolbar(self.root, self.tool)
        self.toolbar.create_toolbar()

        self.canvas.bind('<B1-Motion>', self.tool.paint)
        self.canvas.bind('<ButtonRelease-1>', self.tool.reset)

        self.root.mainloop()

if __name__ == '__main__':
    PaintApp()