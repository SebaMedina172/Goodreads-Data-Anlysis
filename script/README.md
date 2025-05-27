# Scripts

Este directorio contiene el script necesario para generar un dataset reducido a partir de los datos crudos del dataset de Goodreads.

## Contenido

- `obtain_samples.py`: Este script procesa los archivos crudos y genera un archivo CSV con una muestra de libros y reseñas, listo para su análisis.

## Cómo usar el script

1. **Prepara los archivos crudos:**
   - Asegúrate de haber descargado y colocado los archivos crudos en la carpeta `raw/` siguiendo las instrucciones del [README de la carpeta raw](./raw/README.md).

2. **Requisitos previos:**
   - Asegúrate de tener Python instalado.
   - No es necesario instalar librerías adicionales, ya que el script utiliza únicamente módulos integrados en Python.

3. **Ejecuta el script:**
   - Abre una terminal o línea de comandos.
   - Navega a este directorio (`scripts/`).
   - Ejecuta el script con el siguiente comando:
     ```bash
     python obtain_samples.py
     ```

4. **Resultado:**
   - El script generará una carpeta `samples`.
   - Dentro de la carpeta `samples`, se generaran un total de 25 archivos `.csv`, donde el que tiene todo unificado y utilizamos para dicho analisis es `all_genres_sample`.
   - Los demas archivos pueden utilizarse para realizar analisis mas especifico dentro de cada genero, pero en este caso, no los utilizamos.
  
## Notas adicionales

- Puedes modificar el script para ajustar el tamaño de las muestras o filtrar datos según tus necesidades específicas.
- Para más detalles sobre el dataset generado y los pasos del análisis, consulta el [README principal del repositorio](../README.md).
