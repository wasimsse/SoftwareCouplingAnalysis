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

def process_directory(directory_path, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['file_path', 'comments', 'identifiers']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        print(f"Processing directory: {directory_path}")
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

def main():
    print("Select the system to process:")
    print("1. ArgoUML")
    print("2. JHotDraw")
    print("3. jEdit")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        process_directory('data/argouml', 'output_argouml.csv')
    elif choice == '2':
        process_directory('data/jhotdraw', 'output_jhotdraw.csv')
    elif choice == '3':
        process_directory('data/jedit', 'output_jedit.csv')
    else:
        print("Invalid choice. Please run the script again and select a valid option.")

if __name__ == "__main__":
    main()
