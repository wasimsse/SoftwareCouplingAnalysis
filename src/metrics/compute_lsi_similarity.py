import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

def compute_lsi_similarity(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Combine comments and identifiers into a single text field
    df['text'] = df['comments'] + ' ' + df['identifiers']
    
    # Handle NaN values and check for empty documents
    df['text'] = df['text'].fillna('').str.strip()
    df = df[df['text'].apply(lambda x: len(x) > 0)]
    
    if df.empty:
        print("No valid documents found after preprocessing.")
        return

    # Vectorize the text using TF-IDF
    vectorizer = TfidfVectorizer()
    try:
        X = vectorizer.fit_transform(df['text'])
    except ValueError as e:
        print(f"Error during vectorization: {e}")
        return
    
    # Apply LSI (Latent Semantic Indexing)
    lsi = TruncatedSVD(n_components=100, random_state=42)
    X_lsi = lsi.fit_transform(X)
    
    # Compute cosine similarity
    similarity_matrix = cosine_similarity(X_lsi)
    
    # Convert the similarity matrix to a DataFrame
    similarity_df = pd.DataFrame(similarity_matrix, index=df['file_path'], columns=df['file_path'])
    
    # Save the similarity DataFrame to a CSV file
    similarity_df.to_csv(output_file)
    print(f"LSI similarity computation completed. Output written to {output_file}")

def main():
    print("Select the system to process for LSI similarity:")
    print("1. ArgoUML")
    print("2. JHotDraw")
    print("3. jEdit")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        input_file = 'data/argouml_semantic.csv'
        output_file = 'data/argouml_lsi_similarity.csv'
    elif choice == '2':
        input_file = 'data/jhotdraw_semantic.csv'
        output_file = 'data/jhotdraw_lsi_similarity.csv'
    elif choice == '3':
        input_file = 'data/jedit_semantic.csv'
        output_file = 'data/jedit_lsi_similarity.csv'
    else:
        print("Invalid choice. Please run the script again and select a valid option.")
        return

    compute_lsi_similarity(input_file, output_file)

if __name__ == "__main__":
    main()
