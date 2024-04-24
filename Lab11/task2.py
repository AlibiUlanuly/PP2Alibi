import psycopg2

def insert_or_update_user(name, phone):
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone", (name, phone))
        
        conn.commit()
        print("User inserted/updated successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting/updating user:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
