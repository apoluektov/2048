import unittest

from g2048 import Board
import utils


class SmokeTest(unittest.TestCase):
    def test_smoke(self):
        w = 4
        h = 4

        cells_before = [
            2, 2, 2, 2,
            0, 2, 2, 2,
            2, 2, 0, 4,
            0, 2, 2, 8
        ]

        cells_after = [
            0, 0, 0, 0,
            0, 0, 0, 4,
            0, 4, 2, 4,
            4, 4, 4, 8
        ]

        b = Board(cells_before, w, h)
        b.down()

        self.assertEqual(b.width, w)
        self.assertEqual(b.height, h)

        self.assertEqual(b.cells, cells_after)

        s = utils.to_html(b)
        self.assertEqual(s, "<html><body><table><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>4</td></tr><tr><td>0</td><td>4</td><td>2</td><td>4</td></tr><tr><td>4</td><td>4</td><td>4</td><td>8</td></tr></table></body></html>")


if __name__ == '__main__':
    unittest.main()
