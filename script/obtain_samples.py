import gzip
import json
import random
import pandas as pd
import os

# 1) Configuración
genres = {
    'children':                {'books': '../raw/goodreads_books_children.json.gz',
                                'reviews': '../raw/goodreads_reviews_children.json.gz'},
    'comics_graphic':          {'books': '../raw/goodreads_books_comics_graphic.json.gz',
                                'reviews': '../raw/goodreads_reviews_comics_graphic.json.gz'},
    'fantasy_paranormal':      {'books': '../raw/goodreads_books_fantasy_paranormal.json.gz',
                                'reviews': '../raw/goodreads_reviews_fantasy_paranormal.json.gz'},
    'history_biography':       {'books': '../raw/goodreads_books_history_biography.json.gz',
                                'reviews': '../raw/goodreads_reviews_history_biography.json.gz'},
    'mystery_thriller_crime':  {'books': '../raw/goodreads_books_mystery_thriller_crime.json.gz',
                                'reviews': '../raw/goodreads_reviews_mystery_thriller_crime.json.gz'},
    'poetry':                  {'books': '../raw/goodreads_books_poetry.json.gz',
                                'reviews': '../raw/goodreads_reviews_poetry.json.gz'},
    'romance':                 {'books': '../raw/goodreads_books_romance.json.gz',
                                'reviews': '../raw/goodreads_reviews_romance.json.gz'},
    'young_adult':             {'books': '../raw/goodreads_books_young_adult.json.gz',
                                'reviews': '../raw/goodreads_reviews_young_adult.json.gz'},
}

# Numero de libros para samplear
n_books = 5000  

output_dir = 'samples'
os.makedirs(output_dir, exist_ok=True)

for genre, paths in genres.items():
    print(f"\n=== Procesando género: {genre} ===")
    # 2) Extraer y muestrear book_id
    book_ids = []
    with gzip.open(paths['books'], 'rt', encoding='utf-8') as f_books:
        for line in f_books:
            book = json.loads(line)
            book_ids.append(book['book_id'])
    sample_ids = set(random.sample(book_ids, min(n_books, len(book_ids))))
    del book_ids  # liberar memoria
    
    # 3) Filtrar y guardar libros muestreados
    books_sample = []
    with gzip.open(paths['books'], 'rt', encoding='utf-8') as f_books:
        for line in f_books:
            book = json.loads(line)
            if book['book_id'] in sample_ids:
                books_sample.append(book)
    df_b = pd.DataFrame(books_sample)
    books_csv = os.path.join(output_dir, f'books_sample_{genre}.csv')
    df_b.to_csv(books_csv, index=False)
    print(f" Guardados {len(df_b)} libros en {books_csv}")
    
    # 4) Filtrar y guardar reseñas correspondientes
    reviews_sample = []
    with gzip.open(paths['reviews'], 'rt', encoding='utf-8') as f_reviews:
        for line in f_reviews:
            review = json.loads(line)
            if review['book_id'] in sample_ids:
                reviews_sample.append(review)
    df_r = pd.DataFrame(reviews_sample)
    reviews_csv = os.path.join(output_dir, f'reviews_sample_{genre}.csv')
    df_r.to_csv(reviews_csv, index=False)
    print(f" Guardadas {len(df_r)} reseñas en {reviews_csv}")
    
    # 5) Merge y guardado final por género
    df_merged = pd.merge(df_r, df_b, how='inner', on='book_id')
    df_merged['genre'] = genre
    merged_csv = os.path.join(output_dir, f'merged_{genre}.csv')
    df_merged.to_csv(merged_csv, index=False)
    print(f" Merge: {len(df_merged)} filas en {merged_csv}")

# 6)Concatenar todos los géneros en un solo CSV
all_merged = []
for f in os.listdir(output_dir):
    if f.startswith('merged_') and f.endswith('.csv'):
        all_merged.append(pd.read_csv(os.path.join(output_dir, f)))
df_all = pd.concat(all_merged, ignore_index=True)
all_csv = os.path.join(output_dir, 'all_genres.csv')
df_all.to_csv(all_csv, index=False)
print(f"\nDataset final combinado: {len(df_all)} filas en {all_csv}")
