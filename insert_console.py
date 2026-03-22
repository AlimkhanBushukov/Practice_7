import psycopg2
from config import load_config

def insert_console():
    name = input("Name: ")
    phone = input("Phone: ")

    query = "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)"

    try:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (name, phone))
            conn.commit()

        print("Inserted")

    except Exception as error:
        print(error)


if __name__ == '__main__':
    insert_console()