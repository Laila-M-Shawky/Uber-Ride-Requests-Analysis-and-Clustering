# ================================================================
# 6. Save the cleaned and feature-engineered dataset
# ================================================================

def save_data(df, path='output/Uber with features.csv'):
    print("💾 Saving transformed data to", path)
    df.to_csv(path, index=False)

# Optional test
if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("data/Uber Request Data.csv", sep="\t")
    df.to_csv("output/test_saved_data.csv", index=False)
    print("✅ Test save complete.")
