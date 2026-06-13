USE healthcare_dw;

-- =====================================================
-- KPI QUERIES
-- =====================================================

-- Total Patients

SELECT COUNT(*) AS TotalPatients
FROM dim_patient;

-- Total Providers

SELECT COUNT(*) AS TotalProviders
FROM dim_provider;

-- Total Organizations

SELECT COUNT(*) AS TotalOrganizations
FROM dim_organization;

-- Total Claims

SELECT COUNT(*) AS TotalClaims
FROM fact_claim;

-- Total Encounters

SELECT COUNT(*) AS TotalEncounters
FROM fact_encounter;

-- =====================================================
-- PATIENT ANALYTICS
-- =====================================================

-- Patient Age Distribution

SELECT
    CASE
        WHEN TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) <= 17 THEN '0-17'
        WHEN TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) BETWEEN 18 AND 34 THEN '18-34'
        WHEN TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) BETWEEN 35 AND 49 THEN '35-49'
        WHEN TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) BETWEEN 50 AND 64 THEN '50-64'
        ELSE '65+'
    END AS AgeGroup,
    COUNT(*) AS TotalPatients
FROM dim_patient
GROUP BY AgeGroup
ORDER BY AgeGroup;



-- =====================================================
-- EXECUTIVE DASHBOARD ANALYTICS
-- =====================================================

-- Top 10 Organizations by Encounters

SELECT
    organization,
    COUNT(*) AS EncounterCount
FROM fact_encounter
GROUP BY organization
ORDER BY EncounterCount DESC
LIMIT 10;

-- Encounter Class Distribution

SELECT
    encounterclass,
    COUNT(*) AS Encounters
FROM fact_encounter
GROUP BY encounterclass
ORDER BY Encounters DESC;

-- Most Frequent Encounter Types

SELECT
    description,
    COUNT(*) AS EncounterCount
FROM fact_encounter
GROUP BY description
ORDER BY EncounterCount DESC
LIMIT 10;

-- Top Providers by Encounters

SELECT
    provider,
    COUNT(*) AS EncounterCount
FROM fact_encounter
GROUP BY provider
ORDER BY EncounterCount DESC
LIMIT 10;


-- =====================================================
-- CLAIMS ANALYTICS
-- =====================================================

-- Claims by Department

SELECT
    departmentid,
    COUNT(*) AS ClaimCount
FROM fact_claim
GROUP BY departmentid
ORDER BY ClaimCount DESC;

-- Claim Status Breakdown

SELECT
    status1,
    COUNT(*) AS TotalClaims
FROM fact_claim
GROUP BY status1;


-- =====================================================
-- RESOURCE UTILIZATION ANALYTICS
-- =====================================================

-- Top Providers by Utilization

SELECT
    name,
    utilization
FROM dim_provider
ORDER BY utilization DESC
LIMIT 10;

-- Top Organizations by Revenue

SELECT
    name,
    revenue
FROM dim_organization
ORDER BY revenue DESC
LIMIT 10;

