# ================================================================
# 1. Data Loading and Basic Exploration
# ================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path='data/Uber Request Data.csv'):
    """
    Loads the Uber dataset and displays initial exploration + visualizations.
    
    Parameters:
    - path (str): Path to the CSV file.

    Returns:
    - df (DataFrame): Loaded dataset.
    """
    print("📥 Loading dataset...")
    df = pd.read_csv(path, sep='\t')

    # ----------------------------
    # Basic Data Preview
    # ----------------------------
    print("\n🔍 First 5 rows:")
    print(df.head())
    print("\n🔍 Last 5 rows:")
    print(df.tail())
    print(f"\n📐 Shape: {df.shape}")
    print("\n🧠 Info:")
    df.info()
    print("\n📊 Numeric Description:")
    print(df.describe())
    print("\n📊 Full Description (including categorical):")
    print(df.describe(include='all'))

    # ----------------------------
    # Missing and Unique Values
    # ----------------------------
    print("\n❗ Missing values per column:")
    print(df.isnull().sum())
    print("\n🔢 Unique values per column:")
    print(df.nunique())

    # ----------------------------
    # Always Show Initial Visualizations
    # ----------------------------

    # 1. Pickup point distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Pickup point', data=df)
    plt.title('Distribution of Pickup Points')
    plt.xlabel('Pickup Point')
    plt.ylabel('Count')
    plt.show()

    # 2. Trip status distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Status', data=df)
    plt.title('Distribution of Trip Status')
    plt.xlabel('Trip Status')
    plt.ylabel('Count')
    plt.show()

    # 3. Status broken down by pickup point
    plt.figure(figsize=(8, 5))
    sns.countplot(x="Status", hue="Pickup point", data=df)
    plt.title("Trip Status by Pickup Point")
    plt.xlabel("Trip Status")
    plt.ylabel("Count")
    plt.show()

    return df

# Optional test run
if __name__ == "__main__":
    df = load_data()
