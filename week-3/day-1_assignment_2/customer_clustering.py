import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("customer_segmentation.csv")

df.columns = [c.strip() for c in df.columns]

id_col = df.columns[0]

required = ["annual_spend", "visit_frequency", "avg_basket_size"]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError("Missing columns: " + ", ".join(missing))

X = df[required]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(X_scaled)

plt.scatter(df["annual_spend"], df["visit_frequency"], c=df["cluster"])
plt.xlabel("Annual Spend")
plt.ylabel("Visit Frequency")
plt.title("Customer Segmentation Using K-Means")
plt.tight_layout()
plt.show()

print(df[[id_col, "cluster"]])
