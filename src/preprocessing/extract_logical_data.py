import os
import csv
from collections import defaultdict

def extract_co_changes(log_file_path, output_csv):
    co_changes = defaultdict(lambda: defaultdict(int))
    
    print(f"Reading commit log from {log_file_path}")
    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    
    print("Processing commit log entries...")
    for index, line in enumerate(lines):
        files_changed = line.strip().split()  # Assumes a space-separated list of changed files in each commit log entry
        for i in range(len(files_changed)):
            for j in range(i + 1, len(files_changed)):
                file1 = os.path.basename(files_changed[i])
                file2 = os.path.basename(files_changed[j])
                co_changes[file1][file2] += 1
                co_changes[file2][file1] += 1
        
        if index % 100 == 0:  # Print status every 100 lines
            print(f"Processed {index} / {len(lines)} lines")
    
    print(f"Writing logical coupling data to {output_csv}")
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['file1', 'file2', 'co_changes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for file1 in co_changes:
            for file2 in co_changes[file1]:
                writer.writerow({'file1': file1, 'file2': file2, 'co_changes': co_changes[file1][file2]})
    
    print(f"Finished processing {log_file_path}")

if __name__ == "__main__":
    extract_co_changes('data/argouml_commit_log.txt', 'logical_data_argouml.csv')
    extract_co_changes('data/jhotdraw_commit_log.txt', 'logical_data_jhotdraw.csv')
    extract_co_changes('data/jedit_commit_log.txt', 'logical_data_jedit.csv')
