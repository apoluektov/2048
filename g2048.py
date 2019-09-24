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
        moved = False
        merged = [False for _ in self.cells]
        for row in range(self.height - 2, -1, -1):
            for column in range(self.width):
                for next_row in range(row, self.height - 1):
                    move_to_y = next_row + 1
                    this = self.get(column, next_row)
                    if this == 0:
                        break
                    move_to = self.get(column, move_to_y)
                    if move_to == 0:
                        self.set(column, move_to_y, this)
                        self.set(column, next_row, 0)
                        moved = True
                    elif move_to == this and not merged[move_to_y * self.width + column]:
                        self.set(column, move_to_y, this * 2)
                        self.set(column, next_row, 0)
                        merged[move_to_y * self.width + column] = True
                        moved = True
                        break
        return moved

    def up(self):
        moved = False
        merged = [False for _ in self.cells]
        for row in range(0, self.height):
            for column in range(self.width):
                for next_row in range(row, 0, -1):
                    move_to_y = next_row - 1
                    this = self.get(column, next_row)
                    if this == 0:
                        break
                    move_to = self.get(column, move_to_y)
                    if move_to == 0:
                        self.set(column, move_to_y, this)
                        self.set(column, next_row, 0)
                        moved = True
                    elif move_to == this and not merged[move_to_y * self.width + column]:
                        self.set(column, move_to_y, this * 2)
                        self.set(column, next_row, 0)
                        merged[move_to_y * self.width + column] = True
                        moved = True
                        break
        return moved

    def right(self):
        moved = False
        merged = [False for _ in self.cells]
        for column in range(self.width - 1, -1, -1):
            for row in range(self.height):
                for next_column in range(column, self.width - 1):
                    move_to_x = next_column + 1
                    this = self.get(next_column, row)
                    if this == 0:
                        break
                    move_to = self.get(move_to_x, row)
                    if move_to == 0:
                        self.set(move_to_x, row, this)
                        self.set(next_column, row, 0)
                        moved = True
                    elif move_to == this and not merged[row * self.width + move_to_x]:
                        self.set(move_to_x, row, this * 2)
                        self.set(next_column, row, 0)
                        merged[row * self.width + move_to_x] = True
                        moved = True
                        break
        return moved

    def left(self):
        moved = False
        merged = [False for _ in self.cells]
        for column in range(self.width):
            for row in range(self.height):
                for next_column in range(column, 0, -1):
                    move_to_x = next_column - 1
                    this = self.get(next_column, row)
                    if this == 0:
                        break
                    move_to = self.get(move_to_x, row)
                    if move_to == 0:
                        self.set(move_to_x, row, this)
                        self.set(next_column, row, 0)
                        moved = True
                    elif move_to == this and not merged[row * self.width + move_to_x]:
                        self.set(move_to_x, row, this * 2)
                        self.set(next_column, row, 0)
                        merged[row * self.width + move_to_x] = True
                        moved = True
                        break
        return moved

    def set(self, x, y, n):
        self.cells[y * self.width + x] = n


def main():
    print("Hello, 2048!")


if __name__ == '__main__':
    main()
