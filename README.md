# Análisis Exploratorio de Reseñas de Goodreads

**Autor:** Sebastián Medina  
**Fecha:** Mayo 2025

---
## Indice

1. [Enlace al notebook](#enlace-al-notebook)
2. [Descripción](#descripción)
3. [Objetivo](#objetivo)
4. [Estructura del repositorio](#estructura-del-repositorio)
5. [Dataset](#dataset)
6. [Principales hallazgos](#principales-hallazgos)
8. [Créditos y licencia](#créditos-y-licencia)

---
## Enlace al notebook

Si desea observar el analisis en detalle, la metodologia aplicada y los resultados mas detallados, puede hacer clic en el siguiente enlace, que lo redireccionara hacia el notebook

- **Google Colab:**  
  [Abrir el notebook en Google Colab](https://colab.research.google.com/drive/1VcHHQg-V92mtW1XzeEe_owLVefp5wvtk?usp=sharing)

---
## Descripción 
Exploración y validación de hipótesis sobre reseñas de libros en Goodreads mediante análisis estadístico, visualizaciones y análisis de sentimiento.

---

## Objetivo
Explorar un dataset de ~380 000 reseñas y 40 000 libros muestreados de Goodreads para responder a seis hipótesis relacionadas con:
- Calificaciones (`rating`)  
- Longitud de reseñas (`review_len`)  
- Género literario (`genre`)  
- Extensión del libro (`num_pages`)  
- Análisis de sentimiento (VADER)  
- Popularidad (`text_reviews_count`)

---

## Estructura del repositorio

```plaintext
goodreads-eda/
├── notebooks/
│   └── goodreads_analysis.ipynb    # Notebook con todo el análisis
├── scripts/
│   ├── obtain_samples.py           # Script para muestrear los JSON originales
│   └── raws/                       # Archivos JSON originales antes de la muestra
└── README.md                       # Este archivo
```
---

## Dataset
- **Oirignal bruto:** ~1 459 609 libros y 14 726 881 reseñas en formato JSON (no incluidos).  
- **Muestra final:** `all_genres.csv`, 40 000 libros (5 000 por género) con todas sus reseñas.

---

## Principales hallazgos

- **Hipótesis 1: Género vs. Calificación**  
  No se detectaron diferencias notables de rating promedio entre géneros principales.

- **Hipótesis 2: Extensión vs. Rating**  
  Libros largos (>400 pág.) tienen rating medio ligeramente superior (3.82 vs. 3.75), pero el efecto es prácticamente nulo (Cohen’s d < 0.1).

- **Hipótesis 3: Rating vs. Longitud de reseña**  
  No hay relación clara entre longitud de reseña y ratings extremos; solo las reseñas de 0 estrellas son inusualmente cortas.

- **Hipótesis 4: Género vs. Longitud de reseña**  
  Reseñas de *Young Adult* y *Romance* son más largas (media ~740 caracteres) que las de *Poetry* (~466) o *Children* (~409).

- **Hipótesis 5: Sentimiento por género**  
  *Young Adult* y *Romance* presentan sentimiento medio más positivo (+0.56) que *Mystery/Thriller/Crime* (+0.43) e *History/Biography*.

- **Hipótesis 6: Género en libros populares**  
  Entre libros con >10 000 reseñas, *Mystery/Thriller/Crime* (35.2 %) y *Fantasy/Paranormal* (29.9 %) dominan en número.  
  *Children* destaca con mejor rating medio (4.10) y *History/Biography* con el más bajo (3.61).


---
## Créditos y licencia

- **Autor:** Sebastián Medina  
- **Licencia:** MIT  
- **Colaboración:** Si te interesa contribuir al proyecto o tienes sugerencias, no dudes en abrir un issue o un pull request en este repositorio.  
- **Citación:** Si utilizas este trabajo en tu investigación o proyectos, por favor da el crédito correspondiente.
