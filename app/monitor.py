import pymysql
import time

def monitor_logs():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='honeypot_db'
        )
        cursor = conn.cursor()

        while True:
            cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 5")
            logs = cursor.fetchall()

            for log in logs:
                print(f"[{log[4]}] {log[1]} attempted login with username '{log[2]}'")

            time.sleep(5)
            
    except Exception as e:
        print(f"Error monitoring logs: {e}")
    finally:
        conn.close()

monitor_logs()
