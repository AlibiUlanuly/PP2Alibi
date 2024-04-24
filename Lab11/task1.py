import psycopg2

def search_phonebook(pattern):
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM phonebook WHERE name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%'))
        rows = cursor.fetchall()
        
        if rows:
            print("Matching Records:")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("No matching records found.")
    except (Exception, psycopg2.Error) as error:
        print("Error searching data:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
