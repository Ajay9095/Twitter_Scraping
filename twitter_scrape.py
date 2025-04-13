import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta
import random



# MongoDB client connection
client = pymongo.MongoClient("mongodb+srv://ajaykumar:ajay9095@cluster-1.npktwbc.mongodb.net/")
twtdb = client.ajaykumar
twtdb_main = twtdb.twitterproj

# Main function
def main():
    st.set_page_config(page_title="Twitter Scraper", page_icon="🐦", layout="wide")
    st.title("🐦 Twitter Scraper & Analysis")

    menu = ["Home", "About", "Search", "Display", "Download"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the Twitter Scraper App! 🚀")
        st.markdown(
            """
            **Features:**  
            - 🔍 Scrape tweets based on hashtag/ keywords  
            - 📊 Store & display tweet data  
            - 📥 Download data as CSV & JSON  
            - 🛢️ Uses MongoDB for storage  
            """
        )

    elif choice == "About":
        st.subheader("📌 About This Project")
        with st.expander("🔍 Twitter Scraper"):
            st.write("This tool extracts public tweets based on hashtags and keywords.")
        with st.expander("💾 MongoDB Database"):
            st.write("MongoDB stores the scraped tweets efficiently.")
        with st.expander("🎨 Streamlit UI"):
            st.write("Streamlit provides an interactive and user-friendly interface.")

    elif choice == "Search":
        st.subheader("🔎 Search & Scrape Tweets")
        twtdb_main.delete_many({})

        with st.form(key='search_form'):
            query = st.text_input('Enter a hashtag or keyword')
            limit = st.number_input('Number of tweets (max 1000)', min_value=10, max_value=1000, step=10)
            start = st.date_input('Start date')
            end = st.date_input('End date')
            submit_button = st.form_submit_button(label="Scrape Tweets")
        
        if submit_button:
            if start >= end:
                st.error("⚠️ End date must be after the start date.")
                return

            st.success(f"Fetching {limit} tweets for `{query}`...")

            tweet_data = fetch_tweets(query, start, end, limit)
            twtdb_main.insert_many(tweet_data)

            df = pd.DataFrame(tweet_data)
            st.success(f"✅ Scraped {len(df)} tweets successfully.")
            st.dataframe(df)

    elif choice == "Display":
        st.subheader("📊 Display Scraped Tweets")
        df = pd.DataFrame(list(twtdb_main.find()))
        if df.empty:
            st.warning("No data found! Please scrape tweets first.")
        else:
            st.dataframe(df)

    elif choice == "Download":
        st.subheader("📥 Download Scraped Data")
        df = pd.DataFrame(list(twtdb_main.find()))

        if df.empty:
            st.warning("⚠️ No data to download! Please scrape tweets first.")
        else:
            col1, col2 = st.columns(2)

            with col1:
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("📂 Download CSV", data=csv, file_name="twitter_data.csv", mime="text/csv")
                st.success("✅ CSV file ready.")

            with col2:
                df = df.astype(str)
                js = df.to_json(orient="records", indent=4, force_ascii=False)
                st.download_button("📂 Download JSON", data=js, file_name="twitter_data.json", mime="application/json")
                st.success("✅ JSON file ready.")

main()

