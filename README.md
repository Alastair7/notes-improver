# NOTES-IMPROVER

Convierte documentos txt a markdown y luego se mejora el formato utilizando IA generativa.

## Cómo funciona?

Una carpeta `notes` contiene ficheros txt que se formatean utilizando un modelo de IA y se mejoran en formato `.md`.

Cuando se ejecuta `notes sync`, va a leer en la carpeta de in los documentos uno por uno, luego un LLM va a mejorar el contenido y se guardará en formato `.md` en la carpeta raíz del proyecto

## CLI

**Es necesario declarar la variable de entorno: `export NOTES_DIR=$HOME/notes/`**

Varios comandos donde cada uno tendrá sus subcomandos que permitirán hacer ciertas acciones como por ejemplo:

- [x] `notes sync`: Ejecuta el script para convertir los ficheros de `in/` a formato .md y mejorados por la IA.
- [x] `notes search-by-text 'Text to find in any note'` esto devolvería el listado de ficheros donde se encuentra el texto.
- [x] `notes search-by-keywords "keywords,to,search"`: Devuelve el contenido de los ficheros donde coincidan sus keywords.
- [] `notes get --path`: Devuelve el contenido del fichero indicado. 

## Sistema de ficheros

- **'~/notes/'**: Esta carpeta debe existir en el PATH con la variable de entorno `NOTES_DIR`. Contiene las notas en formato `.md` ya parseadas.

## Formato de los documentos MD

---
keywords: [esto,son,keywords]
---

# Título

Contenido


## TODO

- [] Usar notas como contexto para el LLM y poder hacer preguntas.
    - [x] Añadir función para obtener el contenido de todas las notas y pasarlo al contexto del modelo.
    - [] Añadir sistema de logging
    - [x] Añadir chat history
- [] Chat bot en vivo desde la terminal con un modelo.
- [] Usar modelo para generar contenido en las notas en base a prompts.


## Propuestas

- [] Usar notas como contexto para el LLM y poder hacer preguntas.
- [] Chat bot en vivo desde la terminal con un modelo.
- [] Usar modelo para generar contenido en las notas en base a prompts.
- [] Generar un index.md como resumen de cada nota: fecha de creación, título y un resumen en 2 lineas.
- [x] Búsqueda de notas por keyword: A partir de keywords, devolver las notas que los incluyan.
- Notas temporales: Poder marcar una nota como temporal y que se borre al cabo de x tiempo.
- [x] Shortcut para invocar el programa para acceder rápidamente a las notas.
- [] Encriptación de notas.
- [] Comando `notes info` para obtener información sobre las notas existentes (nº total de notas, fecha de creación de cada nota, fecha de actualización...)

## Pendientes a decidir

