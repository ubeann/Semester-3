# Code by Ubean, 081911633071
import numpy as np
import sklearn.metrics as metrics
from sklearn import datasets
from sklearn.linear_model import LinearRegression

def regression_results(y_true, y_pred):

    # Regression metrics
    explained_variance = metrics.explained_variance_score(y_true, y_pred)
    mean_absolute_error = metrics.mean_absolute_error(y_true, y_pred) 
    mse = metrics.mean_squared_error(y_true, y_pred) 
    mean_squared_log_error = metrics.mean_squared_log_error(y_true, y_pred)
    median_absolute_error = metrics.median_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)

    print('\t> explained_variance:', round(explained_variance,4))    
    print('\t> mean_squared_log_error:', round(mean_squared_log_error,4))
    print('\t> r2:', round(r2,4))
    print('\t> MAE:', round(mean_absolute_error,4))
    print('\t> MSE:', round(mse,4))
    print('\t> RMSE:', round(np.sqrt(mse),4))

solved = "Credit by Ubean | 081911633071"