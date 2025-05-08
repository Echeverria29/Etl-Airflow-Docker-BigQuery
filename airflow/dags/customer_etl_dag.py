from airflow import DAG
from airflow.operators.python import PythonOperator  # ✅ Importación actualizada
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime
import os
import requests
import pandas as pd

def fetch_customers():
    df = pd.DataFrame([requests.get('https://randomuser.me/api/').json()['results'][0] for _ in range(100)])
    os.makedirs('/opt/airflow/data', exist_ok=True)
    df.to_csv('/opt/airflow/data/customers.csv', index=False)

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='customer_etl_pipeline',
    schedule_interval='@daily',
    catchup=False,
    default_args=default_args,
    description='ETL pipeline to fetch customers, upload to GCS, and load to BigQuery',
    tags=['example', 'gcs', 'bigquery']
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_customers',
        python_callable=fetch_customers
    )

    upload_task = LocalFilesystemToGCSOperator(
        task_id='upload_to_gcs',
        src='/opt/airflow/data/customers.csv',
        dst='customers/customers.csv',
        bucket='TU_BUCKET_GCS'  # 👈 Reemplaza con tu bucket real
    )

    bq_load_task = BigQueryInsertJobOperator(
        task_id='load_to_bq',
        configuration={
            "load": {
                "destinationTable": {
                    "projectId": "TU_PROYECTO",         # 👈 Reemplaza con tu ID de proyecto
                    "datasetId": "clientes_dataset",
                    "tableId": "clientes"
                },
                "sourceUris": ["gs://TU_BUCKET_GCS/customers/customers.csv"],
                "sourceFormat": "CSV",
                "autodetect": True,
                "skipLeadingRows": 1
            }
        }
    )

    fetch_task >> upload_task >> bq_load_task
