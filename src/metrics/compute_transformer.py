import csv
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Load the pre-trained model
model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

def read_csv(file_path):
    print(f"Reading data from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['file_path'], row['comments'], row['identifiers']) for row in reader]
    print(f"Loaded {len(data)} entries from {file_path}")
    return data

def compute_similarity(text1, text2):
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
    return cosine_scores.item()

def process_system(system_name, input_csv, output_csv):
    data = read_csv(input_csv)
    num_classes = len(data)
    similarities = []

    print(f"Computing similarities for {system_name}...")

    for i in range(num_classes):
        for j in range(i + 1, num_classes):
            class1_path, comments1, identifiers1 = data[i]
            class2_path, comments2, identifiers2 = data[j]
            combined_text1 = comments1 + ' ' + identifiers1
            combined_text2 = comments2 + ' ' + identifiers2
            similarity_score = compute_similarity(combined_text1, combined_text2)
            similarities.append((class1_path, class2_path, similarity_score))

            if (i * num_classes + j) % 500 == 0:  # Print status every 500 comparisons
                print(f"Processed {i * num_classes + j} / {num_classes * (num_classes - 1) // 2} comparisons")

    print(f"Writing results to {output_csv}")

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['class1_path', 'class2_path', 'similarity_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in similarities:
            writer.writerow({'class1_path': row[0], 'class2_path': row[1], 'similarity_score': row[2]})

    print(f"Finished processing {system_name}")

if __name__ == "__main__":
    process_system('ArgoUML', 'output_argouml.csv', 'semantic_similarity_argouml.csv')
    process_system('JHotDraw', 'output_jhotdraw.csv', 'semantic_similarity_jhotdraw.csv')
    process_system('jEdit', 'output_jedit.csv', 'semantic_similarity_jedit.csv')
