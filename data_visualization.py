# ================================================================
# 4. Data Visualization Module
# Create charts to explore patterns and extract insights
# ================================================================

import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# Distribution of Pickup Points
# ----------------------------------------------------------------
def plot_pickup_point_distribution(df):
    """
    Bar chart showing the count of pickup points (City vs Airport)
    """
    sns.countplot(x='Pickup point', data=df)
    plt.title('Distribution of Pickup Points')
    plt.xlabel('Pickup Point')
    plt.ylabel('Count')
    plt.show()

# ----------------------------------------------------------------
# Distribution of Trip Status
# ----------------------------------------------------------------
def plot_trip_status(df):
    """
    Bar chart showing the status of trips (Completed, Cancelled, etc.)
    """
    sns.countplot(x='Status', data=df)
    plt.title('Distribution of Trip Status')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.show()

# ----------------------------------------------------------------
# Trip Status broken down by Pickup Point
# ----------------------------------------------------------------
def plot_status_by_pickup_point(df):
    """
    Stacked bar chart: Status by Pickup Point
    """
    sns.countplot(x='Status', hue='Pickup point', data=df)
    plt.title('Trip Status by Pickup Point')
    plt.xlabel('Trip Status')
    plt.ylabel('Count')
    plt.show()

# ----------------------------------------------------------------
# Daily Request Count by Day of the Week
# ----------------------------------------------------------------
def plot_daily_requests(df):
    """
    Shows total number of requests for each day of the week
    """
    sns.countplot(x='Request day', data=df)
    plt.title('Number of Daily Requests by Day')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Requests')
    plt.show()

# ----------------------------------------------------------------
# Requests per Time Slot
# ----------------------------------------------------------------
def plot_time_slot_distribution(df):
    """
    Count of requests per time period (Morning, Afternoon, etc.)
    """
    sns.countplot(x='Time slot', data=df, palette='crest')
    plt.title('Requests per Time Slot')
    plt.xlabel('Time Slot')
    plt.ylabel('Number of Requests')
    plt.show()

# ----------------------------------------------------------------
# Requests per Hour
# ----------------------------------------------------------------
def plot_hourly_requests(df):
    """
    Count of requests by hour of the day
    """
    sns.countplot(x='Request hour', data=df, palette='crest')
    plt.title('Requests per Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Requests')
    plt.show()

# ----------------------------------------------------------------
# Heatmap of Requests by Hour and Day
# ----------------------------------------------------------------
def plot_request_heatmap(df):
    """
    Heatmap showing request density by hour and weekday
    """
    pivot_table = df.pivot_table(values='Request id', index='Request hour', columns='Request day', aggfunc='count')
    sns.heatmap(pivot_table, cmap='Spectral')
    plt.title('Requests by Hour and Day')
    plt.xlabel('Day of the Week')
    plt.ylabel('Hour of the Day')
    plt.show()

# ----------------------------------------------------------------
# Trip Duration Distribution per Hour (Boxplot)
# ----------------------------------------------------------------
def plot_trip_duration_boxplot(df):
    """
    Boxplot showing the variation of trip duration over different hours
    """
    df_filtered = df[df['Trip Duration Mins'] > 0]
    sns.boxplot(x='Request hour', y='Trip Duration Mins', data=df_filtered, palette='rainbow')
    plt.title('Trip Duration Distribution by Request Hour')
    plt.xlabel('Request Hour')
    plt.ylabel('Trip Duration (mins)')
    plt.ylim(0, 100)
    plt.show()

# ----------------------------------------------------------------
# Trip Duration vs. Request Hour (Scatter plot)
# ----------------------------------------------------------------
def plot_trip_duration_scatter(df):
    """
    Scatter plot showing trip duration across request hours
    """
    # Remove outliers before plotting
    df_filtered = df[(df['Trip Duration Mins'] <= 180) & (df['Trip Duration Mins'] > 0)]

    # Scatter plot
    sns.scatterplot(x='Request hour', y='Trip Duration Mins', data=df_filtered)
    plt.xlabel('Request Hour')
    plt.ylabel('Trip Duration (mins)')
    plt.title('Trip Duration vs. Request Hour')
    plt.show()


# ----------------------------------------------------------------
# Top 10 Drivers with Most Trips
# ----------------------------------------------------------------
def plot_top_drivers(df):
    """
    Bar chart showing top 10 drivers by number of trips
    """
    top_drivers = df[df['Driver id'] > 0].groupby('Driver id').size().sort_values(ascending=False).head(10)
    sns.barplot(x=top_drivers.index.astype(str), y=top_drivers.values, palette='viridis')
    plt.title('Top 10 Drivers by Number of Trips')
    plt.xlabel('Driver ID')
    plt.ylabel('Number of Trips')
    plt.xticks(rotation=45)
    plt.show()

# ----------------------------------------------------------------
# Driver Availability by Day of Week
# ----------------------------------------------------------------
def plot_driver_availability_by_day(df):
    """
    Stacked bar showing driver availability broken down by day
    """
    sns.countplot(x='Driver Available', hue='Request day', data=df, palette='rainbow')
    plt.title('Driver Availability by Day of Week')
    plt.xlabel('Driver Available?')
    plt.ylabel('Number of Requests')
    plt.show()

# ----------------------------------------------------------------
# Driver Availability by Time Slot
# ----------------------------------------------------------------
def plot_driver_availability_by_slot(df):
    """
    Stacked bar showing driver availability by time of day
    """
    sns.countplot(x='Driver Available', hue='Time slot', data=df, palette='crest')
    plt.title('Driver Availability by Time Slot')
    plt.xlabel('Driver Available?')
    plt.ylabel('Number of Requests')
    plt.show()

# ----------------------------------------------------------------
# Number of Requests Per Day of the Week
# ----------------------------------------------------------------
def plot_requests_per_weekday(df):
    """
    Bar chart showing number of ride requests per day of the week.
    """
    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    sns.countplot(x='Request day', data=df, order=order)
    plt.title('Amount of Daily Requests per Week')
    plt.xlabel('Week Day')
    plt.ylabel('Total Requests')
    plt.show()

# ----------------------------------------------------------------
# KMeans Clustering Plot (after clustering is done externally)
# ----------------------------------------------------------------
def plot_location_clusters(df):
    """
    Visualizes clusters of locations using KMeans result
    """
    sns.scatterplot(x='Longitude', y='Latitude', hue='cluster', data=df, palette='viridis', s=15)
    plt.title('K-Means Clustering of Pickup Locations')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()
