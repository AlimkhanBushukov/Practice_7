import psycopg2
from config import load_config

def create_phonebook():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        phone VARCHAR(20)
    );
    """

    try:
        with psycopg2.connect(**load_config()) as conn:
            with conn.cursor() as cur:
                cur.execute(query)

        print("Phonebook table created")

    except Exception as error:
        print(error)


if __name__ == '__main__':
    create_phonebook()