from pytamaro import *
import helper_functions as helper  # defines how the helper_functions.py file is called here


# The short axis of the main black body defines the penguin dimension
# Changing this variable may result in the need to change most of the helper_functions ratios in the return statement
def penguin_shape(short_axis) -> Graphic:
    return overlay(helper.main_white_body(short_axis * 0.75), helper.main_black_body(short_axis))

# show_graphic(penguin_shape(1000))
