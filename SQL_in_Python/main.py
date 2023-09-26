import pyodbc
import pandas as pd
import sqlalchemy

print(pyodbc.drivers())

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Pa55word!'
driver = 'ODBC Driver 17 for SQL Server'

pyodbc_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
sqlalchemy_conn = sqlalchemy.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
cursor = pyodbc_conn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
# print(row)

cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# print(cust_rows)

cust_rows_obj = cursor.execute("SELECT * FROM Customers;")
customers_df = pd.DataFrame(cust_rows_obj)
# print(customers_df)

sql_query = 'SELECT * FROM Customers'
df = pd.read_sql(sql_query, sqlalchemy_conn)
# print(df)

# Creating the DataFrame
paris_cus_df = pd.read_sql("SELECT * FROM Customers WHERE city = 'paris'", con=sqlalchemy_conn)
# print(paris_cus_df)

# Using to_sql to create a table from the DataFrame
paris_cus_df.to_sql(name="paris_customers", con=sqlalchemy_conn, if_exists="replace")

query = pd.read_sql_query("SELECT * FROM paris_customers;", con=sqlalchemy_conn)
print(query)

sql_query = "SELECT * FROM Products WHERE UnitPrice > 20;"
unitprice_above_20_df = pd.read_sql(sql_query, sqlalchemy_conn)
# print(unitprice_above_20_df)


continued_df = unitprice_above_20_df.drop(unitprice_above_20_df[unitprice_above_20_df["Discontinued"] == False].index)
# print(continued_df)

continued_df.to_sql(name="continued_up_20", con=sqlalchemy_conn, if_exists='replace')


query = pd.read_sql_query("SELECT * FROM continued_up_20;", con=sqlalchemy_conn)
print(query)
