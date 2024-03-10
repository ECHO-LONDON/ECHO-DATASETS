import pandas as pd

# Load the CSV files
df1 = pd.read_csv('Modified_and_extracted_data_2.csv')  
df2 = pd.read_csv('Modified_Training_data.csv')

if len(df1) == len(df2):
    df1.iloc[:, 1] = df2['content']
else:
    print("The DataFrames do not match in length.")

# Now df1 has the original first column and the updated second column from df2
# Save the combined DataFrame to a new CSV file
df1.to_csv('combined_data.csv', index=False)
