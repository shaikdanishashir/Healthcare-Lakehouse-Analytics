import pandas as pd
import os

print("=" * 60)
print("GOLD LAYER PROCESSING STARTED")
print("=" * 60)

# --------------------------
# DIM PATIENT
# --------------------------

patients = pd.read_csv(
    "data/silver/patients/patients.csv"
)

dim_patient = patients[[
    "id",
    "first",
    "last",
    "gender",
    "birthdate",
    "city",
    "state"
]].copy()

dim_patient.columns = [
    "patient_id",
    "first_name",
    "last_name",
    "gender",
    "birth_date",
    "city",
    "state"
]

dim_patient.insert(
    0,
    "patient_sk",
    range(1, len(dim_patient) + 1)
)

# --------------------------
# DIM PROVIDER
# --------------------------

providers = pd.read_csv(
    "data/silver/providers/providers.csv"
)

dim_provider = providers.copy()

dim_provider.insert(
    0,
    "provider_sk",
    range(1, len(dim_provider) + 1)
)

# --------------------------
# DIM ORGANIZATION
# --------------------------

organizations = pd.read_csv(
    "data/silver/organizations/organizations.csv"
)

dim_organization = organizations.copy()

dim_organization.insert(
    0,
    "organization_sk",
    range(1, len(dim_organization) + 1)
)

# --------------------------
# FACT ENCOUNTER
# --------------------------

encounters = pd.read_csv(
    "data/silver/encounters/encounters.csv"
)

fact_encounter = encounters.copy()

# --------------------------
# FACT CLAIM
# --------------------------

claims = pd.read_csv(
    "data/silver/claims/claims.csv"
)

fact_claim = claims.copy()

# --------------------------
# SAVE GOLD TABLES
# --------------------------

gold_tables = {
    "dim_patient": dim_patient,
    "dim_provider": dim_provider,
    "dim_organization": dim_organization,
    "fact_encounter": fact_encounter,
    "fact_claim": fact_claim
}

for name, df in gold_tables.items():

    folder = f"data/gold/{name}"

    os.makedirs(
        folder,
        exist_ok=True
    )

    df.to_csv(
        f"{folder}/{name}.csv",
        index=False
    )

    print(f"Created: {name}")

print("\nGOLD LAYER COMPLETED")