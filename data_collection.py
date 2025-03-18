import yfinance as yf
import pandas as pd

def download_stock_data(ticker, start_date, end_date):
    """
    Downloads historical stock price data from Yahoo Finance.

    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The start date for the data in 'YYYY-MM-DD' format.
    end_date (str): The end date for the data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the stock price data.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def save_data_to_csv(data, filepath):
    """
    Saves the DataFrame to a CSV file.

    Parameters:
    data (pd.DataFrame): The DataFrame to save.
    filepath (str): The path where the CSV file will be saved.
    """
    data.to_csv(filepath, index=True)