import pandas as pd
import re

# Path to the log CSV file
log_file_path = "C:\\xampp\\htdocs\\HoneyPot\\logs\\request_log.csv"
def load_data(file_path):
    """Load the log data from a CSV file."""
    try:
        df = pd.read_csv(file_path, header=None, names=["timestamp", "ip", "username", "password", "user_agent", "activity"])
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean and preprocess the log data."""
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # Remove leading and trailing whitespace from text columns
    for col in ["ip", "username", "user_agent", "activity"]:
        df[col] = df[col].str.strip()

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    print("Data cleaned successfully!")
    return df

def parse_ip(ip_address):
    """Validate and clean IP address."""
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    return ip_address if re.match(pattern, ip_address) else "Invalid IP"

def transform_data(df):
    """Transform data into a structured format."""
    # Validate IP addresses
    df["ip"] = df["ip"].apply(parse_ip)

    # Encode activities using label encoding
    df["activity_code"] = df["activity"].astype("category").cat.codes

    print("Data transformed successfully!")
    return df

def save_cleaned_data(df, output_path= "C:\\xampp\\htdocs\\HoneyPot\\logs\\cleaned_request_log.csv"):
    """Save the cleaned and preprocessed data."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print(f"Error saving cleaned data: {e}")

def preprocess_logs():
    """Full pipeline to preprocess logs."""
    data = load_data(log_file_path)
    if data is not None:
        cleaned_data = clean_data(data)
        transformed_data = transform_data(cleaned_data)
        save_cleaned_data(transformed_data)

if __name__ == "__main__":
    preprocess_logs()
