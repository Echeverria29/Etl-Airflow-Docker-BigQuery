# Usar una imagen base con Python 3.12 y Apache Airflow 3.0.0
FROM apache/airflow:3.0.0-python3.12

# Cambiar a root para instalar dependencias del sistema
USER root

# Instalar dependencias necesarias (PostgreSQL, etc.)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-psycopg2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Volver al usuario airflow
USER airflow

# Comando por defecto
CMD ["bash"]