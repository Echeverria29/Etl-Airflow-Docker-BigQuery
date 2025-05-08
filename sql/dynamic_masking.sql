CREATE OR REPLACE ROW ACCESS POLICY mask_email_policy
ON `TU_PROYECTO.clientes_dataset.clientes`
GRANT TO ('allAuthenticatedUsers')
FILTER USING (REGEXP_CONTAINS(email, r'.*@example.com'));