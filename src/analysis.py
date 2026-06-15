import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import numpy as np
# Load datasets
donations = pd.read_csv("data/donations.csv")
volunteers = pd.read_csv("data/volunteers.csv")
social = pd.read_csv("data/social_media.csv")
campaigns = pd.read_csv("data/campaigns.csv")

# Basic Analysis
print("Total Donations:", donations["Amount"].sum())
print("Average Donation:", donations["Amount"].mean())

print("\nCampaign-wise Donations:")
campaign_totals = donations.groupby("Campaign")["Amount"].sum()
print(campaign_totals)

# ==========================
# DONOR SEGMENTATION
# ==========================

def donor_type(amount):
    if amount < 1000:
        return "Small Donor"
    elif amount < 5000:
        return "Medium Donor"
    else:
        return "Major Donor"

donations["Donor_Type"] = donations["Amount"].apply(donor_type)

print("\nDonor Segmentation:")
print(donations["Donor_Type"].value_counts())

donor_counts = donations["Donor_Type"].value_counts()

plt.figure(figsize=(8,5))
donor_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Donor Segmentation")
plt.ylabel("")
plt.savefig("screenshots/donor_segmentation.png")
plt.close()

# Create chart
plt.figure(figsize=(8,5))
campaign_totals.plot(kind="bar")
plt.title("Donations by Campaign")
plt.xlabel("Campaign")
plt.ylabel("Donation Amount")
plt.tight_layout()

# Save chart
plt.savefig("screenshots/donations_by_campaign.png")
plt.close()
print("\nVolunteer Hours by City:")
city_hours = volunteers.groupby("City")["Hours_Worked"].sum()
print(city_hours)

plt.figure(figsize=(8,5))
city_hours.plot(kind="bar")
plt.title("Volunteer Hours by City")
plt.ylabel("Hours Worked")
plt.tight_layout()
plt.savefig("screenshots/volunteer_hours.png")
plt.close()

# ==========================
# TOP VOLUNTEERS
# ==========================

volunteers["Performance_Score"] = (
    volunteers["Hours_Worked"] * 10
)

top_volunteers = volunteers.sort_values(
    by="Performance_Score",
    ascending=False
)

print("\nTop 10 Volunteers:")
print(top_volunteers.head(10))

top10 = top_volunteers.head(10)

plt.figure(figsize=(10,5))
plt.bar(
    top10["Volunteer_ID"],
    top10["Performance_Score"]
)

plt.title("Top 10 Volunteers")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("screenshots/top_volunteers.png")
plt.close()


print("\nSocial Media Data:")
print(social.head())

plt.figure(figsize=(10,5))
plt.plot(social["Month"], social["Instagram_Followers"])

plt.title("Instagram Follower Growth")
plt.xlabel("Month")
plt.ylabel("Followers")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/social_media_growth.png")
plt.close()
print("\nCampaign ROI Analysis")

campaigns["ROI"] = (
    campaigns["Donations_Raised"]
    - campaigns["Cost"]
)

print(campaigns)

best_campaign = campaigns.loc[
    campaigns["ROI"].idxmax()
]

print("\nBest Campaign:")
print(best_campaign)
plt.figure(figsize=(8,5))

plt.bar(
    campaigns["Campaign"],
    campaigns["ROI"]
)

plt.title("Campaign ROI")
plt.ylabel("ROI")

plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig("screenshots/campaign_roi.png")
plt.close()

# ==========================
# NGO IMPACT ANALYSIS
# ==========================

campaigns["Cost_Per_Beneficiary"] = (
    campaigns["Cost"]
    /
    campaigns["Beneficiaries"]
)

print("\nCost Per Beneficiary:")
print(
    campaigns[
        ["Campaign", "Cost_Per_Beneficiary"]
    ]
)

plt.figure(figsize=(8,5))

plt.bar(
    campaigns["Campaign"],
    campaigns["Cost_Per_Beneficiary"]
)

plt.title("Cost Per Beneficiary")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "screenshots/cost_per_beneficiary.png"
)

plt.close()


# Machine Learning Model Placeholder 
donations["Date"] = pd.to_datetime(
    donations["Date"]
)

donations["Month"] = (
    donations["Date"].dt.month
)

monthly = donations.groupby(
    "Month"
)["Amount"].sum().reset_index()

X = monthly[["Month"]]
y = monthly["Amount"]

# Linear Regression

model = LinearRegression()
model.fit(X, y)

# Random Forest

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X, y)

print("\nBoth ML Models Trained Successfully")

future_month = np.array([[13]])

prediction = model.predict(
    future_month
)

print("\nPredicted Donation For Next Month:")
print(prediction[0])

rf_prediction = rf_model.predict(
    future_month
)

print(
    "\nRandom Forest Prediction:"
)

print(
    rf_prediction[0]
)

plt.figure(figsize=(8,5))

plt.plot(
    monthly["Month"],
    monthly["Amount"],
    marker="o"
)

plt.title("Monthly Donation Trend")
plt.xlabel("Month")
plt.ylabel("Donation Amount")

plt.tight_layout()

plt.savefig(
    "screenshots/donation_prediction.png"
)

plt.close()

# Executive Summary Export

summary = pd.DataFrame({
    "Metric": [
        "Total Donations",
        "Average Donation",
        "Total Volunteers",
        "Total Campaigns"
    ],
    "Value": [
        donations["Amount"].sum(),
        donations["Amount"].mean(),
        volunteers["Volunteer_ID"].count(),
        campaigns["Campaign"].count()
    ]
})

summary.to_csv(
    "reports/executive_summary.csv",
    index=False
)

print("Executive Summary Saved")