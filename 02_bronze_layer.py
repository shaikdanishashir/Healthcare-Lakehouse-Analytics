import pandas as pd
import os

# Healthcare source tables
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
print("HEALTHCARE BRONZE LAYER INGESTION STARTED")
print("=" * 60)

for table in tables:

    try:
        input_file = f"data/raw/{table}.csv"
        output_folder = f"data/bronze/{table}"

        print(f"\nProcessing: {table}")

        # Create bronze folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Read source file
        df = pd.read_csv(input_file)

        print(f"Rows Loaded: {len(df)}")
        print(f"Columns: {len(df.columns)}")

        # Save bronze copy
        output_file = f"{output_folder}/{table}.csv"

        df.to_csv(
            output_file,
            index=False
        )

        print(f"Bronze table created: {output_file}")

    except Exception as e:
        print(f"Error processing {table}: {e}")

print("\n" + "=" * 60)
print("BRONZE LAYER CREATED SUCCESSFULLY")
print("=" * 60)