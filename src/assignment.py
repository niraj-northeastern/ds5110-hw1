# %% [markdown]
# # Coffee Cart Sales Analysis

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("/Users/shruti.patil/Desktop/DS5110/HW1/data/raw/coffee_sales.csv")
df.head()

# %%
df["revenue"] = df["quantity"] * df["unit_price"]
df.head()

# %% [markdown]
# ### Daily revenue

# %%
daily = df.groupby("date")["revenue"].sum()
avg_daily = daily.mean()
daily


# %% [markdown]
# ### Average Daily Revenue

# %%

print(f"Average daily revenue: ${avg_daily:.2f}")

# %% [markdown]
# ### Compare revenue: random 50/50 split of the days

# %%
shuffled = df.sample(frac=1, random_state=42)
half = len(shuffled) // 2
group_a = shuffled.iloc[:half]
group_b = shuffled.iloc[half:]
print(f"Group A mean revenue: {group_a['revenue'].mean():.2f}")
print(f"Group B mean revenue: {group_b['revenue'].mean():.2f}")

# %%
shuffled = daily.sample(frac=1, random_state=42)
half = len(shuffled) // 2
group_aa = shuffled.iloc[:half]
group_bb = shuffled.iloc[half:]
print(f"Group A mean daily revenue: {group_aa.mean():.2f}")
print(f"Group B mean daily revenue: {group_bb.mean():.2f}")

# %% [markdown]
# ### Revenue by product

# %%
by_product = df.groupby("product")["revenue"].sum()
by_product.plot(kind="bar")
plt.ylabel("Total revenue ($)")
plt.title("Revenue by product")
plt.savefig("/Users/shruti.patil/desktop/DS5110/HW1/output/revenue_by_product.png")
plt.show()

# %% [markdown]
# ### Takeaway
# Drip coffee brings in the most total revenue this month.


