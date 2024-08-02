import os
import csv
from collections import defaultdict

def extract_dynamic_calls(trace_file_path):
    dynamic_calls = defaultdict(lambda: defaultdict(int))
    
    with open(trace_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    
    for line in lines:
        caller, callee = line.strip().split()  # Assumes a space-separated list of caller and callee in each trace entry
        dynamic_calls[caller][callee] += 1
    
    return dynamic_calls

def compute_dynamic_coupling(trace_file_path, output_csv):
    dynamic_calls = extract_dynamic_calls(trace_file_path)
    similarities = []
    
    for class1 in dynamic_calls:
        for class2 in dynamic_calls[class1]:
            similarity_score = dynamic_calls[class1][class2]
            similarities.append((class1, class2, similarity_score))
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['class1', 'class2', 'similarity_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in similarities:
            writer.writerow({'class1': row[0], 'class2': row[1], 'similarity_score': row[2]})

if __name__ == "__main__":
    compute_dynamic_coupling('data/argouml_trace.txt', 'dynamic_similarity_argouml.csv')
    compute_dynamic_coupling('data/jhotdraw_trace.txt', 'dynamic_similarity_jhotdraw.csv')
    compute_dynamic_coupling('data/jedit_trace.txt', 'dynamic_similarity_jedit.csv')
