from pytamaro import *
import helper_functions as helper  # defines how the helper_functions.py file is called here


def penguin_shape(size) -> Graphic:  # the penguin size scale as needed
    return compose(pin(center_right, compose(pin(center, helper.wing(size / 2)),
                   pin(center_left, helper.body(size)))), helper.wing(size / 2))


show_graphic(penguin_shape(561))
