import psycopg2

def query_phonebook_data_pagination(limit, offset):
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
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