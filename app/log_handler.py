import csv
import sys
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
ip = sys.argv[1]
ua = sys.argv[2]
endpoint = sys.argv[3]
params = sys.argv[4]

with open('logs/request_log.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([timestamp, ip, ua, endpoint, params])
