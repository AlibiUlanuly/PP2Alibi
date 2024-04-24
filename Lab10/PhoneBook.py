import csv
import psycopg2

# Function to create the phonebook table
def create_phonebook_table():
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                phone VARCHAR(20)
            )
        """)
        
        conn.commit()
        print("PhoneBook table created successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error creating phonebook table:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function to insert data from CSV file
def insert_from_csv(phonebook):
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        with open(phonebook, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if it exists
            for row in reader:
                name, phone = row
                cursor.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        
        conn.commit()
        print("Data inserted successfully from CSV.")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting data from CSV:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function to insert data from console
def insert_from_console():
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        
        cursor.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        
        conn.commit()
        print("Data inserted successfully from console.")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting data from console:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function to update data in the phonebook
def update_phonebook_data(name_to_update, new_name, new_phone, conn):
    try:
        cursor = conn.cursor()

        # Execute the update query
        cursor.execute("UPDATE phonebook SET name = %s, phone = %s WHERE name = %s RETURNING id, name, phone", (new_name, new_phone, name_to_update))

        # Fetch the updated row
        updated_row = cursor.fetchone()

        # Display the updated data
        if updated_row:
            print(f"Data updated successfully. ID: {updated_row[0]}, Name: {updated_row[1]}, Phone: {updated_row[2]}")
        else:
            print("No records updated.")
        
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error updating data:", error)
    finally:
        if cursor:
            cursor.close()

# Function to query data from the phonebook
def query_phonebook_data():
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM phonebook")
        rows = cursor.fetchall()
        
        if rows:
            print("PhoneBook:")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("PhoneBook is empty.")
    except (Exception, psycopg2.Error) as error:
        print("Error querying data:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function to delete data from the phonebook
def delete_from_phonebook():
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        name_to_delete = input("Enter the name to delete: ")
        
        cursor.execute("DELETE FROM phonebook WHERE name = %s", (name_to_delete,))
        
        conn.commit()
        print("Data deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error deleting data:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Main function to run the phonebook application
def main():
    create_phonebook_table()
    while True:
        print("\nOptions:")
        print("1. Insert data from CSV file")
        print("2. Insert data from console")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            csv_file = input("Enter the CSV file path: ")
            insert_from_csv(csv_file)
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_phonebook_data()
        elif choice == '4':
            query_phonebook_data()
        elif choice == '5':
            delete_from_phonebook()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()