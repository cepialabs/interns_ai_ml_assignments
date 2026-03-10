from src.predict import predict_risk

# Give sample input based on your dataset columns
sample = [50000, 1, 200000, 2]

result = predict_risk(sample)

print("Prediction Result:", result)