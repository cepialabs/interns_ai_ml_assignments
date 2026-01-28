import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

genres = df['listed_in'].dropna().str.split(', ')
all_genres = genres.explode()

top_genres = all_genres.value_counts().head(10)
print("Top 10 Genres:\n", top_genres)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

type_counts = df['type'].value_counts()
print("\nMovies vs TV Shows:\n", type_counts)

plt.figure()
type_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Movies vs TV Shows")
plt.ylabel("")
plt.show()

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

yearly_content = df['year_added'].value_counts().sort_index()
print("\nContent added per year:\n", yearly_content.tail())

plt.figure()
yearly_content.plot()
plt.title("Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

countries = df['country'].dropna().str.split(', ')
all_countries = countries.explode()

top_country = all_countries.value_counts().head(1)
print("\nTop Producing Country:\n", top_country)
