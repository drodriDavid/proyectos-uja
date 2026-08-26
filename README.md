# Panel de proyectos · UJA

Un sitio para los nueve proyectos activos: qué es cada uno, cuál es mi papel, en qué punto
está, qué vence, dónde vive el código y por dónde se entra.

Es la puerta de arriba. Dos de los proyectos tienen además cuaderno propio, con la misma
mecánica de acceso:

- [Cuaderno de REGEN4ANDALUCIA](https://drodridavid.github.io/regen4andalucia-uja/)
- [Cuaderno de LivingSoiLL](https://drodridavid.github.io/livingsoill-cuaderno/)

Seis vistas: proyectos, panel de situación, agenda de plazos, tareas, notas y bitácora.

## Cómo se entra

Se entra **con cuenta de Google**. No hay contraseña que escribir.

El repositorio es público porque GitHub Pages lo exige, así que `index.html` no contiene el
documento en claro: contiene el documento cifrado con **AES-256-GCM**, con la clave derivada
mediante **PBKDF2-HMAC-SHA256** (400.000 iteraciones). Sin la clave, lo que hay aquí es ruido.

La clave vive en `clave-cuaderno.txt`, dentro de la carpeta de Drive **Cuaderno Proyectos
(UJA)**. Al entrar, la portada pide acceso a Drive, busca esa carpeta, lee la clave y descifra
la página en el propio navegador.

A diferencia de los dos cuadernos de proyecto, **este panel es personal**: la carpeta no se
comparte con nadie.

Recargar no vuelve a pedir Google: la clave con la que se entró se queda en la pestaña y muere
al cerrarla.

## Sincronización

Se conecta solo al entrar y guarda en `panel-proyectos-uja.json`, en esa misma carpeta de
Drive, a los pocos segundos de cada cambio. Usa el mismo ID de cliente OAuth que los otros
dos, porque el origen autorizado (`https://drodridavid.github.io`) los cubre todos.

## Qué contiene

Los nueve proyectos salen del vault de Obsidian, con su color de lomo, sus cifras, sus plazos
y lo que hay que vigilar en cada uno. La **agenda** junta todos los plazos con fecha —los de
los proyectos y los de las tareas— en una sola línea de tiempo, y se exporta a `.ics` para el
calendario.

Las tareas, notas y entradas de bitácora se etiquetan por proyecto y heredan su color.

## Cómo se construye

El documento en claro se arma a partir de cuatro piezas:

    _p1.html       estilo y cabecera
    _p2.html       las seis vistas
    _p3.html       el script
    proyectos.js   los nueve proyectos

    python montar.py
    python build.py fuente.html --pass "$(cat clave.txt)"

`build.py` cifra `fuente.html` y lo envuelve en la portada `puerta.html`, produciendo
`index.html`, que es lo único que se publica. Las cuatro piezas, `fuente.html` y `clave.txt`
están ignorados por git: juntos reconstruyen todo el contenido y el repositorio es público.

Antes de cifrar, `node --check` sobre el `<script>` de `fuente.html` y de `puerta.html`.

## Publicar cambios

    cd C:/ProyectosUJA/proyectos-uja
    .\publicar.ps1          # PowerShell
    ./publicar.sh           # Git Bash

La clave se lee de `clave.txt`. Si la cambias, borra `clave-cuaderno.txt` de la carpeta de
Drive y entra una vez para dejar la nueva.

En **Windows PowerShell 5.1** el operador `&&` no existe; encadena con `;`.

## Identidad

Neutra a propósito: el chasis va en grafito y el color lo pone cada proyecto en su lomo, para
que se distingan de un vistazo. La marca son cuatro pestañas de archivador sobre una caja.
Todos los pares de color verificados sobre WCAG AA en tema claro y oscuro, mínimo 4,92; los
nueve colores de lomo superan 5:1 contra blanco.
