echo "running airflow standalone "

NO_PROXY="*" AIRFLOW_HOME="$(pwd)/airflow" airflow standalone
