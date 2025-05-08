-- dynamic_masking.sql

CREATE OR REPLACE ROW ACCESS POLICY mask_email_policy
ON `etl-airflow-project-459015.etl_dataset.clientes`
GRANT TO ('allAuthenticatedUsers')
FILTER USING (
  REGEXP_CONTAINS(email, r'.*@example\.com')
);
