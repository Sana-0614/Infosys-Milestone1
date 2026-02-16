import pandas as pd
import numpy as np

def clean_data(file_path):
    data = pd.read_csv(file_path)

    # Convert ID and ProdID to numeric
    data['ID'] = pd.to_numeric(data['ID'], errors='coerce')
    data['ProdID'] = pd.to_numeric(data['ProdID'], errors='coerce')

    # Drop rows where ID or ProdID is NaNs
    data.dropna(subset=['ID', 'ProdID'], inplace=True)

    # Remove rows where ID or ProdID is 0
    data = data[(data['ID'] != 0) & (data['ProdID'] != 0)]

    # Drop unwanted column if exists
    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)

    # Fill text columns with empty string
    text_columns = ['Category', 'Brand', 'Name', 'ImageURL', 'Description', 'Tags']
    for col in text_columns:
        if col in data.columns:
            data[col] = data[col].fillna('')

    # Remove "|" from ImageURL
    if 'ImageURL' in data.columns:
        data['ImageURL'] = data['ImageURL'].str.replace('|', '', regex=False)

    # Reset index
    data.reset_index(drop=True, inplace=True)

    return data
