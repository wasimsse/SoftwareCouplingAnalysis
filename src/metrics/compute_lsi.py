import os
import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

def read_csv(file_path):
    print(f"Reading data from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['file_path'], row['comments'], row['identifiers']) for row in reader]
    print(f"Loaded {len(data)} entries from {file_path}")
    return data

def compute_lsi_similarity(texts, n_components=100):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    lsi = TruncatedSVD(n_components=n_components)
    lsi_matrix = lsi.fit_transform(tfidf_matrix)
    
    similarity_matrix = cosine_similarity(lsi_matrix)
    return similarity_matrix

def process_system(system_name, input_csv, output_csv):
    data = read_csv(input_csv)
    texts = [' '.join([comments, identifiers]) for _, comments, identifiers in data]
    
    similarity_matrix = compute_lsi_similarity(texts)
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['class1_path', 'class2_path', 'similarity_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                class1_path = data[i][0]
                class2_path = data[j][0]
                similarity_score = similarity_matrix[i, j]
                writer.writerow({'class1_path': class1_path, 'class2_path': class2_path, 'similarity_score': similarity_score})

if __name__ == "__main__":
    process_system('ArgoUML', 'output_argouml.csv', 'lsi_similarity_argouml.csv')
    process_system('JHotDraw', 'output_jhotdraw.csv', 'lsi_similarity_jhotdraw.csv')
    process_system('jEdit', 'output_jedit.csv', 'lsi_similarity_jedit.csv')
