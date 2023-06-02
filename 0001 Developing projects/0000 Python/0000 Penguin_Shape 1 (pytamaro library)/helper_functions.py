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


def eyes_beak_belly(radius) -> Graphic:
    return compose(pin(bottom_center, beside(left_eye(radius / 2), right_eye(radius / 2))),
                   pin(top_center, beak(radius / 2.5)))


# show_graphic(eyes_beak_belly(500))


# show_graphic(left_feet(100))


def right_foot(side_length) -> Graphic:
    return compose(pin(top_left, rotate(45, triangle(side_length / 2, side_length / 2, 60, orange))),
                   pin(bottom_right, rotate(-90, circular_sector(side_length / 2, 90, white))))


# show_graphic(right_foot(500))


def left_foot(side_length) -> Graphic:
    return rotate(-90, right_foot(side_length))


# show_graphic(left_foot(500))


def feet(side_length) -> Graphic:
    return beside(left_foot(side_length), right_foot(side_length))


# show_graphic(feet(500))


def wing(short_axis) -> Graphic:
    return ellipse(short_axis, short_axis * 2.5, black)


def helper_circular_sector_white(radius, angle) -> Graphic:
    return circular_sector(radius, angle, white)


def beak_feet_belly_eyes(side) -> Graphic:
    return compose(pin(bottom_center, feet(side)), pin(bottom_center, eyes_beak_belly(side / 1.2)))


# show_graphic(beak_feet_belly_eyes(100))


def wings(size) -> Graphic:
    return compose(pin(top_right,
                       compose(pin(top_center, wing(size)),
                               pin(top_left, rectangle(size * 2, size * 2, black)))),
                   pin(top_center, wing(size)))


# show_graphic(wings(100))


def top(size) -> Graphic:
    return overlay(beak_feet_belly_eyes(size),
                 wings(size))


show_graphic(top(500))

