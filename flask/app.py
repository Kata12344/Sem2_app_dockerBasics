from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv('MYSQL_HOST', 'localhost')
DB_USER = os.getenv('MYSQL_USER', 'user')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
DB_NAME = os.getenv('MYSQL_DATABASE', 'testdb')

@app.route('/')
def index():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cats")  # <-- Change to your table name

        rows = cursor.fetchall()
        return jsonify(rows)

    except mysql.connector.Error as err:
        return jsonify({"error": f"MySQL Error: {str(err)}"}), 500

    except Exception as e:
        # Handle general exceptions
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

    finally:
        # Always close cursor and connection if they were opened
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)