from collections import defaultdict
from random import randint


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
        for row in range(self.height - 1, -1, -1):
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

    def is_game_over(self):
        for x in range(self.width):
            for y in range(self.height):
                n = self.get(x, y)
                if n == 0:
                    return False
                if x > 0 and self.get(x - 1, y) == n:
                    return False
                if x < self.width - 1 and self.get(x + 1, y) == n:
                    return False
                if y > 0 and self.get(x, y - 1) == n:
                    return False
                if y < self.height - 1 and self.get(x, y + 1) == n:
                    return False
        return True


def empty_board():
    return Board([0 for _ in range(16)], 4, 4)


def random_new_val():
    # 90% 2, 10% 4
    if randint(0, 9) == 0:
        return 4
    else:
        return 2


def random_new_cell(board):
    # found all empty cells
    # randomly chose one of them
    empties = []
    for i, c in enumerate(board.cells):
        if c == 0:
            empties.append(i)
    x = randint(0, len(empties) - 1)
    return empties[x]


def run_game(actor):
    b = empty_board()
    b.cells[random_new_cell(b)] = random_new_val()
    b.cells[random_new_cell(b)] = random_new_val()
    #print_board(b)
    while not b.is_game_over():
        if not actor.next_move(b):
            # illegal move tried
            raise ValueError
        b.cells[random_new_cell(b)] = random_new_val()
        #print_board(b)
    return max(b.cells)


def print_board(b):
    for y in range(b.height):
        for x in range(b.width):
            print('{:>5}'.format(b.get(x, y)), end='')
        print()
    print()


class HumanActor:
    def next_move(self, board):
        while True:
            s = input('your move: ')
            if s == '' or s not in 'udlr':
                continue
            if s == 'u':
                if not board.up():
                    continue
            if s == 'd':
                if not board.down():
                    continue
            if s == 'l':
                if not board.left():
                    continue
            if s == 'r':
                if not board.right():
                    continue
            return True


class StupidActor:
    # plays down, right, down, right, ...
    # if not possible -- tries up and left in order

    def __init__(self):
        self.prev = None

    def next_move(self, board):
        if self.prev != 'down' and board.down():
            self.prev = 'down'
        elif self.prev != 'right' and board.right():
            self.prev = 'right'
        elif self.prev != 'left' and board.left():
            self.prev = 'left'
        elif self.prev != 'up' and board.up():
            self.prev = 'up'
        else:
            # try whatever is possible
            if board.down():
                self.prev = 'down'
            elif board.right():
                self.prev = 'right'
            elif board.left():
                self.prev = 'left'
            elif board.up():
                self.prev = 'up'
            else:
                assert False

        return True


def main():
    d = defaultdict(int)
    for i in range(10000):
        max_ = run_game(StupidActor())
        d[max_] += 1
        if (i + 1) % 100 == 0:
            print(i + 1)
    print(sorted(d.items()))


if __name__ == '__main__':
    main()
