import psycopg2

def delete_from_phonebook_by_username_or_phone(identifier):
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (identifier, identifier))
        
        conn.commit()
        print("Data deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error deleting data:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
