#SQL Functions

import mysql.connector
from mysql.connector import Error


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='snowboardDB',
            user='root',
            password=''
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def insert_spec_to_db(name, brand, bend, flex, shape):
    connection = get_db_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return None  # Return None if connection fails

    try:
        cursor = connection.cursor()

        sql_insert_query = """
        INSERT INTO snowboard (Name, Brand, Bend, Flex, Shape)
        VALUES (%s, %s, %s, %s, %s)
        """

        record = (name, brand, bend, flex, shape)

        cursor.execute(sql_insert_query, record)
        connection.commit()

        # Retrieve the auto-incremented ID of the inserted row
        snowboard_id = cursor.lastrowid

        print("Record inserted successfully into snowboard table")
        return snowboard_id  # Return the snowboardID

    except Error as error:
        print(f"Failed to insert record into MySQL table: {error}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insert_length_data(snowboard_id, length, price, url):
    try:
        connection = get_db_connection()
        if connection.is_connected():
            cursor = connection.cursor()

            sql_insert_query = """
            INSERT INTO length (SnowboardID, Length, Price, URL)
            VALUES (%s, %s, %s, %s)
            """

            record = (snowboard_id, length, price, url)
            cursor.execute(sql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into length table")

    except mysql.connector.Error as error:
        print(f"Failed to insert record into MySQL table: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
