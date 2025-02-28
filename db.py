import psycopg2
from db_config import Config

def get_db_connection():
    connection = psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        port=Config.DB_PORT
    )
    return connection

def test_connection():
    try:
        # Get the connection
        connection = get_db_connection()

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a simple query to test the connection
        cursor.execute("SELECT 1")

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print("Connection successful!")
        else:
            print("Connection failed, no result from query.")

        # Close the cursor and the connection
        cursor.close()
        connection.close()

    except psycopg2.OperationalError as e:
        print(f"Error: Unable to connect to the database\n{e}")

if __name__ == "__main__":
    test_connection()