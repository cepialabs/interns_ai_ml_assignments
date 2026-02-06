import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("email_marketing.csv")

p_click = df["clicked"].mean()

clicked_users = df[df["clicked"] == 1]
p_convert_given_click = clicked_users["converted"].mean()

table = pd.crosstab(df["clicked"], df["converted"], normalize="index")

print("Probability user clicks email:", round(p_click, 3))
print("Probability user converts given click:", round(p_convert_given_click, 3))
print("\nConditional Probability Table (P(Convert | Click))")
print(table)

table.plot(kind="bar", stacked=True)
plt.xlabel("Clicked")
plt.ylabel("Probability")
plt.title("Conditional Probability of Conversion Given Click")
plt.tight_layout()
plt.show()
