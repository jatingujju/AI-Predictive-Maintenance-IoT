def preprocess_data(df):
    print("🔧 Preprocessing Data...")

    df = df.dropna()

    print("✅ Preprocessing Done")
    return df