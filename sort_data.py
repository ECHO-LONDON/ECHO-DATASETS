import pandas as pd

# Assuming 'search' is the first column and 'relevance' is the third
# Load the JSON file into a DataFrame
df = pd.read_json("mastodon_data.json")

# Replace values in the 'search' column
replacement_dict = {
    0: "politics",
    1: "solana news",
    2: "machine learning research",
    3: "computer vision",
    4: "global warming",
    5: "international space station"
}
df['search'] = df['search'].replace(replacement_dict)

# Remove the third column, assumed to be 'relevance'
df.drop(columns=['relevance'], inplace=True)

# Export the modified DataFrame to a CSV file
df.to_csv("Modified2_Training_data.csv", index=False)
