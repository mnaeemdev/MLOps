# Practicing the Data Versioning with DVC tool
import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Ali'],
    'Age': [25, 30, 35, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Pakistan']
}

df = pd.DataFrame(data)

import os

# The data directory is created inside the DVC folder
dvc_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(dvc_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

df.to_csv(os.path.join(data_dir, 'people.csv'), index=False)

print("Data saved to data/people.csv")
