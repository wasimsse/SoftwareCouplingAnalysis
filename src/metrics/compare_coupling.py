import pandas as pd
import matplotlib.pyplot as plt

def load_similarity_data(lsi_file, transformer_file):
    lsi_df = pd.read_csv(lsi_file)
    transformer_df = pd.read_csv(transformer_file)
    return lsi_df, transformer_df

def compare_similarity(lsi_df, transformer_df, output_file):
    merged_df = pd.merge(lsi_df, transformer_df, on=['class1_path', 'class2_path'], suffixes=('_lsi', '_transformer'))
    
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['similarity_score_lsi'], merged_df['similarity_score_transformer'], alpha=0.5)
    plt.xlabel('LSI Similarity Score')
    plt.ylabel('Transformer Similarity Score')
    plt.title('Comparison of LSI and Transformer-based Semantic Coupling')
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    lsi_df_argouml, transformer_df_argouml = load_similarity_data('lsi_similarity_argouml.csv', 'semantic_similarity_argouml_subset.csv')
    compare_similarity(lsi_df_argouml, transformer_df_argouml, 'comparison_argouml.png')

    lsi_df_jhotdraw, transformer_df_jhotdraw = load_similarity_data('lsi_similarity_jhotdraw.csv', 'semantic_similarity_jhotdraw_subset.csv')
    compare_similarity(lsi_df_jhotdraw, transformer_df_jhotdraw, 'comparison_jhotdraw.png')

    lsi_df_jedit, transformer_df_jedit = load_similarity_data('lsi_similarity_jedit.csv', 'semantic_similarity_jedit_subset.csv')
    compare_similarity(lsi_df_jedit, transformer_df_jedit, 'comparison_jedit.png')
