from pytamaro import *


orange = rgb_color(255, 165, 0)

# ratios may be changed in respect to one function to another
# all ellipse helper functions are based on 1.20 Length/Width ratio
# wings helper function is based on a 2.5 Length/Width ratio.

# function variable may be changed only if the ratio is respected


def main_black_oval(short_axis) -> Graphic:
    return ellipse(short_axis, short_axis * 1.2, black)


# show_graphic(main_black_oval(750))


# function variable may be changed only if the ratio is respected
def main_white_oval(short_axis) -> Graphic:
    return ellipse(short_axis, short_axis * 1.2, white)


# show_graphic(main_white_oval(100))


# an equilateral triangle does not have a ratio to respect for its sides
def feet(side_length) -> Graphic:
    return triangle(side_length, side_length, 60, orange)


# show_graphic(feet(100))


def left_feet(side_length) -> Graphic:
    return rotate(-45, triangle(side_length, side_length, 60, orange))


# show_graphic(left_feet(100))


def right_feet(side_length) -> Graphic:
    return rotate(45, triangle(side_length, side_length, 60, orange))


# show_graphic(right_feet(100))


def beak(side_length) -> Graphic:
    return rotate(180, triangle(side_length, side_length * 2, 75.522, orange))


# show_graphic(beak(500))


def wings(short_axis) -> Graphic:
    return ellipse(short_axis, short_axis * 2.5, black)


# show_graphic(wings(100))


def left_half_eye(diameter) -> Graphic:
    return rotate(90, compose(pin
                              (bottom_right, circular_sector(diameter / 2.25, 180, black)),
                              circular_sector(diameter, 180, white)))


# show_graphic(left_half_eye(500))


def right_half_eye(diameter) -> Graphic:
    return rotate(-90, compose(pin(bottom_left,
                                   circular_sector(diameter / 2.25, 180, black)),
                               circular_sector(diameter, 180, white)))


# show_graphic(right_half_eye(500))


def eye(diameter) -> Graphic:
    return beside(left_half_eye(diameter), right_half_eye(diameter))


# show_graphic(eye(500))


def penguin_top_left(diameter) -> Graphic:
    return beside(compose(pin(bottom_right, eye(diameter / 3)),
                          pin(bottom_right, rotate(90, circular_sector(diameter, 90, black)))),
                  rectangle(diameter / 2, diameter, black), )


# show_graphic(penguin_top_left(500))


def penguin_top_right(diameter) -> Graphic:
    return beside(rectangle(diameter / 2, diameter, black),
                  compose(pin(bottom_left, eye(diameter / 3)), pin(bottom_left, circular_sector(diameter, 90, black))))


# show_graphic(penguin_top_right(500))


def penguin_top_portion(diameter) -> Graphic:
    return compose(pin(bottom_center,
                       (beside(penguin_top_left(diameter / 2),
                               penguin_top_right(diameter / 2)))),
                   circular_sector(diameter, 180, black))


# show_graphic(penguin_top_portion(500))

"""
def penguin_black_body_no_wings(diameter) -> Graphic:
    return compose(pin(top_center, penguin_top_portion(diameter)),
                   pin(top_center, main_black_oval(diameter * 2)))

# show_graphic(penguin_black_body_no_wings(500))
"""

def belly_beak(diameter) -> Graphic:
    return compose(pin(center, beak(diameter / 5)),
                   pin(top_center, main_white_oval(diameter * 1.25)))


# show_graphic(belly_beak(500))


def body_without_feet(diameter) -> Graphic:
    return compose(pin(top_center, belly_beak(diameter)),
                   pin(bottom_center, penguin_top_portion(diameter)))


# show_graphic(body_without_feet(500))


def body_no_wings(diameter) -> Graphic:
    return overlay(body_without_feet(diameter / 1.5),
                   ellipse(diameter * 1.7, diameter * 2, black))


show_graphic(body_no_wings(500))



