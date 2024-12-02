import psycopg2

# Database connection
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="contacts_db",  # Din databasnamn här
            user="admin",          # Ditt användarnamn här
            password="password",   # Ditt lösenord här
            host="localhost",      # Om du använder localhost
            client_encoding='UTF-8' # För att säkerställa rätt teckenkodning
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_contact(name, phone_number, email, adress):
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO contacts (name, phone_number, email, adress)
                VALUES (%s, %s, %s, %s)
            """, (name, phone_number, email, adress))
            conn.commit()
            cur.close()
            print(f"Contact '{name}' has been created!")
        except Exception as e:
            print(f"Error inserting contact: {e}")
        finally:
            conn.close()

def get_all_contacts():
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM contacts")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            cur.close()
        except Exception as e:
            print(f"Error fetching contacts: {e}")
        finally:
            conn.close()

def update_contact(id, name, phone_number, email, adress):
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                UPDATE contacts
                SET name = %s, phone_number = %s, email = %s, adress = %s
                WHERE id = %s
            """, (name, phone_number, email, adress, id))
            conn.commit()
            cur.close()
            print(f"The contact with ID {id} has been updated!")
        except Exception as e:
            print(f"Error updating contact: {e}")
        finally:
            conn.close()

def delete_contact(id):
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM contacts WHERE id = %s", (id,))
            conn.commit()
            cur.close()
            print(f"The contact with ID {id} has been removed!")
        except Exception as e:
            print(f"Error deleting contact: {e}")
        finally:
            conn.close()

def main():
    while True:
        print("What do you want to do:")
        print("1. Create a contact")
        print("2. Show all contacts")
        print("3. Update a contact")
        print("4. Remove a contact")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            phone_number = input("Phone number: ")
            email = input("Email: ")
            adress = input("Address: ")
            create_contact(name, phone_number, email, adress)
        
        elif choice == "2":
            get_all_contacts()
        
        elif choice == "3":
            id = int(input("Enter the ID of the contact to update: "))
            name = input("New name: ")
            phone_number = input("New phone number: ")
            email = input("New email: ")
            adress = input("New address: ")
            update_contact(id, name, phone_number, email, adress)
        
        elif choice == "4":
            id = int(input("Enter the ID of the contact to remove: "))
            delete_contact(id)
        
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
