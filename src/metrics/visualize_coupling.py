import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_coupling(input_file, title):
    df = pd.read_csv(input_file, index_col=0)
    plt.figure(figsize=(10, 8))
    sns.heatmap(df, cmap='viridis')
    plt.title(title)
    plt.show()

def main():
    print("Select the system to visualize coupling data:")
    print("1. ArgoUML")
    print("2. JHotDraw")
    print("3. jEdit")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        semantic_file = 'data/argouml_lsi_similarity.csv'
        structural_file = 'data/argouml_structural_coupling.csv'
        logical_file = 'data/argouml_logical_coupling.csv'
    elif choice == '2':
        semantic_file = 'data/jhotdraw_lsi_similarity.csv'
        structural_file = 'data/jhotdraw_structural_coupling.csv'
        logical_file = 'data/jhotdraw_logical_coupling.csv'
    elif choice == '3':
        semantic_file = 'data/jedit_lsi_similarity.csv'
        structural_file = 'data/jedit_structural_coupling.csv'
        logical_file = 'data/jedit_logical_coupling.csv'
    else:
        print("Invalid choice. Please run the script again and select a valid option.")
        return

    print("Select the type of coupling to visualize:")
    print("1. Semantic Coupling")
    print("2. Structural Coupling")
    print("3. Logical Coupling")
    coupling_choice = input("Enter the number corresponding to your choice: ")

    if coupling_choice == '1':
        visualize_coupling(semantic_file, "Semantic Coupling Heatmap")
    elif coupling_choice == '2':
        visualize_coupling(structural_file, "Structural Coupling Heatmap")
    elif coupling_choice == '3':
        visualize_coupling(logical_file, "Logical Coupling Heatmap")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
