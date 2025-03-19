import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('logs/request_log.csv', names=['timestamp', 'ip', 'user_agent', 'endpoint', 'params'])
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Requests per hour
df['hour'] = df['timestamp'].dt.hour
plt.figure(figsize=(10,5))
sns.countplot(x='hour', data=df)
plt.title('Requests per Hour')
plt.show()

# Top endpoints
plt.figure(figsize=(10,5))
sns.countplot(y='endpoint', data=df, order=df['endpoint'].value_counts().index)
plt.title('Top Endpoints Accessed')
plt.show()
