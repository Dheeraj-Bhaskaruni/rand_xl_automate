import pandas as pd

file_path = '/mnt/data/power150_5.csv'
data = pd.read_csv(file_path, skiprows=5)
data.columns = ['TAG ID', 'COUNT', 'RSSI']
data['COUNT'] = pd.to_numeric(data['COUNT'], errors='coerce')
data['RSSI'] = pd.to_numeric(data['RSSI'], errors='coerce')
data.dropna(inplace=True)
read_time_str = pd.read_csv(file_path, nrows=3).iloc[2, 1]

minutes, seconds = map(int, read_time_str.split(':'))
read_time_seconds = minutes * 60 + seconds

tags_starting_with_A = data[data['TAG ID'].str.startswith('A')]
tags_starting_with_number = data[data['TAG ID'].str.match('^\d')]
count_A = tags_starting_with_A['COUNT'].sum()
count_number = tags_starting_with_number['COUNT'].sum()

result = {
    'cycle time 1 (Tags starting with "A")': count_A,
    'cycle time 2 (Tags starting with a number)': count_number,
    'READ TIME (seconds)': read_time_seconds
}

print(result)
