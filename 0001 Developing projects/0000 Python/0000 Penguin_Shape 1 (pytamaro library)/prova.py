from pytamaro.it import *

orange = colore_rgb(255, 165, 0)


def occhio_sinistro(raggio: float) -> Grafica:
    assert raggio > 0
    return accanto(
        componi
        (fissa(alto_sinistra, ellipse(raggio / 3, raggio / 3, nero)),
         fissa(centro, ellisse(raggio, raggio, bianco))),
        rettangolo(raggio / 2, raggio, nero))


visualizza_grafica(occhio_sinistro(265))
