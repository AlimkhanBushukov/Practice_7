import psycopg2
from config import load_config

def get_all_contacts():
    with psycopg2.connect(**load_config()) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            rows = cur.fetchall()

            print("All contacts:")
            for row in rows:
                print(row)


def find_by_name(name):
    with psycopg2.connect(**load_config()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE first_name = %s",
                (name,)
            )
            rows = cur.fetchall()

            print("Search by name:")
            for row in rows:
                print(row)


def find_by_phone_part(part):
    with psycopg2.connect(**load_config()) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE phone LIKE %s",
                (f"%{part}%",)
            )
            rows = cur.fetchall()

            print("Search by phone:")
            for row in rows:
                print(row)


if __name__ == '__main__':
    get_all_contacts()
    find_by_name("Ali")
    find_by_phone_part("8777")