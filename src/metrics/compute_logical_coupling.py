import pandas as pd

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

def compute_logical_coupling(input_file, output_file):
    df = pd.read_csv(input_file)
    
    coupling_matrix = pd.crosstab(df['File1'], df['File2'])
    coupling_matrix = coupling_matrix + coupling_matrix.T
    coupling_matrix.to_csv(output_file)
    print(f"Logical coupling computation completed. Output written to {output_file}")

def main():
    print("Select the system to process for logical coupling:")
    print("1. ArgoUML")
    print("2. JHotDraw")
    print("3. jEdit")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        input_file = 'data/argouml_logical.csv'
        output_file = 'data/argouml_logical_coupling.csv'
    elif choice == '2':
        input_file = 'data/jhotdraw_logical.csv'
        output_file = 'data/jhotdraw_logical_coupling.csv'
    elif choice == '3':
        input_file = 'data/jedit_logical.csv'
        output_file = 'data/jedit_logical_coupling.csv'
    else:
        print("Invalid choice. Please run the script again and select a valid option.")
        return

    compute_logical_coupling(input_file, output_file)

if __name__ == "__main__":
    main()
