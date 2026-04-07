import csv
import re
from conc import get_connection


def is_valid_phone(phone):
    return re.match(r'^\+7\d{10}$', phone)

#  PATTERN SEARCH
def search_pattern(pattern):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone ILIKE %s",
                (f"%{pattern}%", f"%{pattern}%")
            )
            rows = cur.fetchall()
            if not rows:
                print("No results found")
            else:
                for row in rows:
                    print(row)

#  UPSERT
def upsert_user(name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO phonebook(first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone)
                DO UPDATE SET first_name = EXCLUDED.first_name;
            """, (name, phone))
    print("Inserted or updated successfully")

#  BULK INSERT



def bulk_insert_csv(filename):
    with get_connection() as conn:
        with conn.cursor() as cur:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) != 2:
                        print("Skipping invalid row: " + str(row))
                        continue
                    
                    name, phone = row
                    if is_valid_phone(phone):
                        cur.execute("""
                            INSERT INTO phonebook(first_name, phone)
                            VALUES (%s, %s)
                            ON CONFLICT DO NOTHING
                        """, (name, phone))
                    else:
                        print("Invalid phone skipped: " + str(phone))
            
            # ВАЖНО: Без этой строки данные не запишутся в таблицу!
            conn.commit() 
            
    print("Bulk insert completed")

#  PAGINATION
def get_paginated(page, limit):
    offset = (page - 1) * limit
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s",
                (limit, offset)
            )
            rows = cur.fetchall()
            if not rows:
                print("No data on this page")
            else:
                for row in rows:
                    print(row)

#  DELETE
def delete_user(value):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM phonebook WHERE name=%s OR phone=%s",
                (value, value)
            )
    print("Deleted (if existed)")