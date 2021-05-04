import psycopg2
from psycopg2 import Error


def delete_data(event_id):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="booking")

        cursor = connection.cursor()
        # Удаление записи
        sql_delete_query = """DELETE FROM events WHERE event_id = %s"""
        cursor.execute(sql_delete_query, (event_id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно удалена")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

delete_data(4)
delete_data(5)
