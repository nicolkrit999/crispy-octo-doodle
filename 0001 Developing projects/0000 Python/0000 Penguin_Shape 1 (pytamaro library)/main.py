from pytamaro import *
import helper_functions as helper  # defines how the helper_functions.py file is called here


"""
# The short axis of the main black body defines the penguin dimension
# Changing this variable may result in the need to change most of the helper_functions ratios in the return statement
def penguin_shape_monco(short_axis) -> Graphic:
    return compose(pin(center_right,
                       compose(pin(top_center, helper.wings(short_axis / 2)),
                               pin(center_left, helper.body(short_axis)))),
                   pin(top_center, helper.wings(short_axis / 2)))


show_graphic(penguin_shape_monco(1000))
"""


def penguin_shape(size) -> Graphic:
    return compose(pin(center_right, compose(pin(center, helper.wing(size / 2)),
                   pin(center_left, helper.body(size)))), helper.wing(size / 2))


show_graphic(penguin_shape(561))
