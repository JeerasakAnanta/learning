from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


# Function to check disk space
def check_disk_space(**kwargs):
    # You can adjust this path as needed
    path = "/"
    statvfs = os.statvfs(path)
    free_space = statvfs.f_frsize * statvfs.f_bavail  # Free space in bytes
    gb_free_space = free_space / (1024**3)  # Convert to GB
    print(f"Free disk space on {path}: {gb_free_space:.2f} GB")

    # You can also push this value to XCom for later use
    kwargs["ti"].xcom_push(key="free_disk_space", value=gb_free_space)


# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 10, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    "check_disk_space_dag",
    default_args=default_args,
    description="A simple DAG to check disk space",
    schedule_interval=timedelta(days=1),
)

# Create a task to check disk space
check_disk_task = PythonOperator(
    task_id="check_disk_space",
    python_callable=check_disk_space,
    provide_context=True,
    dag=dag,
)

# Set task dependencies (if needed)
# In this simple example, we only have one task.

if __name__ == "__main__":
    dag.cli()
