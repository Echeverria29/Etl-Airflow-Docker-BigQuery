assertion("no_null_emails", """
  SELECT
    COUNT(*) = 0
  FROM
    ${ref("clientes")}
  WHERE
    email IS NULL
""");
