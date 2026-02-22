import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/house_prices.csv")

X = df[["square_feet", "bedrooms", "age"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Without Scaling
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)

mse = mean_squared_error(y_test, pred)
r2 = r2_score(y_test, pred)

print("WITHOUT Scaling")
print("MSE:", mse)
print("R2:", r2)

# With Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)
pred_scaled = model_scaled.predict(X_test_scaled)

mse_scaled = mean_squared_error(y_test, pred_scaled)
r2_scaled = r2_score(y_test, pred_scaled)

print("\nWITH Scaling")
print("MSE:", mse_scaled)
print("R2:", r2_scaled)

# Save results
with open("outputs/regression_results.txt", "w") as f:
    f.write("WITHOUT Scaling\n")
    f.write(f"MSE: {mse}\nR2: {r2}\n\n")
    f.write("WITH Scaling\n")
    f.write(f"MSE: {mse_scaled}\nR2: {r2_scaled}\n")
