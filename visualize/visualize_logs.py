import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
def fetch_logs():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='honeypot_db'
        )
        query = "SELECT * FROM logs"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return None

# Fetch logs from the database
logs_df = fetch_logs()

if logs_df is not None and not logs_df.empty:
    # Convert timestamp to datetime format
    logs_df['timestamp'] = pd.to_datetime(logs_df['timestamp'])

    # Plot: Number of login attempts over time
    plt.figure(figsize=(10, 6))
    sns.countplot(data=logs_df, x='timestamp', color='blue')
    plt.title('Number of Login Attempts Over Time')
    plt.xticks(rotation=45)
    plt.show()

    # Plot: Frequency of specific usernames being used
    plt.figure(figsize=(8, 5))
    sns.countplot(data=logs_df, x='username', order=logs_df['username'].value_counts().index, palette='viridis', hue='username', dodge=False)
    plt.title('Frequency of Username Usage')
    plt.xticks(rotation=45)
    plt.show()

    # Plot: Number of comments submitted
    comments = logs_df[logs_df['activity'].str.contains('Comment submitted', na=False)]
    plt.figure(figsize=(8, 5))
    sns.countplot(data=comments, x='username', order=comments['username'].value_counts().index, palette='plasma', hue='username', dodge=False)
    plt.title('Number of Comments Submitted by User')
    plt.xticks(rotation=45)
    plt.show()

    # Plot: Successful vs. Unsuccessful Login Attempts
    logs_df['success'] = logs_df['activity'].str.contains('Successful login', na=False).astype(int)
    success_counts = logs_df['success'].value_counts()

    if len(success_counts) == 2:
        labels = ['Unsuccessful', 'Successful']
    elif len(success_counts) == 1:
        labels = ['Successful'] if success_counts.index[0] == 1 else ['Unsuccessful']
    else:
        labels = ['Unknown']

    plt.figure(figsize=(6, 6))
    plt.pie(success_counts, labels=labels, autopct='%1.1f%%', colors=['red', 'green'])
    plt.title('Successful vs. Unsuccessful Login Attempts')
    plt.show()

else:
    print("No logs available for visualization.")
