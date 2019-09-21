from g2048 import Board


def to_html(board):
    s = "<html><body><table>"
    for y in range(board.height):
        s += "<tr>"
        for x in range(board.width):
            s += "<td>"
            s += str(board.get(x, y))
            s += "</td>"
        s += "</tr>"
    s += "</table></body></html>"
    return s
