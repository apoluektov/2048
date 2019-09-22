class Board:
    # first row is top row, first column is left column
    # cells[0] is top-left corner element, cells[w] is second row leftmost element
    def __init__(self, cells, w, h):
        assert w > 1 and h > 1
        assert len(cells) == w * h
        self.cells = cells.copy()
        self.width = w
        self.height = h

    def get(self, x, y):
        assert 0 <= x < self.width
        assert 0 <= y < self.height
        return self.cells[y * self.width + x]

    def down(self):
        merged = [False for _ in self.cells]
        for row in range(self.height - 2, -1, -1):
            for column in range(self.width):
                y = row
                while y < self.height - 1:
                    this = self.get(column, y)
                    below = self.get(column, y + 1)
                    if below == 0:
                        self.set(column, y + 1, this)
                        self.set(column, y, 0)
                    elif below == this and not merged[(y + 1) * self.width + column]:
                        self.set(column, y + 1, this * 2)
                        self.set(column, y, 0)
                        merged[(y + 1) * self.width + column] = True
                        break

                    y += 1

    def up(self):
        merged = [False for _ in self.cells]
        for row in range(0, self.height):
            for column in range(self.width):
                y = row
                while y > 0:
                    this = self.get(column, y)
                    above = self.get(column, y - 1)
                    if above == 0:
                        self.set(column, y - 1, this)
                        self.set(column, y, 0)
                    elif above == this and not merged[(y - 1) * self.width + column]:
                        self.set(column, y - 1, this * 2)
                        self.set(column, y, 0)
                        merged[(y - 1) * self.width + column] = True
                        break

                    y -= 1


    def set(self, x, y, n):
        self.cells[y * self.width + x] = n


def main():
    print("Hello, 2048!")


if __name__ == '__main__':
    main()
