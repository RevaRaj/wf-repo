def insert_rows1():
    
    #   To avoid import errors in Airflow 
    from google.cloud import bigquery
    from google.oauth2 import service_account
    import pandas as pd
    
    #   Credentials to authenticate bigquery(GC)
    cred = service_account.Credentials.from_service_account_file("/opt/airflow/data/winter-inkwell-361409-25baad0824e0.json")

    #   Construct a BigQuery client object.
    client = bigquery.Client(credentials=cred,project='winter-inkwell-361409')

    #   Reading csv file
    csvFile = pd.read_csv("/opt/airflow/data/Managers.csv")

    #   Defining schema for the table that is going to be created
    schema = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("year", "INTEGER", mode="REQUIRED"),
    ]

    #   Creating dataset if not there already
    dataset = client.create_dataset("googlewf1",exists_ok=True) 

    #   Creating table in BQ
    table_ref = dataset.table('csv_bq_table')
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table,)  # Make an API request.

    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )
    
    fullData = []

    #   Collecting data from dataframe to list to sedn it to bigquery table
    for i, row in csvFile.iterrows():
        temp=dict()
        temp['full_name'] = row['full_name']
        temp['year'] = row['age']
        fullData.append(temp)

    table = client.get_table(table_ref)

    #   All rows in single insert
    client.insert_rows(table, fullData)