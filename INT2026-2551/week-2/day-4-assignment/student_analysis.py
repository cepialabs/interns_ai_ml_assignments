import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_performance.csv")

print("Dataset loaded successfully")
print(df.head())

# Score Distribution Plot
plt.figure()
plt.hist(df["overall_score"], bins=20)
plt.xlabel("Overall Score")
plt.ylabel("Number of Students")
plt.title("Score Distribution")
plt.show()

# Gender vs Performance Chart
gender_perf = df.groupby("gender")["overall_score"].mean()

plt.figure()
gender_perf.plot(kind="bar")
plt.xlabel("Gender")
plt.ylabel("Average Overall Score")
plt.title("Gender vs Performance")
plt.show()

# Correlation Heatmap
plt.figure()
corr = df[
    ["study_hours", "attendance_percentage",
     "math_score", "science_score", "english_score",
     "overall_score"]
].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 4. Attendance vs Score Trend
plt.figure()
plt.scatter(df["attendance_percentage"], df["overall_score"])
plt.xlabel("Attendance Percentage")
plt.ylabel("Overall Score")
plt.title("Attendance vs Score Trend")
plt.show()