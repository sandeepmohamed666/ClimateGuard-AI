

from pathlib import Path
import sys

root_path = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_path))

from backend.utils.data_loader import load_data

train_df, test_df, weather_df, nasa_df = load_data(
    "datasets/raw/DailyDelhiClimateTrain.csv",
    "datasets/raw/DailyDelhiClimateTest.csv",
    "datasets/raw/global_weather.csv",
    "datasets/raw/nasa_power.csv"
)

print(train_df.head())
print(test_df.head())
print(weather_df.head())
print(nasa_df.head())