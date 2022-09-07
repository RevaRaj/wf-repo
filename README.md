#       GC Credentials

        1)  To access google cloud we need to create a service account and credentials. Below steps need to be followed.
        
        2)  Go to Google cloud console ---> big query --> enabled APIs and services -->  big query API --> credentials --> 
            create  credentials -- > service account --> provide any serv acc name(samplegoogle) --> create and continue --> add below 2 roles then click continue and finally  done 
            a)	project and owner
            b)	bigquery admin
        
        3)	Once done click that service acc(samplegoogle) and go to keys --> addkey -> create new key --> json --> key will be 
            created and downloaded,	use this json key file to access bigquery.
        
        4)	I've used DBeaver to visualize the data. In DBeaver new connection --> project --> winter-inkwell-361409(this is 
            getting created automatically when you create credentials) and provide your key path(downloaded json)
        
        5)	Test connection that's it, you are connected to big query.


##      Python-BQ

        1)  Using service account module for accessing downloaded credentials.

        2)  Create a bq client and read the csv file using pandas since it loads the entire data in single shot.
        
        3)  Defining schema for my table since i'm going to create a dataset and table.

        4)  Once dataset and table are created reading the data from pandas dataframe and pushing them to BQ in single shot.


###     Scheduling

        1)  Airflow scheduling has been used to schedule and monitor the jobs which is more secure and provides central visualization 
            for jobs in UI.
        
        2)  DAGs provides a useful relationshp informations even for complex jobs and sclae effectively based on needs.

        3)  I've installed Airflow in docker container. Below are the steps.

                a)  Download Docker Desktop windows app.
                b)  Create directory 'airflow-latest' and inside that run beow curl cmnd
                    ```curl -LfO "https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml"```
                c)  Create 3 directories inside your airflow dir ``` mkdir dags,logs,plugins ```.
                d)  Set the airflow user using ``` echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env	```.
                e)  Initialize airflow DB using ``` docker-compose up airflow-init ```.
                f)  Start airflow services by ``` docker-compose up ```.
                g)  Use ``` docker ps ``` to check the status of containers, wait until all the container status is healthy.
                h)  Now airflow has been successfully installed inside the container check docker desktop(container should be running).
                i)  In browser type  localhost:8080 --> uname - airflow, pwd - airflow(these can be found in docker-compose.yaml file).
                j)  If you want to inspect particular container ``` docker exec -it 5bb37e6634d3 bash ```, 5bb37e6634d3 - container id
                k)  Create a python file inside a dags/ with scheduing and owner args. and import your python script(where you have 
                    done the csv to BQ load).
                l)  Start the containers again and work with this on the Airflow dashboard -- > ```docker-compose up -d```.
                m)  If any errors in your pgm then that can be seen at top of AIrflow UI, once you fix the errors it will come
                    under DAG aifrlow UI.
                n)  Click on the DAG id and in graph you will be able to see the graphical view of the entire flow.
                o)  I've scheduled my DAG to run on daily basis, but we can do manual and hourly, weekly,monthly, yearly as well.
                p)  To make Airflow to access your csv and credentials file create data folder and provide their path
                    - ./data:/opt/airflow/data in docker-compose file.
                q)  Successful job completion will show green in color, for logs click the task and check the logs.
                r)  That's it , you are good to go with your script running everyday. For a safer side I've removed my credentials
                    json from here.
                s)  Please find the SQL query answers in sql.db file.  



####    SQL

        1)  For make use of the wunderflats.db in DBeaver create new connection and provide the .db file path in JDBC URL
            that's it test the connection and play with your queries.

        2)  Validation :    Completeness of the query which does not return any NULL/BLANK values.
                            We can check for uniqueness of values.

        3)  I would definitely use DBT(Data Build Tool) to do the test on individual queries and subqueries results by using dbt tests.
            Using that we can check the uniqueness, accepted values, Not null. Validation of dates or any other expression using dbtutils.expression.

            Using Macros in dbt we can do generic test for our sql models(which is again sql query), one advantage is we can re use the test in dbt.