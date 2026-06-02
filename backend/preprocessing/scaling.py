from sklearn.preprocessing import StandardScaler

def scale_data(train_X, test_X):
    scaler = StandardScaler()

    # Fit only on train
    train_scaled = scaler.fit_transform(train_X)

    # Use same scaler for test
    test_scaled = scaler.transform(test_X)

    return train_scaled, test_scaled, scaler