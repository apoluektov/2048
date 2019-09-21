import unittest

from g2048 import Board


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


if __name__ == '__main__':
    unittest.main()
