from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def hello_world():
    print("Hello World")


# Define the default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 11, 1),  # Adjust the start date as needed
    "retries": 1,
}

# Define the DAG
dag = DAG(
    "hello_world_dag",
    default_args=default_args,
    description="A simple Hello World DAG",
    schedule_interval="@daily",  # Set the schedule interval as needed
)

# Define the task
hello_task = PythonOperator(
    task_id="hello_task",
    python_callable=hello_world,
    dag=dag,
)
