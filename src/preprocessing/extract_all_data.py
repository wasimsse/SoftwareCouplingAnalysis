import os
import re
import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def extract_comments_and_identifiers(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            code = file.read()
    except UnicodeDecodeError as e:
        print(f"Error decoding {file_path}: {e}")
        return [], []

    comments = re.findall(r'//.*|/\*.*?\*/', code, re.DOTALL)
    identifiers = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)

    return comments, identifiers

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalnum() and word.lower() not in stop_words]

    return ' '.join(words)

def extract_structural_dependencies(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            code = file.read()
    except UnicodeDecodeError as e:
        print(f"Error decoding {file_path}: {e}")
        return []

    dependencies = re.findall(r'import\s+([\w\.]+);', code)
    return dependencies

def extract_co_changes(log_file_path, csv_path):
    co_changes = []
    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        commits = file.read().split('commit ')[1:]
    
    for commit in commits:
        files = re.findall(r'\s+(\S+)\s+\|\s+\d+', commit)
        if len(files) > 1:
            for i in range(len(files)):
                for j in range(i + 1, len(files)):
                    co_changes.append((files[i], files[j]))
    
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File1', 'File2'])
        writer.writerows(co_changes)

def process_directory_semantic(directory_path, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['file_path', 'comments', 'identifiers']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        print(f"Processing directory for semantic data: {directory_path}")
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.java'):
                    file_path = os.path.join(root, file)
                    print(f"Processing file: {file_path}")
                    comments, identifiers = extract_comments_and_identifiers(file_path)
                    
                    comments_text = preprocess_text(' '.join(comments))
                    identifiers_text = preprocess_text(' '.join(identifiers))
                    
                    writer.writerow({
                        'file_path': file_path,
                        'comments': comments_text,
                        'identifiers': identifiers_text
                    })
    print(f"Finished processing semantic data for {directory_path}. Output written to {output_file}")

def process_directory_structural(directory_path, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['file_path', 'dependencies']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        print(f"Processing directory for structural data: {directory_path}")
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.java'):
                    file_path = os.path.join(root, file)
                    print(f"Processing file: {file_path}")
                    dependencies = extract_structural_dependencies(file_path)
                    
                    writer.writerow({
                        'file_path': file_path,
                        'dependencies': ', '.join(dependencies)
                    })
    print(f"Finished processing structural data for {directory_path}. Output written to {output_file}")

def main():
    while True:
        print("Select the type of data to extract:")
        print("1. Semantic Coupling")
        print("2. Structural Coupling")
        print("3. Logical Coupling")
        data_choice = input("Enter the number corresponding to your choice: ")

        print("Select the system to process:")
        print("1. ArgoUML")
        print("2. JHotDraw")
        print("3. jEdit")
        system_choice = input("Enter the number corresponding to your choice: ")

        if system_choice == '1':
            system = 'argouml'
            commit_log = 'data/argouml_commit_log.txt'
        elif system_choice == '2':
            system = 'jhotdraw'
            commit_log = 'data/jhotdraw_commit_log.txt'
        elif system_choice == '3':
            system = 'jedit'
            commit_log = 'data/jedit_commit_log.txt'
        else:
            print("Invalid system choice. Please select a valid option.")
            continue

        if data_choice == '1':
            output_file = f'data/{system}_semantic.csv'
            process_directory_semantic(f'data/{system}', output_file)
        elif data_choice == '2':
            output_file = f'data/{system}_structural.csv'
            process_directory_structural(f'data/{system}', output_file)
        elif data_choice == '3':
            output_file = f'data/{system}_logical.csv'
            extract_co_changes(commit_log, output_file)
            print(f"Finished processing logical data for {system}. Output written to {output_file}")
        else:
            print("Invalid data choice. Please select a valid option.")
            continue

        another = input("Do you want to process another system or data type? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Terminating the process.")
            break

if __name__ == "__main__":
    main()
