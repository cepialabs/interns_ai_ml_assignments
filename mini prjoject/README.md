# Spam Email Detection - Kaggle Style ML Mini Project

## Goal
Classify emails as Spam (1) or Not Spam (0) using text + engineered features.

## Dataset
Place `spam.csv` inside:
`data/raw/spam.csv`

Required columns:
- text
- label (0/1)

## Run
Install:
pip install -r requirements.txt

Train:
python -m src.train

Evaluate (charts in outputs/):
python -m src.evaluate