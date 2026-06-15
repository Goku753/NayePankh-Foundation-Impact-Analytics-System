import sqlite3
import pandas as pd

# Connect Database
conn = sqlite3.connect("nayepankh.db")

# Load CSV
donations = pd.read_csv("data/donations.csv")
volunteers = pd.read_csv("data/volunteers.csv")
campaigns = pd.read_csv("data/campaigns.csv")
social = pd.read_csv("data/social_media.csv")

# Store tables
donations.to_sql(
    "donations",
    conn,
    if_exists="replace",
    index=False
)

volunteers.to_sql(
    "volunteers",
    conn,
    if_exists="replace",
    index=False
)

campaigns.to_sql(
    "campaigns",
    conn,
    if_exists="replace",
    index=False
)

social.to_sql(
    "social_media",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")

conn.close()