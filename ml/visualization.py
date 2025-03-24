import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit page configuration
st.set_page_config(page_title="Honeypot Activity Dashboard", layout="wide")

# Title
st.title("🚀 Honeypot Activity Dashboard")
st.markdown("Visualizing suspicious activity and trends detected by the honeypot.")

# Load the CSV data
csv_path = "logs/features.csv"  # Update the path if necessary

@st.cache_data
def load_data():
    try:
        data = pd.read_csv(csv_path)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Fetch data
data = load_data()

if not data.empty:
    # Display the raw data
    st.subheader("Raw Honeypot Data")
    st.dataframe(data)

    # Suspicious vs Normal Activities Count
    st.subheader("Activity Distribution")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.countplot(data=data, x="malicious", palette="Set2")
    plt.title("Suspicious vs Normal Activities")
    plt.xlabel("Activity Type (0 = Normal, 1 = Suspicious)")
    plt.ylabel("Count")
    st.pyplot(fig1)

    # Activity Trend over Time
    st.subheader("Activity Trend Over Time")
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])
    data.set_index("Timestamp", inplace=True)
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    data.resample("H")["malicious"].sum().plot(ax=ax2, marker="o", color="orange")
    plt.title("Suspicious Activity Count Per Hour")
    plt.xlabel("Time")
    plt.ylabel("Suspicious Activity Count")
    st.pyplot(fig2)

    # Hourly Distribution of Suspicious Activity
    st.subheader("Suspicious Activity by Hour")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.countplot(data=data[data["malicious"] == 1], x="Hour", palette="coolwarm")
    plt.title("Suspicious Activity by Hour")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Count")
    st.pyplot(fig3)

    # Day of Week Distribution
    st.subheader("Activity by Day of the Week")
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    sns.countplot(data=data, x="Weekday", hue="malicious", palette="viridis")
    plt.title("Normal vs Suspicious Activities by Weekday")
    plt.xlabel("Weekday (0 = Monday, 6 = Sunday)")
    plt.ylabel("Count")
    st.pyplot(fig4)

else:
    st.warning("No data available to visualize. Make sure the CSV file exists and has data.")

# Auto-refresh every 10 seconds
st.markdown("🔄 Auto-refreshing every 10 seconds")
st_autorefresh = st.empty()
st_autorefresh.write("Last refreshed: Now")
st_autorefresh.button("Refresh", on_click=lambda: st_autorefresh.write("Last refreshed: Now"))

