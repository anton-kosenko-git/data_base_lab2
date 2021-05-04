import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
    "booking", "postgres", "postgres", "127.0.0.1", "5432"
)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

events = [
    (4, "Workers Day", "2021-01-05", "2021-01-05"),
    (5, "Easter", "2021-02-05", "2021-02-05")
]
events_records = ", ".join(["%s"] * len(events))

insert_query = (
    f"INSERT INTO events (event_id, title, starts, ends) VALUES {events_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, events)

