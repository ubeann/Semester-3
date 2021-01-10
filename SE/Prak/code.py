#%%

# Reference: https://medium.com/@adiptamartulandi/memprediksi-harga-rumah-dengan-machine-learning-multivariate-linear-regression-ucupstory-6f0bac830077
# Using VSCode + Interactive Window by Jupyter Notebook
# Code by Ubean, 081911633071

# import API or modules
import pandas as pd                 # Pandas, docs: https://pandas.pydata.org/docs/
import numpy as np                  # NumPy, docs: https://numpy.org/doc/ 
import matplotlib.pyplot as plt     # Matplotlib (plotting, optional), docs: https://matplotlib.org/
import seaborn as sns               # Seaborn (visualization, optional), docs: https://seaborn.pydata.org/ 
import os                           # OS (path), docs: https://docs.python.org/3/library/os.html

# import machine learning library for predict (Scikit-learn, Machine Learning in Python)
from sklearn.linear_model import LinearRegression           # docs: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
from sklearn.model_selection import train_test_split        # docs: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
from sklearn import preprocessing                           # docs: https://scikit-learn.org/stable/modules/preprocessing.html
from collections import defaultdict                         # docs: https://www.kite.com/python/docs/collections.defaultdict

# import data (CSV file), as much as possible code and data in the same directory
data = pd.read_csv('cars_data.csv')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# check the top 5 rows or instance of data --> head(x) , change x depends on what you want to check
# check from bottom rows or instance using --> tail(x)
# Independent variable (x) : normalized-losses, make, fuel-type, etc 
# Dependent variable (y) : price
# data.head() "remove '#' and this comment for run code"

# check the number of columns and rows of data
# data used has 201 rows and 26 columns
# data.shape "remove '#' and this comment for run code"

# check amount of data, data type, memory used, etc.
# data.info() "remove '#' and this comment for run code"

# check statistical description data start from the mean, quartile, standard deviation, etc.
# data.describe() "remove '#' and this comment for run code"

# check missing values in data
# has missing values (need action to fill it)
# data.isnull().sum() "remove '#' and this comment for run code"

# handle missing values in data
data = data.fillna(data.mean())     # fill missing numeric data using mean values
data = data.fillna('two')           # fill missing String data using value = "two"

# last check missing values in data, data has been filled completely
# data.isnull().sum() "remove '#' and this comment for run code"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Splitting data (80% Data Training, 20% Data Test)
# encoder_dict = defaultdict(preprocessing.LabelEncoder)                                # Creating dict for labeling data (Optional) --> remove '#' to use command
# inverse_transform_lambda = lambda x: encoder_dict[x.name].inverse_transform(x)        # Creating command for inverse labeling (Optional) --> remove '#' to use command
select = ["compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg"]         # edit this depends on your columns
x = data[select]                                                # take data for X-axis depends on "select" array
# x = x.apply(lambda x: encoder_dict[x.name].fit_transform(x))    # labeling data because data has the Strings data type (Optional) --> remove '#' to use command
y = data['price']                                               # take data for Y-axis, 'price' column
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 4)    # splitting data (x,y)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Regression
# create linear regression object
data_reg = LinearRegression()

# train the model using the split training data
data_reg.fit(x_train, y_train)

# calculate the value of the slope/coefficient (m) and intercept (b).
print("slope/koefisien (m):", end=" ")
print(data_reg.coef_)
print("intercept (b):", end=" ")
print(data_reg.intercept_)

# find out the accuracy score of the model using the testing data that has been split
test_score = data_reg.score(x_test, y_test)
print("Score Model: %.2f" % test_score, '%')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# do predictions using criteria (edit this depends your columns)
variable:dict = {
    "compression-ratio" : 13,
    "horsepower"        : 37,
    "peak-rpm"          : 2,
    "city-mpg"          : 8,
    "highway-mpg"       : 11,
    "key"              : ["compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg"]
}
print("Variable predict:")
sdtin = []
for i in variable["key"]:
    sdtin.append(variable[i])
    print("\t>",i+' =', variable[i])
data_predict = data_reg.predict([sdtin])
print("Price predict:", int(round(data_predict[0],0)),"$")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# saving data in CSV
path = os.path.dirname(os.path.abspath(__file__))+"\data"                               # path directory for save CSV file
y_test.to_csv(path + '\y_test.csv', index = True, index_label = 'index')                # save variable y_test
y_train.to_csv(path + '\y_train.csv', index = True, index_label = 'index')              # save variable y_train

# saving file CSV for NO Labeling data
x_test.to_csv(path + r'\x_test.csv', index = True, index_label = 'index')                # save variable x_test
x_train.to_csv(path + r'\x_train.csv', index = True, index_label = 'index')              # save variable x_train

# saving file CSV for Labeling data (remove '#' in command below to use)
# x_test.apply(inverse_transform_lambda).to_csv(path + r'\x_test.csv', index = True, index_label = 'index')            # save variable x_test
# x_train.apply(inverse_transform_lambda).to_csv(path + r'\x_train.csv', index = True, index_label = 'index')          # save variable x_test

# saving dict in txt
f = open(path + "\input-predict.txt","w")
f.write( str(variable) )
f.close()
# %%