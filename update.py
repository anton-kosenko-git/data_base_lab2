import psycopg2
from psycopg2 import Error


def update_table(event_id, title):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="postgres",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="booking")

        cursor = connection.cursor()
        print("Таблица до обновления записи")
        sql_select_query = """SELECT * FROM events WHERE event_id = %s"""
        cursor.execute(sql_select_query, (event_id,))
        record = cursor.fetchone()
        print(record)

        # Обновление отдельной записи
        sql_update_query = """UPDATE events SET title = %s WHERE event_id = %s"""
        cursor.execute(sql_update_query, (title, event_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно обновлена")

        print("Таблица после обновления записи")
        sql_select_query = """SELECT * FROM events WHERE event_id = %s"""
        cursor.execute(sql_select_query, (event_id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

update_table(4, "International Labor Day")
