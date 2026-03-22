import psycopg2
from config import load_config

def delete_by_name(name):
    query = "DELETE FROM phonebook WHERE first_name = %s"

    try:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (name,))
            conn.commit()

        print("Deleted")

    except Exception as error:
        print(error)


if __name__ == '__main__':
    name = input("Enter name to delete: ")
    delete_by_name(name)