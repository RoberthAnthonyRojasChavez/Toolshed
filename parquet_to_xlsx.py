import pandas as pd
file_dir = r'D:\ab5a3a47c41d5189060b646f2f7671c8\processing-run\d3b8dedd-69a1-44b7-a530-b4b840a7a6db\\'
file_ID = 'timscore.candidates'

# Specify the path to your .parquet file
parquet_file = file_dir+file_ID+'.parquet'

# Read the .parquet file into a pandas DataFrame
df = pd.read_parquet(parquet_file)

# Specify the path where you want to save the .xlsx file
excel_file = file_dir+file_ID+'.xlsx'

# Write the DataFrame to an Excel file (.xlsx)
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f'Conversion complete. Excel file saved at: {excel_file}')
