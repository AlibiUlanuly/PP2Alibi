import psycopg2

def insert_many_users(users):
    try:
        conn = psycopg2.connect("dbname=PhoneBook user=postgres password=Akira123 host=localhost port=5432")
        cursor = conn.cursor()
        
        for user in users:
            name, phone = user
            cursor.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        
        conn.commit()
        print("Users inserted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting users:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()