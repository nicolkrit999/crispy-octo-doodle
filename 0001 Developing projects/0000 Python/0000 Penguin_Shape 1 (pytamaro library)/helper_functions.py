from pytamaro import *  # importing single elements may reduce compiling time


orange = rgb_color(255, 165, 0)  # rgb color definition for the feet and beak

# ratios may be changed in respect to one function to another
# function variable may be changed only if the function body is changed accordingly
# the dimensions do not respect a ratio however they scale well for any variable input value
# since every function call another one, starting grom the left_eye, pins may not be changed


def left_eye(radius: float) -> Graphic:
    assert radius > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert radius <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return beside(
        compose(pin(top_left,
                    ellipse(radius / 3, radius / 3, black)),
                pin(center,
                    ellipse(radius, radius, white))),
        rectangle(radius / 2, radius, black))  # the rectangle allow to distance the eyes


# show_graphic(left_eye(265.1))


def right_eye(radius: float) -> Graphic:
    assert radius > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert radius <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return beside(
        compose(pin(top_left,
                    ellipse(radius / 3, radius / 3, black)),
                pin(center,
                    ellipse(radius, radius, white))),
        rectangle(radius / 2, radius, black))  # the rectangle allow the pupils to not touch


# show_graphic(right_eye(500))


def beak_belly(side_length: float) -> Graphic:
    assert side_length > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert side_length <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    # the center of this function is the point of the beak
    return compose(pin(top_center,
                       rotate(180,  # rotating the beak now allow to not shift the center pin in other functions
                              triangle(side_length, side_length * 2, 75.522, orange))),  # the angle was computed
                   # with an online tool
                   pin(top_center,
                       ellipse(side_length * 5.2, side_length * 6, white)))


# show_graphic(beak_belly(500))


def eyes_beak_belly(radius: float) -> Graphic:  # putting together these 3 elements allows to have the belly as
    # center element
    assert radius > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert radius <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return compose(pin(bottom_center,
                       beside(
                           left_eye(radius / 2), right_eye(radius / 2))),
                   pin(top_center,
                       beak_belly(radius / 2.5)))


# show_graphic(eyes_beak_belly(500))


def right_foot(side_length: float) -> Graphic:  # the circular_sector is hidden by the belly,
    # however it is necessary to not have the feet touch each other in the final penguin shape
    assert side_length > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert side_length <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return compose(pin(top_left,
                       rotate(45,
                              triangle(side_length / 2, side_length / 2, 60, orange))),
                   pin(bottom_right,
                       rotate(-90,
                              circular_sector(side_length / 2, 90, white))))


# show_graphic(right_foot(500))


def left_foot(side_length: float) -> Graphic:  # using the right_foot allow the feet do be modified at the same time
    return rotate(-90,
                  right_foot(side_length))


# show_graphic(left_foot(500))


def feet(side_length: float) -> Graphic:  # necessary to not shift the bottom_center pin of the belly to the center
    # of the foot
    return beside(
        left_foot(side_length * 1.3),
        right_foot(side_length * 1.3))


# show_graphic(feet(500))


def wing(short_axis: float) -> Graphic:  # the height may be changed without problems
    assert short_axis > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert short_axis <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return ellipse(short_axis, short_axis * 2.5, black)


def beak_feet_belly_eyes(size: float) -> Graphic:  # allow to have the center of the belly to easily create the body
    assert size > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert size <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return compose(pin(bottom_center,
                       eyes_beak_belly(size / 1.2)),
                   pin(bottom_center,
                       feet(size)))

# show_graphic(beak_feet_belly_eyes(500))


def body_no_wings(size: float) -> Graphic:
    assert size > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert size <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return overlay(beak_feet_belly_eyes(size * 0.976),
                   pin(bottom_center,
                       ellipse(size * 2.23, size * 2.7, black)))


# show_graphic(body_no_wings(500))
