# Import all necessary functions from the src package (enabled by __init__.py)
from src import (
    load_data,
    clean_data,
    engineer_features,
    add_random_coordinates,
    perform_clustering,
    save_data,
    plot_time_slot_distribution,
    plot_hourly_requests,
    plot_request_heatmap,
    plot_trip_duration_boxplot,
    plot_trip_duration_scatter,
    plot_top_drivers,
    plot_driver_availability_by_day,
    plot_driver_availability_by_slot,
    plot_requests_per_weekday,
    plot_location_clusters
)

def main():
    # Step 1: Load the raw Uber request dataset
    df = load_data('data/Uber Request Data.csv')

    # Step 2: Clean the dataset (parse dates, remove duplicates, fix missing and invalid values)
    df = clean_data(df)

    # Step 3: Add time-based and derived features (hour, weekday, time slot, duration, etc.)
    df = engineer_features(df)
    print("✅ Done cleaning and feature engineering!")

    # (Optional) Check how requests are distributed by weekday
    print("\n🗓️ Request count per weekday:")
    print(df['Request day'].value_counts())

    # Step 4: Simulate GPS coordinates and perform clustering using KMeans
    df = add_random_coordinates(df)
    df = perform_clustering(df, n_clusters=5)

    # Step 5: Save the cleaned and enriched dataset to a new CSV file
    save_data(df, 'output/Uber with features.csv')

    # Step 6: Generate all key visualizations for analysis
    print("\n📊 Generating visualizations...\n")
    plot_time_slot_distribution(df)
    plot_hourly_requests(df)
    plot_request_heatmap(df)
    plot_trip_duration_boxplot(df)
    plot_trip_duration_scatter(df)
    plot_top_drivers(df)
    plot_driver_availability_by_day(df)
    plot_driver_availability_by_slot(df)
    plot_requests_per_weekday(df)
    plot_location_clusters(df)

# Run the main pipeline if this file is executed directly
if __name__ == "__main__":
    main()
