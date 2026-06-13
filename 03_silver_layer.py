import pandas as pd
import os

# Read Bronze Patient Data
patients = pd.read_csv(
    "data/bronze/patients/patients.csv"
)

print("Original Rows:", len(patients))

# Remove duplicates
patients = patients.drop_duplicates()

# Standardize column names
patients.columns = [
    col.lower()
       .replace(" ", "_")
    for col in patients.columns
]

# Missing value report
missing_report = patients.isnull().sum()

print("\nMissing Values:")
print(missing_report)

# Create Silver folder
os.makedirs(
    "data/silver/patients",
    exist_ok=True
)

# Save cleaned data
patients.to_csv(
    "data/silver/patients/patients.csv",
    index=False
)

print("\nSilver Patients Table Created Successfully")