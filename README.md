# NOTES-IMPROVER

Convierte documentos txt a markdown y luego se mejora el formato utilizando IA generativa.

## Cómo funciona?

Una carpeta de in donde contendrá ficheros txt y otra carpeta out con los documentos formateados y mejorados en md.

Cuando se ejecuta el script, va a leer en la carpeta de in los documentos uno por uno, y los va a mandar en los procesos de IA y el resultado se guardará en la carpeta out con el mismo nombre y extensión md.

## CLI

**Es necesario declarar la variable de entorno: `export NOTES_DIR=$HOME/notes/`**

Varios comandos donde cada uno tendrá sus subcomandos que permitirán hacer ciertas acciones como por ejemplo:

`notes sync`: Ejecuta el script para convertir los ficheros de `in/` a `out/` en formato .md y mejorados por la IA.

`notes search 'Text to find in any note'` esto devolvería el listado de ficheros donde se encuentra el texto.

`notes keywords`: Devuelve el contenido de los ficheros donde coincidan sus keywords.

`notes get --path`: Devuelve el contenido del fichero indicado. 

## Sistema de ficheros

 En la carpeta HOME del usuario, existirá la carpeta `notes/in` para añadir ficheros .txt.
 La carpeta `notes/out` contendrá las notas ya parseadas y esta carpeta estará registrada mediante variable de entorno.

## TODO

- [x] Crear función de utilidad para buscar mediante configuración la carpeta de las notas
- [x] Decidir cómo hacer el sistema de ficheros
- [x] Adaptar el test de search_notes_by_text para llamar a la función directamente sin pasar por click. 


PREV
- [x] Revisar librerías `markdown-full-yaml-metadata` y `python-frontmatter` y decidir cuál utilizar
- [x] Añadir la lógica de `get_md_file_content` utilizando TDD.

## Propuestas

- Generar un index.md como resumen de cada nota: fecha de creación, título y un resumen en 2 lineas.
- Sincronizar notas con Obsidian, o poder sincronizarlas con alguna otra app para tenerlas disponibles siempre.
- (WIP) Búsqueda de notas por keyword: A partir de keywords, devolver las notas que los incluyan.
- Búsqueda por tags.
- Notas temporales: Poder marcar una nota como temporal y que se borre al cabo de x tiempo.
- Shortcut para invocar el programa para acceder rápidamente a las notas.
- Poder encriptar notas.
- Al abrir el programa que aparezca el número de notas creadas y número total de espacio.
- Parsear una captura de pantalla sobre una nota y extraer el texto.

## Pendientes a decidir

- Cómo va a ser el flujo de los archivos
- Con qué IA vamos a hablar?
- Cómo se van a utilizar las piezas en el proyecto?
