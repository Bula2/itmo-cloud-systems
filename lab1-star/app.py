import os
import psycopg2

pg_host = os.environ["POSTGRES_HOST"]
pg_db = os.environ["POSTGRES_DB"]
pg_user = os.environ["POSTGRES_USER"]
pg_password = os.environ["POSTGRES_PASSWORD"]
pg_port = os.environ["POSTGRES_PORT"]


def write_to_database(db_value):
    try:
        connection = psycopg2.connect(
            host=pg_host,
            database=pg_db,
            user=pg_user,
            password=pg_password,
            port=pg_port,
        )
        cursor = connection.cursor()
        insert_query = "INSERT INTO mytable (value) VALUES (%s)"
        cursor.execute(insert_query, (db_value,))
        connection.commit()
        cursor.close()
        connection.close()

        print(f"Значение '{db_value}' успешно записано в базу данных!")
    except Exception as e:
        print(f"Ошибка при записи в базу данных: {e}")


if __name__ == "__main__":
    db_value = os.environ["VALUE"]
    if db_value:
        write_to_database(db_value)
    else:
        print("Значение не указано!")
