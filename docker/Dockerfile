# Usar la imagen base de Apache Airflow 3.0.0 con Python 3.12
FROM apache/airflow:3.0.0

# Cambiar al usuario root para instalar dependencias
USER root

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Volver al usuario airflow para ejecutar Airflow
USER airflow
