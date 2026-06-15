import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "nayepankh.db"
)

# Query 1
query1 = """
SELECT Campaign,
SUM(Amount) AS Total_Donation
FROM donations
GROUP BY Campaign
ORDER BY Total_Donation DESC
"""

result1 = pd.read_sql(
    query1,
    conn
)

print("\nTop Campaigns")
print(result1)

# Query 2
query2 = """
SELECT City,
SUM(Hours_Worked) AS Total_Hours
FROM volunteers
GROUP BY City
ORDER BY Total_Hours DESC
"""

result2 = pd.read_sql(
    query2,
    conn
)

print("\nVolunteer Hours By City")
print(result2)

conn.close()