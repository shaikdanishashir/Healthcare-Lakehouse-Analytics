from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Healthcare Lakehouse") \
    .getOrCreate()

# Read Patients CSV
patients = spark.read.csv(
    "data/raw/patients.csv",
    header=True,
    inferSchema=True
)

print("\n=== PATIENTS SCHEMA ===")
patients.printSchema()

print("\n=== SAMPLE RECORDS ===")
patients.show(5, truncate=False)

print("\n=== TOTAL PATIENTS ===")
print(patients.count())

spark.stop()