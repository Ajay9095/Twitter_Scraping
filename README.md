---

# 🐦 Twitter Scraper & Analysis App

This is a Streamlit-based web application that allows you to **search**, **scrape**, **analyze**, and **download** tweet data using hashtags or keywords. The app uses **MongoDB** as a backend database to store tweets and supports exporting data in both **CSV** and **JSON** formats.

---

## 🚀 Features

- 🔍 Scrape tweets based on **hashtags** or **keywords**
- 💾 Store and retrieve tweets using **MongoDB**
- 📊 View scraped tweets in an interactive table
- 📥 Download tweets in **CSV** or **JSON** formats
- 🎨 Built with an intuitive **Streamlit** UI

---

## 📦 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Database**: MongoDB (via [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))  
- **Libraries**: `pandas`, `streamlit`, `pymongo`, `datetime`, `random`

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/twitter-scraper-app.git
cd twitter-scraper-app
```

### 2. Install Dependencies

Make sure you have Python 3.8 or higher.

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
```bash
pip install streamlit pymongo pandas
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
📦twitter-scraper-app
├── app.py                # Main Streamlit application
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
```

---

## 🔒 MongoDB Setup

- Replace the following line in `app.py` with your MongoDB Atlas URI:
```python
client = pymongo.MongoClient("your-mongodb-uri-here")
```

- Make sure the database and collection names are correct:
```python
twtdb = client.ajaykumar
twtdb_main = twtdb.twitterproj
```

---

## 🙋‍♂️ Author

**Ajay Kumar**  
_Developer & AI Enthusiast_

---

## 📄 License

This project is open-source and free to use for non-commercial purposes.

---
