import pandas as pd
import os

tables = [
    "patients",
    "encounters",
    "claims",
    "conditions",
    "observations",
    "providers",
    "organizations",
    "procedures",
    "medications"
]

print("=" * 60)
print("SILVER LAYER PROCESSING STARTED")
print("=" * 60)

for table in tables:

    try:
        print(f"\nProcessing {table}")

        bronze_file = f"data/bronze/{table}/{table}.csv"

        df = pd.read_csv(bronze_file)

        original_rows = len(df)

        # Remove duplicates
        df = df.drop_duplicates()

        # Standardize column names
        df.columns = [
            col.lower()
               .replace(" ", "_")
               .replace("-", "_")
            for col in df.columns
        ]

        # Create silver folder
        silver_folder = f"data/silver/{table}"

        os.makedirs(
            silver_folder,
            exist_ok=True
        )

        silver_file = f"{silver_folder}/{table}.csv"

        df.to_csv(
            silver_file,
            index=False
        )

        print(f"Original Rows: {original_rows}")
        print(f"Rows After Cleaning: {len(df)}")
        print(f"Silver table created: {silver_file}")

    except Exception as e:
        print(f"Error processing {table}: {e}")

print("\n" + "=" * 60)
print("SILVER LAYER COMPLETED")
print("=" * 60)