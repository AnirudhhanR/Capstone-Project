import pandas as pd

# Replace 'your_file.csv' with the actual file path
file_path = 'C:/Users/Deepa V/Downloads/output.csv'

# Read CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Assuming your data is separated by commas, you can use the 'str.split' method
df['Column_Name'] = df['Your_Column'].str.split(',')

# If you want to split into separate columns, you can use the 'expand' parameter
df[['Column1', 'Column2', 'Column3']] = df['Your_Column'].str.split(',', expand=True)

# Save the DataFrame to a new CSV file
df.to_csv('new_file.csv', index=False)