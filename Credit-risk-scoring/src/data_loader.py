import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip().str.replace(" ", "_")

        print("Data Loaded Successfully")
        return df

    except Exception as e:
        print("Error loading data:", e)