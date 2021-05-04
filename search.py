import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="booking")

    cursor = connection.cursor()
    cursor.execute("SELECT c.name FROM cities c LEFT JOIN venues v "
                   "ON c.country_code=v.country_code LEFT JOIN events e "
                   "ON v.venue_id=e.venue_id WHERE e.event_id BETWEEN 1 AND 2"
                   )
    record = cursor.fetchall()
    print("Результат", record)

    cursor = connection.cursor()
    cursor.execute("SELECT c.country_name FROM countries c LEFT JOIN cities ci "
                   "ON ci.country_code=c.country_code LEFT JOIN venues v "
                   "ON v.country_code=ci.country_code LEFT JOIN events e "
                   "ON e.venue_id=v.venue_id WHERE e.title LIKE 'LARP%'"
                   )
    record = cursor.fetchall()
    print("Результат", record)

    cursor = connection.cursor()
    cursor.execute("SELECT c.country_name FROM countries c LEFT JOIN cities ci "
                   "ON c.country_code=ci.country_code LEFT JOIN venues v "
                   "ON ci.country_code=v.country_code WHERE private is True"
                   )
    record = cursor.fetchall()
    print("Результат", record)

    cursor = connection.cursor()
    cursor.execute("SELECT v.name FROM venues v LEFT JOIN events e "
                   "ON v.venue_id=e.venue_id WHERE e.starts BETWEEN SYMMETRIC '2012-01-01' AND '2012-03-31'"
                   )
    record = cursor.fetchall()
    print("Результат", record)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")