from pytamaro import *
import main as main

def prova() -> Graphic:
    return beside(main.pytamaro_logo(25, blue, red), rectangle(100, 50, yellow))

show_graphic(prova())