import pandas as pd
import os

file_path = 'all_folders/a-team reader/default_power_1.csv'
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
read1= count_A / read_time_seconds
read2 = count_number / read_time_seconds
result = {
    'cycle time 1 (Tags starting with "A")': count_A,
    'cycle time 2 (Tags starting with a number)': count_number,'READ1(seconds)': read1,
'READ2(seconds)': read2}

print(result)
