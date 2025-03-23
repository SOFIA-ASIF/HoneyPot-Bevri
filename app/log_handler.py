import pymysql
from datetime import datetime
import sys

def log_activity(ip_address, username, password, user_agent, activity):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='honeypot_db'
        )
        cursor = conn.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            ip_address VARCHAR(50),
            username VARCHAR(50),
            password VARCHAR(255),
            user_agent TEXT,
            activity TEXT
        );
        """
        cursor.execute(create_table_query)
        
        # Log for debugging
        print(f"Logging activity: {activity} from {ip_address} with user {username}")

        # Insert log into the table
        query = """INSERT INTO logs (timestamp, ip_address, username, password, user_agent, activity) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (timestamp, ip_address, username, password, user_agent, activity))
        conn.commit()
        
        # Log success message
        print(f"Successfully logged: {activity} from {ip_address}")

    except Exception as e:
        print(f"Error logging activity: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 6:
        ip_address, username, password, user_agent, activity = sys.argv[1:]
        log_activity(ip_address, username, password, user_agent, activity)
    else:
        print("Usage: python log_handler.py <ip_address> <username> <password> <user_agent> <activity>")
