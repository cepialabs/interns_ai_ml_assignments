import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/spam_emails.csv")

X = df[["word_count", "special_char_count", "capital_letters"]]
y = df["spam"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Without Scaling
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)
print("WITHOUT Scaling Accuracy:", accuracy)

# With Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_scaled = LogisticRegression(max_iter=1000)
model_scaled.fit(X_train_scaled, y_train)
pred_scaled = model_scaled.predict(X_test_scaled)

accuracy_scaled = accuracy_score(y_test, pred_scaled)
print("WITH Scaling Accuracy:", accuracy_scaled)

# Save results
with open("outputs/classification_results.txt", "w") as f:
    f.write("WITHOUT Scaling Accuracy: " + str(accuracy) + "\n")
    f.write("WITH Scaling Accuracy: " + str(accuracy_scaled))
