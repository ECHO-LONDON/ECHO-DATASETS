import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv('Modified2_Training_data.csv')  

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text(separator=' ', strip=True)

df.iloc[:, 1] = df.iloc[:, 1].apply(extract_text)


df.to_csv('extracted_and_modified_text.csv', index=False)
