import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")


def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

def execute_query(query: str):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()  

def initialize_db():
    query = """
    CREATE TABLE IF NOT EXISTS patients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        address VARCHAR(255),
        phone VARCHAR(255),
        image LONGBLOB NOT NULL
    )
    """
    execute_query(query)


def create_patient(name: str, email: str, address: str, phone: str):
    query = f"""
    INSERT INTO patients (name, email, address, phone, image)
    VALUES ('{name}', '{email}', '{address}', '{phone}', 0);
    """
    execute_query(query)
