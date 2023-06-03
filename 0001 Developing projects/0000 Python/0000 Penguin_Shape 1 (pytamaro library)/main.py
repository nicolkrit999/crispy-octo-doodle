from pytamaro import *  # importing single elements may reduce compiling time
import helper_functions as helper  # defines how the helper_functions.py file is called here


# the penguin may be created with 2 methods, 2 different functions ("input_penguin_shape" or "penguin_shape")
# the comments at lines 15-16 and 24-25 explain the difference

# all variables define the area of the graphic. Formulas like 1 * 500 may be used as long as the result is a floating
# point number

# forced variables type may be changed to int (natural numbers) or
# removed (may lead to errors if the input is not an int or a floating point number


# this function display the graphic by asking the user to input the desired area of the penguin in the terminal
# to use this version comment "show_graphic(penguin_shape(500))"at line 35
def input_penguin_shape():
    return show_graphic(helper.penguin_complete_shape_input())


show_graphic(input_penguin_shape())


# this function display the graphic by changing the value inside "show_graphic(penguin_shape()"at line 33
# to use this version comment "show_graphic(input_penguin_shape(500))"at line 21
def penguin_shape(area) -> Graphic:  # size scale as needed. A size over 1000 may take some time to
    # compile
    assert area > 0, "A Graphic with area 0 is the same as empty_graphic()"
    assert area <= 1.7976931348623157e+308  # maximum float size accepted by python (64-bit double-precision)
    return compose(pin(center_right, compose(pin(center, helper.wing(area / 2.5)),  # wings size may be changed
                                             pin(center_left,
                                                 helper.body_no_wings(area)))), helper.wing(area / 2.5))


# show_graphic(penguin_shape(500))
