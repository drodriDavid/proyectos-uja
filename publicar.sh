#!/bin/sh
# Recifra el panel y lo publica en GitHub Pages.
#
#   ./publicar.sh                 -> mantiene la clave actual
#   ./publicar.sh "CLAVE-NUEVA"   -> ademas cambia la clave
#
# La clave se guarda en clave.txt, que git ignora: el repositorio es publico
# y ahi dentro no puede haber nada que abra el panel.

set -e
cd "$(dirname "$0")"

# Nada en claro vive aqui: las piezas y la clave estan en el repositorio
# privado de fuentes, al lado de este.
FUENTES="../fuentes/$(basename "$PWD")"
if [ ! -d "$FUENTES" ]; then
  echo "ERROR: no encuentro las fuentes en $FUENTES" >&2
  echo "       Clona el repositorio privado de fuentes al lado de este." >&2
  exit 1
fi

CLAVE="$1"
if [ -z "$CLAVE" ]; then
  if [ ! -f "$FUENTES/clave.txt" ]; then
    echo "ERROR: falta clave.txt y no has pasado ninguna clave." >&2
    exit 1
  fi
  CLAVE=$(tr -d ' \t\r\n' < "$FUENTES/clave.txt")
fi

echo "-> Montando fuente.html..."
python montar.py

echo "-> Cifrando fuente.html..."
python build.py "$FUENTES/fuente.html" --pass "$CLAVE"
printf '%s' "$CLAVE" > "$FUENTES/clave.txt"

echo "-> Publicando..."
git add -A
if git diff --cached --quiet; then
  echo "   (nada que confirmar)"
else
  git commit -q -m "Actualiza el panel"
fi
git push -q origin main

echo
echo "Publicado en https://drodridavid.github.io/proyectos-uja/"
echo "Si has cambiado la clave, borra clave-panel.txt de la carpeta de Drive"
echo "'Cuaderno Proyectos (UJA)' y vuelve a entrar para dejar la nueva."
