import pandas as pd

donations = pd.read_csv("data/donations.csv")

top_campaign = donations.groupby(
    "Campaign"
)["Amount"].sum().idxmax()

print("\nBusiness Insights")
print(
    f"Highest Revenue Campaign: {top_campaign}"
)