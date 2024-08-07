import pandas as pd
import os
def process_csv(file_path):
    data = pd.read_csv(file_path, skiprows=5)
    data.columns = ['TAG ID', 'COUNT', 'RSSI']
    data['COUNT'] = pd.to_numeric(data['COUNT'], errors='coerce')
    data['RSSI'] = pd.to_numeric(data['RSSI'], errors='coerce')

    data.dropna(inplace=True)

    with open(file_path, 'r') as file:
        lines = file.readlines()
    read_time_str = lines[3].split(',')[1].strip()
    minutes, seconds = map(int, read_time_str.split(':'))
    read_time_seconds = minutes * 60 + seconds
    tags_starting_with_A = data[data['TAG ID'].str.startswith('A')]
    tags_starting_with_number = data[data['TAG ID'].str.match('^\d')]

    count_A = tags_starting_with_A['COUNT'].sum()
    count_number = tags_starting_with_number['COUNT'].sum()
    read1 = count_A / read_time_seconds
    read2 = count_number / read_time_seconds

    result = {
        'folder': os.path.dirname(file_path),
        'file': os.path.basename(file_path),
        'cycle time 1 (Tags starting with "A")': count_A,
        'cycle time 2 (Tags starting with a number)': count_number,
        'READ1 (seconds)': read1,
        'READ2 (seconds)': read2
    }

    return result
def main(folder_path, output_file):
    results = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                result = process_csv(file_path)
                results.append(result)
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
folder_path = 'all_folders/mac'
output_file = 'processed_results1.csv'
main(folder_path, output_file)
