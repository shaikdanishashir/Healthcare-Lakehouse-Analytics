# 🏥 Healthcare Lakehouse Analytics Platform

## 📌 Project Overview

This project demonstrates the design and implementation of an end-to-end Healthcare Analytics Platform using a Medallion (Bronze, Silver, Gold) Lakehouse Architecture.

The objective is to transform raw healthcare datasets into analytics-ready data and build interactive dashboards that support healthcare decision-making.

The solution processes patient, provider, organization, encounter, and claims data to generate actionable insights into healthcare utilization, patient demographics, and provider performance.

---

## 🎯 Business Problem

Healthcare organizations generate large volumes of operational and clinical data.

Without a structured analytics platform, it becomes difficult to:

- Monitor patient activity
- Analyze encounter trends
- Evaluate provider performance
- Understand healthcare utilization patterns
- Support data-driven decision making

This project addresses these challenges by building a healthcare analytics solution from raw data ingestion to dashboard visualization.

---

## 🏗 Architecture

```text
Raw Healthcare Data
        │
        ▼
 Bronze Layer
 (Raw Ingestion)
        │
        ▼
 Silver Layer
 (Data Cleaning & Transformation)
        │
        ▼
 Gold Layer
 (Analytics Ready Data)
        │
        ▼
 SQL Analysis
        │
        ▼
 Power BI Dashboard
```

---

## 📊 Dataset

Dataset Source:

Synthea Synthetic Healthcare Dataset

https://synthea.mitre.org/

The dataset contains synthetic healthcare records including:

- Patients
- Providers
- Organizations
- Encounters
- Claims

### Dataset Statistics

| Table | Records |
|---------|---------:|
| Patients | 1,163 |
| Providers | 5,056 |
| Organizations | 1,127 |
| Encounters | 61,459 |
| Claims | 117,889 |

---

## ⚙️ ETL Pipeline

### Bronze Layer

- Ingest raw healthcare datasets
- Preserve source data
- Initial validation

### Silver Layer

- Handle missing values
- Standardize formats
- Remove inconsistencies
- Data quality checks

### Gold Layer

- Generate analytics-ready datasets
- Create dimension and fact tables
- Prepare data for reporting and visualization

---

## 📂 Data Model

### Dimension Tables

#### dim_patient

Contains:

- Patient ID
- Full Name
- Gender
- Birth Date
- City
- State

#### dim_provider

Contains:

- Provider ID
- Provider Name
- Specialty
- Location
- Utilization Metrics

#### dim_organization

Contains:

- Organization ID
- Organization Name
- Revenue
- Utilization Metrics

---

### Fact Tables

#### fact_encounter

Contains:

- Encounter ID
- Patient
- Provider
- Organization
- Encounter Class
- Encounter Cost
- Claim Cost

#### fact_claim

Contains:

- Claim ID
- Diagnosis Information
- Claim Status
- Department Information
- Billing Information

---

## 🛠 Technologies Used

- Python
- Pandas
- SQL
- Power BI
- Git
- GitHub
- Data Warehousing
- Lakehouse Architecture

---

## 📈 SQL Business Analysis

The project includes SQL-based business analysis for:

- Total Patients
- Total Providers
- Total Organizations
- Total Encounters
- Top Organizations by Encounters
- Encounter Class Distribution
- Top Providers by Utilization

SQL scripts are available in:

```text
sql/analysis.sql
```

---

## 📊 Power BI Dashboard

The dashboard provides executive-level healthcare analytics through:

### KPI Metrics

- Total Patients
- Total Providers
- Total Organizations
- Total Claims
- Total Encounters

### Patient Analytics

- Patients by Birth Year
- Patients by Age Group
- Gender Filtering

### Encounter Analytics

- Encounter Class Distribution
- Most Frequent Encounter Types

### Organization Analytics

- Top Organizations by Encounters

### Provider Analytics

- Top Providers by Utilization

---

## 🔍 Key Insights

### Healthcare Network

- 1,163 patients received healthcare services.
- 61,459 encounters were recorded across the network.
- 5,056 healthcare providers contributed to patient care.
- 1,127 healthcare organizations participated in healthcare delivery.

### Demographic Insights

- The 65+ age group represents the largest patient segment.
- Healthcare demand is higher among senior populations.

### Operational Insights

- Wellness encounters are the most common healthcare interaction.
- A small number of organizations account for a significant share of total encounters.
- Provider utilization varies significantly across the healthcare network.

---

## 📁 Project Structure

```text
Healthcare-Lakehouse-Analytics
│
├── README.md
│
├── spark_jobs/
│   ├── 01_ingest_patients.py
│   ├── 02_bronze_layer.py
│   ├── 03_silver_layer.py
│   ├── 04_silver_all_tables.py
│   └── 05_gold_layer.py
│
├── sql/
│   └── analysis.sql
│
├── dashboards/
│   └── Healthcare_Analytics_Dashboard.pbix
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
└── docs/
    └── dashboard.png
```

---

## 📷 Dashboard Preview

Add your final dashboard screenshot here.

Example:

```markdown
![Healthcare Dashboard](docs/dashboard.png)
```

---

## 🚀 Skills Demonstrated

### Data Engineering

- ETL Pipeline Development
- Data Cleaning
- Data Transformation
- Data Validation

### Data Warehousing

- Fact and Dimension Modeling
- Star Schema Concepts
- Lakehouse Architecture

### Business Intelligence

- KPI Design
- Dashboard Development
- Data Visualization
- Data Storytelling

### Analytics

- Healthcare Data Analysis
- Provider Performance Analysis
- Patient Demographic Analysis
- Operational Analytics

---

## 👨‍💻 Author

**Ashir**

Master's Student – Information Systems

Central Michigan University

---

## Disclaimer

This project uses synthetic healthcare data generated by the Synthea Synthetic Patient Generator. All patient records are fictional and do not represent real individuals.
