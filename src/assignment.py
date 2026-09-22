# Coffee Cart Sales Analysis

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from urllib.error import URLError


DATA_URL = "https://raw.githubusercontent.com/niraj-northeastern/ds5110-hw1/refs/heads/main/data/raw/coffee_sales.csv"
LOCAL_RAW = Path(__file__).resolve().parents[1] / "data" / "raw" / "coffee_sales.csv"
OUT = Path(__file__).resolve().parents[1] / "output"
OUT.mkdir(exist_ok=True)

#try-except block to handle url failure
try:
    df = pd.read_csv(DATA_URL)
    print("Data from Github URL")
except (URLError, OSError) as e:
    print("Data from Local path")
    df = pd.read_csv(LOCAL_RAW)

df["revenue"] = df["quantity"] * df["unit_price"]

# Daily revenue
daily = df.groupby("date")["revenue"].sum()
avg_daily = daily.mean()


# Average Daily Revenue
print(f"Average daily revenue: ${avg_daily:.2f}")

# Compare revenue: random 50/50 split of the days(Original Header) - (Actual - random 50/50 split of the rows)
shuffled = df.sample(frac=1, random_state=42)
half = len(shuffled) // 2
group_a = shuffled.iloc[:half]
group_b = shuffled.iloc[half:]
print(f"Group A mean revenue: {group_a['revenue'].mean():.2f}")
print(f"Group B mean revenue: {group_b['revenue'].mean():.2f}")

# Compare revenue: random 50/50 split of the days
shuffled = daily.sample(frac=1, random_state=42)
half = len(shuffled) // 2
group_aa = shuffled.iloc[:half]
group_bb = shuffled.iloc[half:]
print(f"Group A mean daily revenue: {group_aa.mean():.2f}")
print(f"Group B mean daily revenue: {group_bb.mean():.2f}")

# Revenue by product
by_product = df.groupby("product")["revenue"].sum()
by_product.plot(kind="bar")
plt.ylabel("Total revenue ($)")
plt.title("Revenue by product")
plt.savefig(OUT / "revenue_by_product.png")
plt.close()


# Takeaway
# Drip coffee brings in the lowest total revenue this month. Latte brings in the highest total revenue this month


