from airflow                  import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime                 import datetime, timedelta

"""
trigger setting example
"""

dag1 = DAG(
    dag_id = 'HelloWorld',
    start_date = datetime.today() - timedelta(days=1),
    catchup=False,
    tags=['example'],
    schedule = '0 2 * * *')

dag2 = DAG(
    dag_id = 'GoodBye',
    start_date = datetime.today() - timedelta(days=1),
    catchup=False,
    tags=['example'],
    schedule = '0 2 * * *')


def print_hello():
    print("hello!")
    return "hello!"

def print_goodbye():
    print("goodbye!")
    return "goodbye!"

print_hello = PythonOperator(
    task_id = 'print_hello',
    python_callable = print_hello,
    dag = dag1)

print_goodbye = PythonOperator(
    task_id = 'print_goodbye',
    python_callable = print_goodbye,
    dag = dag2)

trigger = TriggerDagRunOperator(
    task_id = 'trigger',
    trigger_dag_id = 'GoodBye',
    dag = dag1
)

print_hello >> print_goodbye