from src.data_loader import load_data
from src.data_validation import validate_data
from src.model import train_model

data_path = "data/credit_risk_scoring_dataset.csv"

df = load_data(data_path)

if validate_data(df):
    train_model(df)