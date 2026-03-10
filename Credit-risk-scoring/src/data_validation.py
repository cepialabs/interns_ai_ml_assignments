def validate_data(df):
    if df.isnull().sum().sum() > 0:
        print("Dataset contains missing values")
        return False

    if "Default" not in df.columns:
        print("Target column 'Default' missing")
        return False

    print("Data validation successful")
    return True