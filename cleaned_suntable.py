import pandas as pd

# Read the CSV file
df = pd.read_csv('suntable_output_data2022.csv')

# Remove string/symbols from "Sunrise" and "Sunset" columns
df['Sunrise'] = df['Sunrise'].str.extract('(\d+:\d+)', expand=False)
df['Sunset'] = df['Sunset'].str.extract('(\d+:\d+)', expand=False)

# Drop rows with missing values
df.dropna(inplace=True)

# Print the modified DataFrame
print(df)

# Save the modified DataFrame to a new CSV file
df.to_csv('cleaned_table_2022.csv', index=False)
