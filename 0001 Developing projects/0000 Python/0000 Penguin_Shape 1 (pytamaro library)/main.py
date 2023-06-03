from pytamaro import *
import helper_functions as helper  # defines how the helper_functions.py file is called here


def penguin_shape(size: float) -> Graphic:  # the penguin size scale as needed
    assert size >= 0  # a graphic with value 0 is possible but not visible
    assert size >= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return compose(pin(center_right, compose(pin(center, helper.wing(size / 2)),  # wings size may be changed
                                             pin(center_left,
                                                 helper.body_no_wings(size)))), helper.wing(size / 2))


show_graphic(penguin_shape(1000))
