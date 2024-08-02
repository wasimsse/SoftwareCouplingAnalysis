import os
import csv
from collections import defaultdict

def extract_dynamic_calls(trace_file_path, output_csv):
    if not os.path.exists(trace_file_path):
        print(f"Error: {trace_file_path} does not exist.")
        return

    dynamic_calls = defaultdict(lambda: defaultdict(int))
    
    print(f"Reading dynamic trace from {trace_file_path}")
    with open(trace_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    
    print("Processing dynamic trace entries...")
    for index, line in enumerate(lines):
        caller_callee = line.strip().split()
        if len(caller_callee) != 2:
            print(f"Skipping invalid line: {line.strip()}")
            continue
        
        caller, callee = caller_callee
        dynamic_calls[caller][callee] += 1
        
        if index % 100 == 0:  # Print status every 100 lines
            print(f"Processed {index} / {len(lines)} lines")
    
    print(f"Writing dynamic coupling data to {output_csv}")
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['caller', 'callee', 'call_count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for caller in dynamic_calls:
            for callee in dynamic_calls[caller]:
                writer.writerow({'caller': caller, 'callee': callee, 'call_count': dynamic_calls[caller][callee]})
    
    print(f"Finished processing {trace_file_path}")

if __name__ == "__main__":
    extract_dynamic_calls('data/argouml_trace.txt', 'dynamic_data_argouml.csv')
    extract_dynamic_calls('data/jhotdraw_trace.txt', 'dynamic_data_jhotdraw.csv')
    extract_dynamic_calls('data/jedit_trace.txt', 'dynamic_data_jedit.csv')
