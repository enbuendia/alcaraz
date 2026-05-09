import os, re

nueva_cabecera = '''<div id="cabecera">
    <div id="cabecera-titulo">TRUFAMANIA</div>
    <div id="cabecera-subtitulo">Pasion por la trufa</div>
</div>'''

patron = re.compile(r'<div id="cabecera">.*?</div>\s*</div>', re.DOTALL)

for nombre in os.listdir('.'):
    if nombre.endswith('.htm'):
        with open(nombre, 'r') as f:
            contenido = f.read()
        nuevo = patron.sub(nueva_cabecera, contenido, count=1)
        if nuevo != contenido:
            with open(nombre, 'w') as f:
                f.write(nuevo)
            print('Modificado: ' + nombre)
