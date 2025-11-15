# NOTES-IMPROVER

Convierte documentos txt a markdown y luego se mejora el formato utilizando IA generativa.

## Cómo funciona?

Una carpeta de in donde contendrá ficheros txt y en la carpeta raíz estarán los documentos formateados y mejorados en md.

Cuando se ejecuta `notes sync`, va a leer en la carpeta de in los documentos uno por uno, luego un LLM va a mejorar el contenido y se guardará en formato `.md` en la carpeta raíz del proyecto

## CLI

**Es necesario declarar la variable de entorno: `export NOTES_DIR=$HOME/notes/`**

Varios comandos donde cada uno tendrá sus subcomandos que permitirán hacer ciertas acciones como por ejemplo:

- [] `notes sync`: Ejecuta el script para convertir los ficheros de `in/` a formato .md y mejorados por la IA.
- [x] `notes search-by-text 'Text to find in any note'` esto devolvería el listado de ficheros donde se encuentra el texto.
- [x] `notes search-by-keywords "keywords,to,search"`: Devuelve el contenido de los ficheros donde coincidan sus keywords.
- [] `notes get --path`: Devuelve el contenido del fichero indicado. 

## Sistema de ficheros

- **'~/notes/'**: Esta carpeta debe existir en el PATH con la variable de entorno `NOTES_DIR`. Contiene las notas en formato `.md` ya parseadas.
- **'~/notes/in/'**: Contiene las notas en formato .txt pendientes de ser parseadas.

## TODO

- [] Implementar comando `notes sync` para convertir ficheros .txt a MD usando el LLM de Gemini.
- [] 
- [x] Reconfigurar el sistema de ficheros para que solo haya in, y los MD estén en la carpeta raíz: notes/
- [x] Corregir test para que revise dentro de las carpetas si existen textos.
- [x] Leer capítulo 7 de Fluent Python


## Propuestas

- [] Generar un index.md como resumen de cada nota: fecha de creación, título y un resumen en 2 lineas.
- [x] Búsqueda de notas por keyword: A partir de keywords, devolver las notas que los incluyan.
- Notas temporales: Poder marcar una nota como temporal y que se borre al cabo de x tiempo.
- [x] Shortcut para invocar el programa para acceder rápidamente a las notas.
- [] Encriptación de notas.
- [] Comando `notes info` para obtener información sobre las notas existentes (nº total de notas, fecha de creación de cada nota, fecha de actualización...)

## Pendientes a decidir

- [] Crear un comando para parsear documentos .txt a markdown o utilizar la carpeta `in`?
- [] El comando `notes get` es necesario existiendo el comando de Linux `cat`?
