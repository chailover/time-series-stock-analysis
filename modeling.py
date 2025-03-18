from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np
import pandas as pd

def split_data(data, test_size=0.2):
    train, test = train_test_split(data, test_size=test_size, shuffle=False)
    return train, test

def train_arima_model(train, order):
    model = ARIMA(train, order=order)
    model_fit = model.fit()
    return model_fit

def train_sarima_model(train, order, seasonal_order):
    model = SARIMAX(train, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit()
    return model_fit

def predict(model, steps):
    return model.forecast(steps)

def evaluate_model(predictions, actual):
    mae = np.mean(np.abs(predictions - actual))
    rmse = np.sqrt(np.mean((predictions - actual) ** 2))
    mape = np.mean(np.abs((actual - predictions) / actual)) * 100
    return mae, rmse, mape