# ================================================================
# 3. Feature Engineering Module
# Extracting time-based and derived features from timestamps
# ================================================================

import pandas as pd

# ----------------------------------------------------------------
# Helper function to classify hour into time period
# ----------------------------------------------------------------
def get_time_period(hour):
    """
    Converts an hour (int) into a part of day:
    Morning, Afternoon, Evening, or Night.
    """
    if pd.isna(hour):
        return None
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# ----------------------------------------------------------------
# Main feature engineering function
# ----------------------------------------------------------------
def engineer_features(df):
    """
    Adds new features to the dataframe:
    - Request hour, Request day (weekday)
    - Time slot (Morning, Evening...)
    - Trip duration (text + numeric in minutes)
    - Driver availability, Trip completion, Request date
    """
    print("🧠 Feature engineering...")

    # Extract hour and day from the request timestamp
    df = df[df['Request timestamp'].notna()]
    df['Request hour'] = df['Request timestamp'].dt.hour         
    df['Request day'] = df['Request timestamp'].dt.dayofweek 
    df['Request hour'] = df['Request hour'].astype('Int64')
    df['Request day'] = df['Request day'].astype('Int64')

    # Map numeric day to weekday name
    weekday_map = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
        3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }
    df['Request day'] = df['Request day'].map(weekday_map)

    # Assign time slot (e.g. Morning, Afternoon)
    df['Time slot'] = df['Request hour'].apply(get_time_period)
    df['Time slot'] = df['Time slot'].astype('category')
    
    # Display the Extracted Time Features
    cols_to_show = ['Request timestamp', 'Request hour', 'Request day',  
                    'Time slot']
    existing_cols = [col for col in cols_to_show if col in df.columns]
    print(df[existing_cols].head())

    # Calculate trip duration as timedelta
    df['Trip duration'] = df['Drop timestamp'] - df['Request timestamp']
    
    # Convert timedelta to string just for readability
    df['Trip duration'] = df['Trip duration'].apply(
        lambda x: str(x).replace("0 days ", "") if pd.notna(x) else "00:00:00"
    )
    
    # Binary features
    df['Is Completed'] = df['Status'] == 'Trip Completed'
    df['Driver Available'] = df['Driver id'].apply(lambda x: True if pd.notna(x) and x > 0 else False)

    # Extract just the date
    df['Request Date'] = df['Request timestamp'].dt.date
    
    # Calculate duration in minutes from timedelta
    df['Trip Duration Mins'] = df['Trip duration'].apply(
    lambda x: round(pd.Timedelta(x).total_seconds() / 60, 1) if pd.notna(x) else 0
    )

    return df

# ----------------------------------------------------------------
# Optional test block for standalone use
# ----------------------------------------------------------------
if __name__ == "__main__":
    df = pd.read_csv("data/Uber Request Data.csv", sep="\t")

    from src.data_cleaning_and_preprocessing import clean_data
    df = clean_data(df)

    df = engineer_features(df)
    print(df[['Request timestamp', 'Drop timestamp', 'Trip duration', 'Trip Duration Mins']].head())