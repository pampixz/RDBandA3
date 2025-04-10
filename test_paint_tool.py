import unittest
from unittest.mock import Mock
from tools.paint_tool import PaintTool


class TestPaintTool(unittest.TestCase):
    def setUp(self):
        self.canvas_mock = Mock()
        self.tool = PaintTool(self.canvas_mock)

    def test_set_pen_size(self):
        self.tool.set_pen_size(7)
        self.assertEqual(self.tool.line_width, 7)

    def test_set_color(self):
        self.tool.set_color("blue")
        self.assertEqual(self.tool.color, "blue")
        self.assertFalse(self.tool.eraser_on)

    def test_use_eraser(self):
        self.tool.use_eraser()
        self.assertTrue(self.tool.eraser_on)

    def test_reset_coordinates(self):
        self.tool.old_x = 100
        self.tool.old_y = 200
        self.tool.reset(None)
        self.assertIsNone(self.tool.old_x)
        self.assertIsNone(self.tool.old_y)

    def test_paint_draws_line_with_pen(self):
        self.tool.old_x = 10
        self.tool.old_y = 20
        event = Mock()
        event.x = 30
        event.y = 40

        self.tool.eraser_on = False
        self.tool.color = "red"
        self.tool.line_width = 5
        self.tool.paint(event)

        self.canvas_mock.create_line.assert_called_with(
            10, 20, 30, 40,
            width=5,
            fill="red",
            capstyle="round",
            smooth=True,
            splinesteps=36
        )

    def test_paint_draws_line_with_eraser(self):
        self.tool.old_x = 15
        self.tool.old_y = 25
        event = Mock()
        event.x = 35
        event.y = 45

        self.tool.eraser_on = True
        self.tool.paint(event)

        self.canvas_mock.create_line.assert_called_with(
            15, 25, 35, 45,
            width=self.tool.line_width,
            fill="white",
            capstyle="round",
            smooth=True,
            splinesteps=36
        )


if __name__ == '__main__':
    unittest.main()