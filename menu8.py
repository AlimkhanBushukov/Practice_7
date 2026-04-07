from practice8 import (
    search_pattern,
    upsert_user,
    bulk_insert_csv,
    get_paginated,
    delete_user
)

def menu():
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Search")
        print("2. Insert/Update (Upsert)")
        print("3. Bulk Insert (CSV)")
        print("4. Pagination")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search_pattern(input("Enter search pattern: "))
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            upsert_user(name, phone)
        elif choice == "3":
            bulk_insert_csv("data.csv")
        elif choice == "4":
            page = int(input("Page number: "))
            limit = int(input("Rows per page: "))
            get_paginated(page, limit)
        elif choice == "5":
            delete_user(input("Enter name or phone: "))
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()