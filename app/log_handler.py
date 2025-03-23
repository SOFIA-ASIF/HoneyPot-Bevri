import csv
from datetime import datetime
import sys
import os

# Path to your CSV log file
CSV_LOG_FILE = "../logs/request_log.csv"

def log_activity(ip_address, username, password, user_agent, activity):
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(CSV_LOG_FILE), exist_ok=True)

        # Prepare the log entry
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = [timestamp, ip_address, username, password, user_agent, activity]

        # Check if file exists to write header
        file_exists = os.path.isfile(CSV_LOG_FILE)

        # Write to CSV
        with open(CSV_LOG_FILE, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            if not file_exists:
                writer.writerow(['timestamp', 'ip_address', 'username', 'password', 'user_agent', 'activity'])  # Header
            writer.writerow(log_entry)

        print(f"Successfully logged: {activity} from {ip_address}")

    except Exception as e:
        print(f"Error logging activity: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 6:
        ip_address, username, password, user_agent, activity = sys.argv[1:]
        log_activity(ip_address, username, password, user_agent, activity)
    else:
        print("Usage: python log_handler.py <ip_address> <username> <password> <user_agent> <activity>")
