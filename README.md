# Proyecto ETL con Apache Airflow, Google Cloud y Docker

Este proyecto implementa una canalización ETL (Extract, Transform, Load) usando **Apache Airflow** para obtener datos de clientes de una API pública (randomuser.me), almacenarlos en **Google Cloud Storage (GCS)** y cargarlos en **Google BigQuery**. Además, este proyecto está preparado para ejecutarse tanto en un entorno local como en Docker.

## Requisitos previos

### Herramientas necesarias:

- **Python 3.12** o superior.
- **Docker** y **Docker Compose** para ejecutar el contenedor de Airflow.
- **Google Cloud Platform (GCP)** con acceso a BigQuery, GCS y IAM.
- **Google Cloud SDK** (opcional, si deseas interactuar con GCP desde la terminal).
- **git** (para clonar el repositorio).

### Instalación en GCP:

Antes de ejecutar el proyecto, debes configurar varios servicios en GCP para que funcione correctamente:

### Paso 1: Crear un Proyecto en GCP

1. Ve a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un nuevo proyecto. (Ej. `etl-airflow-project`).
3. Anota el ID del proyecto que será utilizado en el archivo de configuración.

### Paso 2: Crear un Bucket en Google Cloud Storage (GCS)

1. En la **Google Cloud Console**, ve a **Storage** > **Browser** y haz clic en **Create Bucket**.
2. Dale un nombre único al bucket, como `etl-airflow-bucket`.
3. Asegúrate de que el almacenamiento sea público o de acceder a él desde tu cuenta de GCP (configura permisos según tus necesidades).
4. Anota el nombre del bucket para usarlo en el archivo de configuración.

### Paso 3: Crear un Dataset en Google BigQuery

1. Ve a **BigQuery** en Google Cloud Console.
2. Crea un nuevo Dataset llamado `clientes_dataset`.
3. Crea una tabla llamada `clientes` donde se almacenarán los datos de los clientes.

### Paso 4: Crear y descargar las Credenciales de Google Cloud

1. Ve a **IAM & Admin** > **Service Accounts** y crea una cuenta de servicio.
2. Asigna los roles adecuados para que la cuenta de servicio pueda interactuar con BigQuery y GCS, como `BigQuery Admin`, `Storage Admin` y `Viewer`.
3. Descarga el archivo de claves JSON de la cuenta de servicio y guárdalo en un directorio seguro. Este archivo es necesario para la autenticación.

### Paso 5: Configuración de la variable de entorno para las credenciales

En tu máquina local, configura la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` para que apunte al archivo de claves descargado:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/ruta/a/tu/keyfile.json"
