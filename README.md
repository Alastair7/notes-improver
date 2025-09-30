# NOTES-IMPROVER

Convierte documentos txt a markdown y luego se mejora el formato utilizando IA generativa.

## Cómo funciona?

Una carpeta de in donde contendrá ficheros txt y otra carpeta out con los documentos formateados y mejorados en md.

Cuando se ejecuta el script, va a leer en la carpeta de in los documentos uno por uno, y los va a mandar en los procesos de IA y el resultado se guardará en la carpeta out con el mismo nombre y extensión md.

## TODO

- Revisar librerías `markdown-full-yaml-metadata` y `python-frontmatter` y decidir cuál utilizar
- Añadir la lógica de `get_md_file_content` utilizando TDD.

## Propuestas

- Generar un index.md como resumen de cada nota: fecha de creación, título y un resumen en 2 lineas.
- Sincronizar notas con Obsidian, o poder sincronizarlas con alguna otra app para tenerlas disponibles siempre.
- Búsqueda de notas por keyword: A partir de keywords, devolver las notas que los incluyan.
- Búsqueda por tags.
- Notas temporales: Poder marcar una nota como temporal y que se borre al cabo de x tiempo.
- Shortcut para invocar el programa para acceder rápidamente a las notas.
- Poder encriptar notas.
- Al abrir el programa que aparezca el número de notas creadas y número total de espacio.
- Parsear una captura de pantalla sobre una nota y extraer el texto.

## Pendientes a decidir

- Cómo va a ser el flujo de los archivos
- Con qué IA vamos a hablar?
