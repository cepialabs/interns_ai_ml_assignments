import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("spam_emails_knn_tree.csv")

X = df.drop(columns=["email_id", "spam"])
y = df["spam"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions)

print("Decision Tree Accuracy:", round(accuracy, 3))
print("Confusion Matrix:")
print(matrix)
