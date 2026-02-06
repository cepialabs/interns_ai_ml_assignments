import os
import pandas as pd
import matplotlib.pyplot as plt

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# -----------------------------
# Chart 1: Score Distribution
# -----------------------------
plt.figure()
plt.hist(df["score"], bins=10)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Students")
plt.savefig("charts/01_score_distribution.png")
plt.close()

# -----------------------------
# Chart 2: Attendance vs Score
# -----------------------------
plt.figure()
plt.scatter(df["attendance"], df["score"])
plt.title("Attendance vs Score")
plt.xlabel("Attendance")
plt.ylabel("Score")
plt.savefig("charts/02_attendance_vs_score.png")
plt.close()

# -----------------------------
# Chart 3: Gender vs Score
# -----------------------------
plt.figure()
df.boxplot(column="score", by="gender")
plt.title("Gender vs Score")
plt.suptitle("")
plt.xlabel("Gender")
plt.ylabel("Score")
plt.savefig("charts/03_gender_vs_score.png")
plt.close()

# -----------------------------
# Chart 4: Average Score by Gender
# -----------------------------
avg_gender = df.groupby("gender")["score"].mean()
plt.figure()
avg_gender.plot(kind="bar")
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.savefig("charts/04_avg_score_gender.png")
plt.close()

# -----------------------------
# Chart 5: Correlation Heatmap
# -----------------------------
corr = df[["attendance","math_score","reading_score","writing_score","score"]].corr()
plt.figure()
plt.imshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.savefig("charts/05_correlation_heatmap.png")
plt.close()

# -----------------------------
# Chart 6: Subject Scores Comparison
# -----------------------------
plt.figure()
plt.plot(df["math_score"], label="Math")
plt.plot(df["reading_score"], label="Reading")
plt.plot(df["writing_score"], label="Writing")
plt.legend()
plt.title("Subject Score Comparison")
plt.xlabel("Student Index")
plt.ylabel("Score")
plt.savefig("charts/06_subject_scores.png")
plt.close()

# -----------------------------
# Chart 7: Attendance Distribution
# -----------------------------
plt.figure()
plt.hist(df["attendance"], bins=10)
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Students")
plt.savefig("charts/07_attendance_distribution.png")
plt.close()

print(" All charts generated successfully!")
