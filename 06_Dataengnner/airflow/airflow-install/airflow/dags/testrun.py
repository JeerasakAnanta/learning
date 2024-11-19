from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def testing() -> None:
    """
    A simple function that prints a hello world message to the console.

    This function is used by the PythonOperator in the DAG to print a message.
    """
    print("Hello, World!")

default_args = {
    'owner': 'Game',
    'start_date': datetime(2024, 11, 1),
    'retries': 1,
}

with DAG('hello',
        default_args=default_args,
        schedule_interval='0 6 * * *'
        ) as dag:

    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=testing,
    )

