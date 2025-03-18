import pandas as pd

def load_data(file_path):
    """Load the dataset from a specified file path."""
    data = pd.read_csv(file_path, parse_dates=True, index_col='Date')
    return data

def handle_missing_values(data):
    """Handle missing values in the dataset."""
    # Fill missing values with the forward fill method
    data.fillna(method='ffill', inplace=True)
    # Alternatively, you can drop missing values
    # data.dropna(inplace=True)
    return data

def format_time_series(data):
    """Ensure the data is formatted correctly as a time series."""
    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("Index must be a DatetimeIndex.")
    return data

def clean_data(file_path):
    """Main function to clean the data."""
    data = load_data(file_path)
    data = handle_missing_values(data)
    data = format_time_series(data)
    return data

def save_cleaned_data(data, output_path):
    """Save the cleaned data to a specified output path."""
    data.to_csv(output_path)