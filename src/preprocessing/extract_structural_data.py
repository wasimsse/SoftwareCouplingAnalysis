import os
import re
import csv

def extract_method_invocations(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        code = file.read()
    
    method_invocations = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code)
    return method_invocations

def process_directory(directory_path, output_csv):
    file_count = 0
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['class_name', 'method_invocations']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.java'):
                    file_count += 1
                    file_path = os.path.join(root, file)
                    class_name = os.path.basename(file_path).replace('.java', '')
                    method_invocations = extract_method_invocations(file_path)
                    writer.writerow({'class_name': class_name, 'method_invocations': ' '.join(method_invocations)})
                    
                    if file_count % 100 == 0:  # Print status every 100 files
                        print(f"Processed {file_count} files")
    
    print(f"Finished processing directory: {directory_path}")

if __name__ == "__main__":
    process_directory('data/argouml', 'structural_data_argouml.csv')
    process_directory('data/jhotdraw', 'structural_data_jhotdraw.csv')
    process_directory('data/jedit', 'structural_data_jedit.csv')
