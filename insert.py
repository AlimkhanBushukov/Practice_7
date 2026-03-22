import psycopg2
from config import load_config

def insert_vendor(vendor_name):
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

    vendor_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name,))
                row = cur.fetchone()

                if row:
                    vendor_id = row[0]

                conn.commit()

    except Exception as error:
        print(error)

    return vendor_id


def insert_many_vendors(vendor_list):
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, vendor_list)

            conn.commit()

    except Exception as error:
        print(error)


if __name__ == '__main__':
    insert_vendor("3M Co.")

    insert_many_vendors([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])