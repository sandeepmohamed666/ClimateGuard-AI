def validate_data(train_df):
    assert train_df.isnull().sum().sum() == 0, "Missing values found!"
    assert len(train_df) > 0, "Empty dataset!"
    return True

def validate_data(test_df):
    assert test_df.isnull().sum().sum() == 0, "Missing values found!"
    assert len(test_df) > 0, "Empty dataset!"
    return True