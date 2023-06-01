from pytamaro import *

def pytamaro_logo(side1, color1, color2) -> Graphic:
    return compose(pin(bottom_right,
        (compose(rotate(180, pin(top_center, triangle(side1, side1, 60, color1))),
                 pin(bottom_left, triangle(side1 * 2, side1 * 2, 60, color2))))),
         rotate(180, pin(top_center, triangle(side1, side1, 60, color1))))


# show_graphic(pytamaro_logo(300, blue, red))


def prova_beside(side) -> Graphic:
    return beside(rectangle(side, side / 2, red), pytamaro_logo(side, blue, red))


# show_graphic(prova_beside(100))
