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

# Cambiar al usuario airflow antes de instalar dependencias Python
USER airflow

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar dependencias de Python como usuario airflow
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto
CMD ["bash"]
