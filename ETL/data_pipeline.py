# Import necessary libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os

# pd from environment variables
db_password = os.environ['DB_PASSWORD']
db_username = os.environ['DB_USERNAME']

# SQL Server connection details
sql_server_driver = "{ODBC Driver 17 for SQL Server}"
sql_server_instance = "DESKTOP-KHKU8QQ\SQLEXPRESS"
sql_server_database = "AdventureWorksDW2019"

# Extract data from SQL Server
def extract():
    src_conn = None
    try:
        # Create the connection string
        conn_str = f'Trusted_connection=no; DRIVER={sql_server_driver};SERVER={sql_server_instance};DATABASE={sql_server_database};UID={db_username};PWD={db_password}'
        src_conn = pyodbc.connect(conn_str)
        src_cursor = src_conn.cursor()

        # Execute query
        src_cursor.execute("""
            SELECT t.name as table_name
            FROM sys.tables t
            WHERE t.name IN ('DimProduct', 'DimProductSubcategory', 'DimProductCategory')
        """)
        src_tables = src_cursor.fetchall()

        for tbl in src_tables:
            # Query and load save data to dataframe
            df = pd.read_sql_query(f'SELECT * FROM {tbl[0]}', src_conn)
            load_to_postgres(df, tbl[0])

    except Exception as e:
        print("Data extract error:", str(e))

    finally:
        # Close the connection in the finally block
        if src_conn:
            src_conn.close()

# Load data to PostgreSQL
def load_to_postgres(df, tbl):
    try:
        postgres_engine = create_engine(f'postgresql://{db_username}:{db_password}@localhost:5432/adventurWorkes')
        print(f'Importing rows for table {tbl}')
        # Save df to PostgreSQL
        df.to_sql(f'stg_{tbl}', postgres_engine, if_exists='replace', index=False)
        print("Data imported successfully")
    except Exception as e:
        print("Data load error:", str(e))

try:
    # Call extract function
    extract()

except Exception as e:
    print("Error while extracting data:", str(e))
