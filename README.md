# 🐝 Honeypot Project

This project is a web-based honeypot designed to detect and log suspicious activities while analyzing patterns using machine learning. The project features real-time prediction, data visualization, and detailed logging to enhance security monitoring.  

---

## 🚀 Features  
1. **Honeypot Web Interface:** A decoy website to attract malicious activities.  
2. **Real-Time Monitoring:** Logs activity with IP addresses, usernames, and user agents.  
3. **Machine Learning Integration:** Predicts whether an action is malicious using a trained Random Forest model.  
4. **Data Visualization:** Analyzes and visualizes suspicious activity trends.  
5. **Log Management:** Stores detailed logs in CSV files for further analysis.  

---

## 🗃️ Project Structure  

```
.
├── app/                # Application scripts (log handling, monitoring)
├── images/             # Image assets used on the website
├── logs/               # Logs and CSV files for activity tracking
├── ml/                 # Machine learning scripts and models
├── php/                # PHP scripts for login, registration, and page handling
├── visualize/          # Scripts for visualizing data
├── db.php              # Database connection file
├── honeypot.py         # Honeypot main script
├── index.html          # Main web page
├── prediction.js       # Prediction handling script
├── style.css           # CSS for styling the honeypot pages
├── submit.php          # PHP script for handling form submissions
└── README.md           # Project documentation
```

---

## 🛠️ Setup Instructions  

### Prerequisites  
- Python 3.x  
- XAMPP (for Apache and MySQL)  
- Streamlit (for visualization)  
Run the following command to install all necessary dependencies:
  ```
  pip install -r requirements.txt
  ```

### Steps to Run  

1. **Clone the repository:**  
   ```
   git clone https://github.com/yourusername/HoneyPot.git
   cd HoneyPot
   ```

2. **Start XAMPP:**  
   - Run Apache and MySQL from the XAMPP Control Panel.  

3. **Database Setup:**  
   - Import the database using `db.php` or manually through phpMyAdmin.  

4. **Run the Honeypot Server:**  
   ```
   python honeypot.py
   ```
   - Visit `http://localhost/HoneyPot` in your browser.  

5. **Start the Machine Learning API:**  
   ```
   python ml/ml_api.py
   ```
   - The API will run on `http://127.0.0.1:5000/predict`.  

6. **Visualize Logs:**  
   ```
   streamlit run visualize/visualize_logs.py
   ```
   - Access the visualization dashboard at `http://localhost:8501`.  

---

## 📊 Usage  

- Access the honeypot web interface to attract and log suspicious activity.  
- Real-time predictions are logged automatically in the CSV file.  
- Visualize patterns and suspicious activity trends via Streamlit.  

---

## 💡 Troubleshooting  

- **API Connection Issues:** Ensure that the API server is running and accessible at `http://127.0.0.1:5000`.  
- **Log Not Generated:** Check file paths and directory permissions.  
- **Visualization Errors:** Verify that Streamlit is running properly.  

---

## 📝 Acknowledgments  

Special thanks to the open-source libraries and tools that made this project possible, including:  
- Flask for API creation  
- Scikit-learn for machine learning  
- Pandas for data processing  
- Streamlit for visualization  

---
