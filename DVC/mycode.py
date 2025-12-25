# Practicing the Data Versioning with DVC tool
import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Ali'],
    'Age': [25, 30, 35, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Pakistan']
}

# The data directory is created in the root of the project
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(root_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

csv_path = os.path.join(data_dir, 'people.csv')

# Check if CSV file exists
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(data)

#Adding a new row to the DataFrame
new_row = {'Name': 'Fatima', 'Age': 21, 'City': 'Lahore'}
df.loc[len(df.index)] = new_row

new_row2 = {'Name': 'Zain', 'Age': 23, 'City': 'Karachi'}
df.loc[len(df.index)] = new_row2

new_row3 = {'Name': 'Hassan', 'Age': 29, 'City': 'Islamabad'}
df.loc[len(df.index)] = new_row3

df.to_csv(csv_path, index=False)

print("Data saved to data/people.csv")