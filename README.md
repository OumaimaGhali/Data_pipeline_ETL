# Data_pipeline_ETL
## ETL (Extract, Transform, Load):

A data integration process comprising three key stages - extraction (collecting data from various sources), transformation (modifying and cleaning data to a consistent format), and loading (storing the transformed data in a centralized repository). ETL ensures data quality and facilitates efficient analysis for business intelligence.

<p align="center">
  <img width="600" height="300" src="https://learn.microsoft.com/en-us/azure/architecture/data-guide/images/etl.png" alt="Your Image Alt Text">
</p>
## Data from SQL server to PostgreSQL 
# Step 1:

## Open pgAdmin4:

## Create a Database:
Right-click on "Databases."
Choose "Create" > "Database..."
Name it (e.g., "mydatabase").
Click "Save" or "OK."

## Create a User:
Right-click on "Login/Group Roles."
Choose "Create" > "Login/Group Role..."
Name it (e.g., "myuser").
Set a password.
Check "Can login" and "Create database."
Click "Save" or "OK."

## Assigning Privileges:
Right-click on your database ("mydatabase").
Choose "Properties."
Go to the "Security" tab.
Add "myuser" to the "Owner" field.
Click "Save" or "OK."

# Step 2:
## Restore AdventureWorks Database:

Open SQL Server Management Studio (SSMS) and connect to your SQL Server instance.
Right-click on "Databases" in the Object Explorer and choose "Restore Database..."
Select the AdventureWorks backup file and click "OK" to restore the database.

## Create User and Grant Privileges:
Open a new query in SSMS.
Use the CREATE LOGIN and CREATE USER commands to create a user with a specified password.
Use the GRANT command to give the user specific privileges (e.g., SELECT, INSERT, UPDATE, DELETE) on a particular schema within the AdventureWorks database.

<p align="center">
  <img width="600" height="300" src="https://www.endpointdev.com/blog/2019/01/migrate-from-sql-server-to-postgresql/sql-server-to-postgres.jpg" alt="Your Image Alt Text">
</p>

# ETL: 
The Python script does two main things. First, it grabs data from specific tables in a Microsoft SQL Server like DimProduct, DimProductSubcategory, and DimProductCategory. Second, it puts that data into matching tables in a PostgreSQL database. The script uses environment variables to keep things like passwords safe and relies on libraries like SQLAlchemy and pandas for working with the data. Think of it as a simple tool for moving data between a SQL Server and a PostgreSQL database.
