import psycopg2
from psycopg2 import sql

# Replace these with your actual values
DB_NAME = 'task_manager'
DB_USER = 'admin'
DB_PASSWORD = 'admin'

# Connect to the default PostgreSQL database
conn = psycopg2.connect(dbname='postgres', user=DB_USER, password=DB_PASSWORD)

# Create a new database
with conn.cursor() as cursor:
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))

# Create a new user and grant privileges on the database
with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD) as conn:
    with conn.cursor() as cursor:
        cursor.execute(sql.SQL("CREATE USER {} WITH PASSWORD %s").format(sql.Identifier(DB_USER)), [DB_PASSWORD])
        cursor.execute(sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(sql.Identifier(DB_NAME), sql.Identifier(DB_USER)))

print("Database and user created successfully.")
