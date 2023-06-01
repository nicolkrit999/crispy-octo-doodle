from pytamaro import *


# ratios may be changed in respect to one function to another
# all ellipse helper functions are based on 1.20 Length/Width ratio
# wings helper function is based on a 2.5 Length/Width ratio.

# function variable may be changed only if the ratio is respected
def main_black_body(short_axis) -> Graphic:
    return ellipse(short_axis, short_axis * 1.2, black)


# show_graphic(main_black_body(750))


# function variable may be changed only if the ratio is respected
def main_white_body(short_axis) -> Graphic:
    return ellipse(short_axis, short_axis * 1.2, white)


# show_graphic(main_white_body(100))


# an equilateral triangle does not have a ratio to respect for its sides
def feet(side_length) -> Graphic:
    return triangle(side_length, side_length, 60, yellow)


# show_graphic(feet(100))


def wings(short_axis) -> Graphic:
    return ellipse(short_axis, short_axis * 2.5, black)


# show_graphic(wings(100))


def eye(diameter) -> Graphic:
    return compose(pin(bottom_center, ellipse(diameter * 0.5, diameter * 0.5, black)),
                       pin(center, ellipse(diameter * 0.75, diameter * 0.75, white)))


show_graphic(eye(500))
