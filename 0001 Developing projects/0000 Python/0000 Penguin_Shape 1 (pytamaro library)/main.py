from pytamaro import *  # importing single elements may reduce compiling time
import helper_functions as helper  # defines how the helper_functions.py file is called here


def penguin_shape(size: float) -> Graphic | str:  # size scale as needed. A size over 1000 may take some time to compile
    assert size > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert size <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return compose(pin(center_right, compose(pin(center, helper.wing(size / 2)),  # wings size may be changed
                                             pin(center_left,
                                                 helper.body_no_wings(size)))), helper.wing(size / 2))


show_graphic(penguin_shape(300))
