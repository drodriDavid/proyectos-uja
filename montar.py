#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma fuente.html a partir de las tres partes y de los datos de los proyectos.

Las partes se llevan aparte porque el fichero completo pasa de los 100 KB y
asi cada trozo (estilo, vistas, script) se edita sin tocar los demas.
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def lee(n):
    return io.open(os.path.join(AQUI, n), encoding="utf-8").read()


def main():
    fincas = lee("proyectos.js").rstrip("\n")
    p1, p2, p3 = lee("_p1.html"), lee("_p2.html"), lee("_p3.html")

    assert p3.count("__PROYECTOS__") == 1, "falta el hueco de los proyectos"
    p3 = p3.replace("__PROYECTOS__", fincas)

    doc = p1 + p2 + p3

    # El fragmento se cifra entero, asi que build.py no llega a sustituir aqui:
    # el logo se incrusta ahora.
    # Este panel no lleva logo de mapa de bits: su marca va en SVG en linea.
    assert "__LOGO__" not in doc, "aqui no deberia quedar hueco de logo"

    io.open(os.path.join(AQUI, "fuente.html"), "w", encoding="utf-8").write(doc)
    print("fuente.html: %d bytes" % len(doc.encode("utf-8")))


if __name__ == "__main__":
    sys.exit(main())
