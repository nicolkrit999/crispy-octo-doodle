from pytamaro import *


orange = rgb_color(255, 165, 0)  # rgb color definition for the feet and beak

# ratios may be changed in respect to one function to another
# function variable may be changed only if the function body is changed accordingly
# the dimensions do not respect a ratio however they scale well for any variable input value


def left_eye(radius) -> Graphic:
    return compose(pin(center_right,  # pinning the eye with the rectangle is necessary
                       overlay(ellipse(radius / 2, radius / 2, black), ellipse(radius, radius, white))),
                   pin(center_left, rectangle(radius / 2, radius, black)))  # rectangle allow the pupils to not touch


# show_graphic(left_eye(500))


def right_eye(radius) -> Graphic:  # using the left_eye allow the eyes do be modified at the same time
    return rotate(180,
                  left_eye(radius))


# show_graphic(right_eye(500))


def beak_belly(side_length) -> Graphic:
    return compose(pin(top_center,
                       rotate(180,  # rotating the beak now allow to not shift the center pin in other functions
                              triangle(side_length, side_length * 2, 75.522, orange))),  # the angle was computed
                   # with an online tool
                   pin(top_center, ellipse(side_length * 4, side_length * 5.5, white)))


# show_graphic(beak_belly(100))


def eyes_beak_belly(radius) -> Graphic:  # putting together these 3 elements allows to have the belly as center element
    return compose(pin(bottom_center, beside(left_eye(radius / 2), right_eye(radius / 2))),
                   pin(top_center, beak_belly(radius / 2.5)))


# show_graphic(eyes_beak_belly(500))


# show_graphic(left_feet(100))


def right_foot(side_length) -> Graphic:  # the circular_sector is hidden by the belly,
    # however it is necessary to not have the feet touch each other in the final penguin shape
    return compose(pin(top_left, rotate(45, triangle(side_length / 2, side_length / 2, 60, orange))),
                   pin(bottom_right, rotate(-90, circular_sector(side_length / 2, 90, white))))


# show_graphic(right_foot(500))


def left_foot(side_length) -> Graphic:  # using the right_foot allow the feet do be modified at the same time
    return rotate(-90, right_foot(side_length))


# show_graphic(left_foot(500))


def feet(side_length) -> Graphic:  # necessary to not shift the bottom_center pin of the belly to the center of the foot
    return beside(left_foot(side_length), right_foot(side_length))


# show_graphic(feet(500))


def wing(short_axis) -> Graphic:  # the height may be changed without problems
    return ellipse(short_axis, short_axis * 2.5, black)


def beak_feet_belly_eyes(side) -> Graphic:  # allow to have the center of the belly to easily create the body
    return compose(pin(bottom_center, eyes_beak_belly(side / 1.2)),
                   pin(bottom_center, feet(side)))

# show_graphic(beak_feet_belly_eyes(100))


def body_no_wings(size) -> Graphic:
    return compose(pin(bottom_center, beak_feet_belly_eyes(size)),
                   pin(bottom_center, ellipse(size * 2.35, size * 2.6, black)))


# show_graphic(body(200))
