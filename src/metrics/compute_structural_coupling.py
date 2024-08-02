import pandas as pd

def compute_structural_coupling(input_file, output_file):
    df = pd.read_csv(input_file)
    df['dependencies'] = df['dependencies'].fillna('')
    
    coupling_dict = {}
    for index, row in df.iterrows():
        file_path = row['file_path']
        dependencies = row['dependencies'].split(', ')
        for dep in dependencies:
            if dep not in coupling_dict:
                coupling_dict[dep] = []
            coupling_dict[dep].append(file_path)
    
    # Compute coupling matrix
    coupling_matrix = pd.DataFrame(0, index=df['file_path'], columns=df['file_path'])
    for dep, files in coupling_dict.items():
        for i in range(len(files)):
            for j in range(i + 1, len(files)):
                coupling_matrix.at[files[i], files[j]] += 1
                coupling_matrix.at[files[j], files[i]] += 1
    
    coupling_matrix.to_csv(output_file)
    print(f"Structural coupling computation completed. Output written to {output_file}")

def main():
    print("Select the system to process for structural coupling:")
    print("1. ArgoUML")
    print("2. JHotDraw")
    print("3. jEdit")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        input_file = 'data/argouml_structural.csv'
        output_file = 'data/argouml_structural_coupling.csv'
    elif choice == '2':
        input_file = 'data/jhotdraw_structural.csv'
        output_file = 'data/jhotdraw_structural_coupling.csv'
    elif choice == '3':
        input_file = 'data/jedit_structural.csv'
        output_file = 'data/jedit_structural_coupling.csv'
    else:
        print("Invalid choice. Please run the script again and select a valid option.")
        return

    compute_structural_coupling(input_file, output_file)

if __name__ == "__main__":
    main()
