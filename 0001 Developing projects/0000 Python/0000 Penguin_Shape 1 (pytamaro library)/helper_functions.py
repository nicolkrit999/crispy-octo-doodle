from pytamaro import *


orange = rgb_color(255, 165, 0)

# ratios may be changed in respect to one function to another
# all ellipse helper functions are based on 1.20 Length/Width ratio
# wings helper function is based on a 2.5 Length/Width ratio.

# function variable may be changed only if the ratio is respected


def left_eye(radius) -> Graphic:
    return compose(pin(center_right,
                       overlay(ellipse(radius / 2, radius / 2, black), ellipse(radius, radius, white))),
                   pin(center_left, rectangle(radius / 2, radius, black)))


# show_graphic(left_eye(500))


def right_eye(radius) -> Graphic:
    return rotate(180, compose(pin(center_right,
                                   overlay(ellipse(radius / 2, radius / 2, black), ellipse(radius, radius, white))),
                               pin(center_left, rectangle(radius / 2, radius, black))))


# show_graphic(right_eye(500))


def beak(side_length) -> Graphic:
    return compose(pin(top_center, rotate(180, triangle(side_length, side_length * 2, 75.522, orange))),
                   pin(top_center, ellipse(side_length * 4, side_length * 5.5, white)))


# show_graphic(beak(100))


def eyes_beak(radius) -> Graphic:
    return compose(pin(bottom_center, beside(left_eye(radius / 2), right_eye(radius / 2))),
                   pin(top_center, beak(radius / 2.5)))


# show_graphic(eyes_beak(500))


def left_feet(side_length) -> Graphic:
    return rotate(-45, triangle(side_length, side_length, 60, orange))


# show_graphic(left_feet(100))


def right_feet(side_length) -> Graphic:
    return rotate(45, triangle(side_length, side_length, 60, orange))


def helper_circular_sector_white(radius, angle) -> Graphic:
    return circular_sector(radius, angle, white)


def feet_belly(side) -> Graphic:
    return compose(pin(bottom_right,
                       rotate(180, helper_circular_sector_white(side, 180))),
                   pin(top_left, right_feet(side)))


show_graphic(feet_belly(100))