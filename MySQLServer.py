import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',    # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as err:
        # Handle MySQL-specific errors
        print(f"MySQL error: {err}")
    
    except Error as e:
        # Handle general connection errors
        print(f"Error: {e}")
    
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == '__main__':
    create_database()
