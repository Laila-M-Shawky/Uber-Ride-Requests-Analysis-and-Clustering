# ================================================================
# 2. Data Preprocessing (Handling Missing Data, Duplicates, Cleanup)
# ================================================================

import pandas as pd
from dateutil import parser

# ----------------------------------------------------------------
# Function to safely parse date strings
# ----------------------------------------------------------------
def smart_date_parser(date_str):
    """
    Attempts to parse a date string into a datetime object.
    Returns NaT if parsing fails.
    """
    try:
        return parser.parse(str(date_str), dayfirst=True)
    except:
        return pd.NaT

# ----------------------------------------------------------------
# Function to apply datetime parsing to both relevant columns
# ----------------------------------------------------------------
def parse_dates(df):
    """
    Applies smart_date_parser to the 'Request timestamp' and 'Drop timestamp' columns.
    """
    df['Request timestamp'] = df['Request timestamp'].apply(smart_date_parser)
    df['Drop timestamp'] = df['Drop timestamp'].apply(smart_date_parser)
    return df

# ----------------------------------------------------------------
# Main data cleaning function
# ----------------------------------------------------------------
def clean_data(df):
    """
    Cleans the Uber dataset:
    - Parses dates
    - Removes duplicates
    - Handles missing driver IDs
    - Cleans text values (strip + title-case)
    - Filters invalid IDs
    """
    print("🧹 Cleaning data...")

    # Apply date parsing
    df = parse_dates(df)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Handle missing Driver IDs
    df['Driver id'] = df['Driver id'].fillna(0)
    df['Driver id'] = df['Driver id'].astype('Int64')

    # Clean text fields
    df['Status'] = df['Status'].str.strip().str.title()
    df['Pickup point'] = df['Pickup point'].str.strip().str.title()

    # Remove rows with invalid IDs
    df = df[df['Request id'] > 0]
    df = df[df['Driver id'] >= 0]

    return df

# ----------------------------------------------------------------
# Optional: Run as standalone script for testing
# ----------------------------------------------------------------
if __name__ == "__main__":
    df_raw = pd.read_csv('data/Uber Request Data.csv', sep='\t')
    df_clean = clean_data(df_raw)
    print(df_clean.head())
