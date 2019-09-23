import unittest

from g2048 import Board
import utils


class SmokeTest(unittest.TestCase):
    def test(self):
        cells_init = [
            2, 2, 2, 2,
            0, 2, 2, 2,
            2, 2, 0, 4,
            0, 2, 2, 8
        ]

        cells_turn1_down = [
            0, 0, 0, 0,
            0, 0, 0, 4,
            0, 4, 2, 4,
            4, 4, 4, 8
        ]

        cells_turn2_up = [
            4, 8, 2, 8,
            0, 0, 4, 8,
            0, 0, 0, 0,
            0, 0, 0, 0
        ]

        cells_turn1_right = [
            0, 0, 4, 4,
            0, 0, 2, 4,
            0, 0, 4, 4,
            0, 0, 4, 8
        ]

        cells_turn2_left = [
            8, 0, 0, 0,
            2, 4, 0, 0,
            8, 0, 0, 0,
            4, 8, 0, 0
        ]

        b = Board(cells_init, 4, 4)

        b.down()
        self.assertEqual(4, b.width)
        self.assertEqual(4, b.height)
        self.assertEqual(cells_turn1_down, b.cells)

        b.up()
        self.assertEqual(4, b.width)
        self.assertEqual(4, b.height)
        self.assertEqual(cells_turn2_up, b.cells)

        b = Board(cells_init, 4, 4)

        b.right()
        self.assertEqual(4, b.width)
        self.assertEqual(4, b.height)
        self.assertEqual(cells_turn1_right, b.cells)

        b.left()
        self.assertEqual(4, b.width)
        self.assertEqual(4, b.height)
        self.assertEqual(cells_turn2_left, b.cells)

    def test_html(self):
        cells = [
            0, 0, 0, 0,
            0, 0, 0, 4,
            0, 4, 2, 4,
            4, 4, 4, 8
        ]

        b = Board(cells, 4, 4)

        s = utils.to_html(b)
        self.assertEqual("<html><body><table>"
                         "<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>"
                         "<tr><td>0</td><td>0</td><td>0</td><td>4</td></tr>"
                         "<tr><td>0</td><td>4</td><td>2</td><td>4</td></tr>"
                         "<tr><td>4</td><td>4</td><td>4</td><td>8</td></tr>"
                         "</table></body></html>",
                         s)


if __name__ == '__main__':
    unittest.main()
