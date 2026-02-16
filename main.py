from preprocess_data import clean_data

# Load cleaned data
data = clean_data("cleaned_data.csv")

print("Data Loaded and Cleaned Successfully!")
print(data.head())
print("\nMissing Values:")
print(data.isnull().sum())






