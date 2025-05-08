config {
  type: "table",
  description: "Tabla de clientes importados desde API randomuser"
}

SELECT
  id.value       AS id,
  name.first     AS first_name,
  name.last      AS last_name,
  email,
  dob.date       AS birth_date
FROM
  ${ref("clientes_dataset_clientes")}
