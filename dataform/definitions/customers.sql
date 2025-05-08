config {
  type: "table",
  description: "Tabla de clientes importados desde API randomuser"
}

SELECT
  full_name,
  email,
  national_id,
  country
FROM
  ${ref("clientes")}
