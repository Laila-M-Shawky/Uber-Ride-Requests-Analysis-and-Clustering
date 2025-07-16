# ================================================================
# 5. Clustering Module (K-Means on Simulated Location Data)
# ================================================================

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# ----------------------------------------------------------------
# Step 1: Add Random Coordinates to Simulate Location Data
# ----------------------------------------------------------------
def add_random_coordinates(df, seed=42):
    """
    Adds random Latitude and Longitude columns to the DataFrame
    to simulate pickup/drop locations.
    
    Parameters:
    - df: DataFrame
    - seed: int (random seed for reproducibility)

    Returns:
    - DataFrame with 'Latitude' and 'Longitude' columns
    """
    np.random.seed(seed)
    N = len(df)
    df['Latitude'] = np.random.uniform(-10, 10, size=N)
    df['Longitude'] = np.random.uniform(-20, 20, size=N)
    return df

# ----------------------------------------------------------------
# Step 2: Perform KMeans Clustering on the Coordinates
# ----------------------------------------------------------------
def perform_clustering(df, n_clusters=5):
    """
    Applies KMeans clustering on 'Latitude' and 'Longitude' columns
    and adds a 'cluster' label to each row.
    
    Parameters:
    - df: DataFrame with 'Latitude' and 'Longitude'
    - n_clusters: number of clusters (default is 5)

    Returns:
    - DataFrame with new column 'cluster' (integer labels)
    """
    X = df[['Longitude', 'Latitude']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)
    return df

# ----------------------------------------------------------------
# Optional: Run this module directly for testing
# ----------------------------------------------------------------
if __name__ == "__main__":
    df = pd.DataFrame({'Request id': range(100)})
    df = add_random_coordinates(df)
    df = perform_clustering(df)
    print(df[['Longitude', 'Latitude', 'cluster']].head())
