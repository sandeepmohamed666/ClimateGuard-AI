


from pathlib import Path
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

root_path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_path))

from backend.utils.data_loader import load_data

# =========================
# LOAD DATA
# =========================
train_path = "datasets/raw/DailyDelhiClimateTrain.csv"
test_path = "datasets/raw/DailyDelhiClimateTest.csv"
weather_path = "datasets/raw/global_weather.csv"
nasa_path = "datasets/raw/nasa_power.csv"

train_df, test_df, weather_df, nasa_df = load_data(
    train_path,
    test_path,
    weather_path,
    nasa_path,
)

print("Train Shape:", train_df.shape)
print("Test Shape:", test_df.shape)
print("Weather Shape:", weather_df.shape)
print("NASA Shape:", nasa_df.shape)

print("\nTrain Info:")
print(train_df.info())


# =========================
# FUNCTION: BASIC EDA PLOTS
# =========================
def basic_eda(df, name="Dataset"):
    print(f"\n===== {name} =====")

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Summary stats
    print("\nDescribe:")
    print(df.describe())

    # =========================
    # 1. Histogram
    # =========================
    df.hist(figsize=(12, 8), bins=20)
    plt.suptitle(f"{name} - Feature Distributions")
    plt.show()

    # =========================
    # 2. Boxplots
    # =========================
    # num_cols = df.select_dtypes(include=np.number).columns

    # for col in num_cols:
    #     plt.figure()
    #     sns.boxplot(x=df[col])
    #     plt.title(f"{name} - Outliers in {col}")
    #     plt.show()
    num_cols = df.select_dtypes(include=np.number).columns

    n_cols = 3  # number of plots per row
    n_rows = int(np.ceil(len(num_cols) / n_cols))

    plt.figure(figsize=(15, 5 * n_rows))

    for i, col in enumerate(num_cols, 1):
        plt.subplot(n_rows, n_cols, i)
        sns.boxplot(x=df[col])
        plt.title(f"Outliers in {col}")

    plt.tight_layout()
    plt.suptitle(f"{name} - Boxplots", y=1.02)
    plt.show()

    # =========================
    # 3. Correlation Heatmap
    # =========================
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True),
                annot=False,
                cmap="coolwarm")
    plt.title(f"{name} - Correlation Heatmap")
    plt.show()

    # =========================
    # 4. Pairplot
    # =========================
    if len(num_cols) <= 6:
        sns.pairplot(df[num_cols])
        plt.suptitle(f"{name} - Pairplot", y=1.02)
        plt.show()


# =========================
# RUN EDA
# =========================
basic_eda(train_df, "Train Data")
basic_eda(test_df, "Test Data")
basic_eda(weather_df, "Weather Data")
basic_eda(nasa_df, "NASA Data")