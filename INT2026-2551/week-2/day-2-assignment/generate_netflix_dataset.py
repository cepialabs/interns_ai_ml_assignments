import pandas as pd
import random

n = 1000

types = ["Movie", "TV Show"]
countries = ["United States", "India", "United Kingdom", "Canada", "Japan"]
genres = ["Drama", "Comedy", "Action", "Romance", "Documentary"]

data = {
    "show_id": [f"s{i}" for i in range(1, n + 1)],
    "type": [random.choice(types) for _ in range(n)],
    "title": [f"Title {i}" for i in range(1, n + 1)],
    "country": [random.choice(countries) for _ in range(n)],
    "date_added": pd.date_range(start="2015-01-01", periods=n, freq="D"),
    "listed_in": [random.choice(genres) for _ in range(n)]
}

df = pd.DataFrame(data)

df.to_csv("netflix_titles.csv", index=False)
print("✅ netflix_titles.csv generated successfully")
