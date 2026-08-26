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

# Nada en claro vive en este repositorio, que es publico. Las piezas y la clave
# estan en el repositorio privado de fuentes, al lado.
FUENTES = os.path.join(os.path.dirname(AQUI), "fuentes", os.path.basename(AQUI))
if not os.path.isdir(FUENTES):
    raise SystemExit(
        "No encuentro las fuentes en %s.\n"
        "Clona el repositorio privado de fuentes en la carpeta 'fuentes',\n"
        "al lado de este repositorio." % FUENTES)


def lee(n):
    """Las piezas estan en las fuentes; lo que sea del repo, en el repo."""
    d = AQUI if n == "logo.b64" else FUENTES
    return io.open(os.path.join(d, n), encoding="utf-8").read()


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

    io.open(os.path.join(FUENTES, "fuente.html"), "w", encoding="utf-8").write(doc)
    print("fuente.html: %d bytes" % len(doc.encode("utf-8")))


if __name__ == "__main__":
    sys.exit(main())
