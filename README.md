# 🚕 Uber Ride Requests Analysis and Clustering

![Demo](Uber%20GIF%20by%20Mashable.gif)

- This project analyzes Uber ride request data to uncover demand patterns and driver behavior using Python.
- It includes cleaning, feature engineering, visualizations, and clustering of pickup locations with K-Means.

---

## 📌 Description

A comprehensive end-to-end data science project analyzing real-world Uber ride request data using Python.

---

### 🔄 Project Workflow:

- **Data Cleaning:**
  - Parsed and standardized datetime columns (`Request timestamp`, `Drop timestamp`).
  - Handled missing values in `Driver id` and `Drop timestamp` without dropping large portions of data.
  - Cleaned categorical fields like `Status` and `Pickup point` (e.g., stripping whitespace, title casing).

- **Feature Engineering:**
  - Extracted informative time-based features:
    - `Request hour`, `Request day`, and `Request Date`
    - `Trip duration` (as timedelta and in minutes)
    - `Time slot` classification (Morning, Afternoon, Evening, Night)
    - Boolean flags like `Driver Available` and `Is Completed`

- **Data Visualization:**
  - Identified:
    - Demand peaks (morning and evening)
    - Driver inactivity periods
    - Request trends by hour, day, and location
    - Cancellation patterns and completion rates

- **Clustering with K-Means (k=5):**
  - Simulated pickup coordinates and applied clustering to segment NYC into 5 operational zones.
  - Visualized high-density clusters vs. low-demand zones.

---

### 💡 Key Insights:

-  **Peak Demand:** Evening hours (5–9 PM) have highest request volume but lowest driver availability.
-  **Driver Inactivity:** Fridays show high inactivity despite high demand.
-  **Trip Duration:** Early morning trips (12–4 AM) are slightly longer.
-  **Top Drivers:** Most top-10 drivers completed between 20–22 trips — tight distribution.
-  **Pickup Patterns:** Majority of requests originate from the **City**; **Airport** has high rate of "No Cars Available".

---

### 🛠️ Recommendations:

-  Incentivize drivers during evening peaks and on inactive days (e.g., Friday).
-  Promote early morning hours (12–3 AM) with offers and safety campaigns.
-  Use K-Means zones to operationally split NYC for optimized driver distribution.
-  Coordinate with airports for better pickup logistics & reduce city cancellations.

---

## 🗂️ Dataset

- **File Name**: `Uber Request Data.csv`
- **Source**: Provided by course instructors
- **Format**: Tab-separated values (`.tsv`)
- **Rows**: 6,745 Uber ride requests
- **Description**: Raw log of Uber rides captured over a period of several days. Used for analyzing ride demand, driver activity, cancellations, and trip patterns.

### 🔑 Key Columns:

- `Request id`: Unique numeric ID for each ride request  
- `Pickup point`: Location where the ride was requested from (`City` or `Airport`)  
- `Driver id`: ID of the driver assigned (may be missing if unassigned)  
- `Status`: Trip outcome - `Trip Completed`, `Cancelled`, or `No Cars Available`  
- `Request timestamp`: Timestamp when the user requested the ride  
- `Drop timestamp`: Timestamp when the trip was completed (may be null)

---

## ⚙️ Installation

### Requirements

To get started, make sure you have **Python 3.10+** installed on your system.  
Then install all required libraries by running:

```bash
pip install -r requirements.txt
```
---

### 📦 Core Libraries Used

- `pandas` → data manipulation  
- `numpy` → numerical operations  
- `matplotlib`, `seaborn` → visualizations  
- `scikit-learn` → KMeans clustering  
- `python-dateutil` → parsing flexible timestamps  

---

### ✅ Setup Checklist

Ensure the following are in place before running the project:

-  `data/Uber Request Data.csv` is inside the `data/` folder  
-  `src/` contains all modular code files  
-  `output/` folder exists for saving processed results  
-  `main.py` exists in the project root  

---

### 🚀 Run the Full Pipeline

Run the entire analysis and visualization pipeline with:

```bash
python main.py
```
---

## 📽️ Inference Demo

Once the project is launched via `main.py`, the following steps are performed:

-  Loads and parses the raw Uber request dataset  
-  Cleans and preprocesses timestamps, missing values, and categories  
-  Extracts useful features like time slot, duration, and weekday  
-  Adds simulated geo-coordinates and clusters pickup points using **K-Means**  
-  Displays visual insights (trip patterns, demand peaks, hotspot regions)  
-  Saves enriched dataset to `output/Uber with features.csv`  

 Visualizations appear live using **matplotlib** and **seaborn**  
 Final processed dataset is reusable for further analysis  

---

## 📁 Project Structure

The project is organized in a modular, production-ready structure:

```
Uber-Trip-Analysis/
│
├── data/                         # Raw input data (Uber Request Data.csv)
│   └── Uber Request Data.csv
│
├── output/                       # Final enriched data & visual assets
│   └── Uber with features.csv
│
├── src/                          # All modular processing code
│   ├── __init__.py
│   ├── data_loading_and_exploration.py
│   ├── data_cleaning_and_preprocessing.py
│   ├── data_feature_engineering.py
│   ├── data_visualization.py
│   ├── location_clustering.py
│   └── save_transformed_data.py
│
├── main.py                       # Master pipeline to run the entire workflow
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 👥 Contributors

-   **Malak Salem**: Data loading, exploration, and reporting key patterns.
-  **Laila Shawky**: Cleaning and feature engineering (timestamps, nulls, derived fields).
-  **Jumanah Rushdi**: Visualizations and spatial clustering (K-Means on pickup points).

---

## 📝 License

- Open source under the **MIT License**.  
- Free to use, modify, and distribute with attribution.
