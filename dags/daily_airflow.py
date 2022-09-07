from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from csv_bigquery import insert_rows1
from airflow.operators.bash import BashOperator

args = {
    'owner': 'revathi',
    'start_date': days_ago(1) # make start date in the past
}

#defining the dag object
dag = DAG(
    dag_id='insert_rows',
    default_args=args,
    schedule_interval='@daily' #to make this workflow happen every day
)
 
#assigning the task for our dag to do
with dag:

    hello_world = PythonOperator(
        task_id='google_bq',
        python_callable=insert_rows1,
        provide_context=True
    )