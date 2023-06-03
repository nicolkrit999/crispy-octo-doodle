from pytamaro import *
import helper_functions as helper  # defines how the helper_functions.py file is called here


def penguin_shape(size: float) -> Graphic:  # the penguin size scale as needed
    assert size >= 0
    return compose(pin(center_right, compose(pin(center, helper.wing(size / 2)),
                                                 pin(center_left, helper.body_no_wings(size)))), helper.wing(size / 2))


show_graphic(penguin_shape(10000))
