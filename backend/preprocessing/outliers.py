import pandas as pd

def detect_outliers_iqr(train_df, column):
    Q1 = train_df[column].quantile(0.25)
    Q3 = train_df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = train_df[(train_df[column] < lower_bound) | (train_df[column] > upper_bound)]

    return outliers

def detect_outliers_iqr(test_df, column):
    Q1 = test_df[column].quantile(0.25)
    Q3 = test_df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = test_df[(test_df[column] < lower_bound) | (test_df[column] > upper_bound)]

    return outliers


    
def remove_outliers_iqr(train_df, column):
    Q1 = train_df[column].quantile(0.25)
    Q3 = train_df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    train_df_cleaned = train_df[(train_df[column] >= lower) & (train_df[column] <= upper)]

    return train_df_cleaned

def remove_outliers_iqr(test_df, column):
    Q1 = test_df[column].quantile(0.25)
    Q3 = test_df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    test_df_cleaned = test_df[(test_df[column] >= lower) & (test_df[column] <= upper)]

    return test_df_cleaned