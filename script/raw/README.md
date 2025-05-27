# Archivos crudos (raw)

Este directorio está destinado a contener los datos crudos utilizados para generar las muestras del dataset. Sin embargo, debido al tamaño considerable de los archivos originales, no están incluidos en este repositorio. A continuación, se proporcionan las instrucciones para obtenerlos manualmente.

## Cómo obtener los archivos crudos

1. **Visita el sitio oficial del dataset de Goodreads:**
   - [Goodreads Dataset](https://cseweb.ucsd.edu/~jmcauley/datasets/goodreads.html)

2. **Descarga los archivos de libros y reseñas por género:**
   - Ve a la última sección del sitio denominada **"By Genre"**.
   - Descarga los archivos que correspondan a cada género:
     - `goodreads_books_{genre}.json.gz` (Libros)
     - `goodreads_reviews_{genre}.json.gz` (Reseñas)
   - **Nota importante:** No descargues los archivos `goodreads_interactions_{genre}.json.gz`, ya que estos no se utilizan en este análisis.

3. **Cantidad esperada de archivos:**
   - Una vez descargados, deberías tener un total de **16 archivos**: 2 por cada género (uno de libros y otro de reseñas).

4. **Organiza los archivos:**
   - Coloca los 16 archivos descargados en esta carpeta (`raw/`), ya que el script de muestreo los utilizará desde aquí para generar las muestras.

## Próximos pasos

Con los archivos crudos listos, puedes proceder a ejecutar el script `obtain_samples.py` para generar las muestras necesarias. Este script está diseñado para tomar los datos originales y crear un dataset reducido y manejable para el análisis.

Si tienes dudas o necesitas ayuda adicional, no dudes en consultar el [README principal del repositorio](../README.md).
