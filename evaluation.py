def evaluate_model(y_true, y_pred):
    from sklearn.metrics import mean_absolute_error, mean_squared_error
    import numpy as np

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape
    }

def plot_predictions(y_true, y_pred):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(y_true, label='Actual', color='blue')
    plt.plot(y_pred, label='Predicted', color='orange')
    plt.title('Actual vs Predicted')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.show()