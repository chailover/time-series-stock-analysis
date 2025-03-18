def create_lag_features(data, lag=1):
    """
    Create lag features for the time series data.
    
    Parameters:
    data (pd.Series): The time series data.
    lag (int): The number of lags to create.
    
    Returns:
    pd.DataFrame: DataFrame with lag features.
    """
    lagged_data = pd.DataFrame()
    for i in range(1, lag + 1):
        lagged_data[f'lag_{i}'] = data.shift(i)
    return lagged_data

def create_rolling_statistics(data, window=3):
    """
    Create rolling statistics for the time series data.
    
    Parameters:
    data (pd.Series): The time series data.
    window (int): The window size for rolling statistics.
    
    Returns:
    pd.DataFrame: DataFrame with rolling mean and rolling standard deviation.
    """
    rolling_mean = data.rolling(window=window).mean()
    rolling_std = data.rolling(window=window).std()
    return pd.DataFrame({'rolling_mean': rolling_mean, 'rolling_std': rolling_std})

def feature_engineering(data):
    """
    Perform feature engineering on the time series data.
    
    Parameters:
    data (pd.DataFrame): The time series data with a datetime index.
    
    Returns:
    pd.DataFrame: DataFrame with original data and engineered features.
    """
    lagged_features = create_lag_features(data['value'], lag=5)
    rolling_features = create_rolling_statistics(data['value'], window=3)
    return pd.concat([data, lagged_features, rolling_features], axis=1)