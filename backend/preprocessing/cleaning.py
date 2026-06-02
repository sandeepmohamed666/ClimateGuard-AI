
import pandas as pd

weather = pd.read_csv("datasets/raw/global_weather.csv")
nasa = pd.read_csv("datasets/raw/nasa_power.csv")

import pandas as pd

nasa["datetime"] = pd.to_datetime(
    nasa[["YEAR", "month", "day", "hr"]]
)

nasa = nasa.drop(columns=["YEAR", "month", "day", "hr"])
weather["datetime"] = pd.to_datetime(weather["last_updated"])

final_df = weather.merge(
    nasa,
    on="datetime",
    how="inner"
)

# ===================
# weather.columns = weather.columns.str.lower()
# nasa.columns = nasa.columns.str.lower()

# weather["date"] = pd.to_datetime(weather["date"])
# nasa["date"] = pd.to_datetime(nasa["date"])

# print(weather["date"].isnull().sum())
# print(nasa["date"].isnull().sum())

# final_df = weather.merge(nasa, on="date", how="inner")

# ================
# import pandas as pd

# # 1. Load data
# train_df = pd.read_csv("datasets/train.csv")
# test_df = pd.read_csv("datasets/test.csv")
# weather_df = pd.read_csv("datasets/weather.csv")
# nasa_df = pd.read_csv("datasets/nasa.csv")

# # 2. Clean function
# def clean_data(df):
#     return df.drop_duplicates()

# # 3. Apply cleaning
# train_df = clean_data(train_df)
# test_df = clean_data(test_df)
# weather_df = clean_data(weather_df)
# nasa_df = clean_data(nasa_df)