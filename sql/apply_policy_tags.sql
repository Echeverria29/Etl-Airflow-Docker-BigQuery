-- apply_policy_tags.sql

ALTER TABLE `etl-airflow-project-459015.etl_dataset.clientes`
ALTER COLUMN email
SET OPTIONS (
  policy_tags = [
    'projects/etl-airflow-project-459015/locations/global/taxonomies/<<TU_TAXONOMY_ID>>/policyTags/<<TU_POLICY_TAG_ID>>'
  ]
);
-- <<TU_TAXONOMY_ID>> y <<TU_POLICY_TAG_ID>>: reemplázalos con los IDs reales de tu Taxonomy y 
-- Policy Tag que creaste en Data Catalog / Dataplex.