# -*- coding: utf-8 -*-
"""SALES PREDICTION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vh6ViSlFHVDYCMqg0p33pXG5LkRV6FlW

***Note:*** *Connect your Google Drive when running the snippets*

*Download dataset here [SALES PRDICTION](https://drive.google.com/file/d/1JWdttoLmCdFqI47LxBeT3-tFZ5mojiuA/view?usp=share_link)*

### Knowing about the Dataset

**Importing the Required Libraries**
"""

# Numpy Library for Numerical Calculations
import numpy as np

# Pandas Library for Dataframe
import pandas as pd

# Matplotlib and Seaborn for Plottings
import matplotlib.pyplot as plt
import seaborn as sns

# Pickle Library for Saving the Model
import pickle

# Train_Test_Split for splitting the Dataset
from sklearn.model_selection import train_test_split

# Linear Regression is the Model
from sklearn.linear_model import LinearRegression

# KFold and Cross_Val_Score for Validation
from sklearn.model_selection import cross_val_score

# Metrics is for Analysis of Models
from sklearn import metrics

# Scipy is for Scientific Calculations in Python
from scipy import stats

# ProfileReport is for geting the report of the Dataframe
from pandas_profiling import ProfileReport

# Variance Inflation Rate is for getting the change factor in Variance
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Data Cleaning Suggestions and Data Suggestions are for cleaning the Dataframe in an unique way
from autoviz.classify_method import data_cleaning_suggestions ,data_suggestions

# Regression is for importing all the regression models
from pycaret.regression import *

"""**Reading informations in the Dataset**"""

sales = pd.read_csv("/content/drive/MyDrive/Advertising.csv")

"""**Checking for null values in Data**"""

sales.isnull().sum()

"""**Checking the First Five Values in the Data**"""

sales.head()

"""**Checking the Last Five Values in the Data**"""

sales.tail()

"""**Dimensions of the Dataset**"""

sales.shape

"""**Describing the Dataset**"""

sales.describe()

"""### Visualization of the Data

**TV Sales Plotting**
"""

plt.figure(figsize=(4,4))
sns.scatterplot(data = sales, x = sales['TV'], y = sales['Sales'])
plt.show()

"""**Radio Sales Plotting**"""

plt.figure(figsize=(4,4))
sns.scatterplot(data = sales, x = sales['Radio'], y = sales['Sales'])
plt.show()

"""**Radio Sales Plotting**"""

plt.figure(figsize=(4,4))
sns.scatterplot(data = sales, x = sales['Newspaper'], y = sales['Sales'])
plt.show()

"""### Data Modeling

**Splitting the Dataset into Training and Testing**
"""

X = sales.drop(['Unnamed: 0','Sales'], axis=1)
Y = sales['Sales']
print("X Dimention: ", X.shape)
print("Y Dimention: ", Y.shape)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=25)

"""**Checking the Dimensions of Training and Testing Data**"""

print("X_Train Shape:", X_train.shape)
print("X_Test Shape:", X_test.shape)
print("Y_Train Shape:", X_train.shape)
print("Y_Test Shape:", Y_test.shape)

"""### Model Building

**Creating the Model**
"""

model = LinearRegression()
model.fit(X_train,Y_train)

pred = model.predict(X_test)

"""### Model Testing

**Testing the Model**
"""

print('MAE: ', metrics.mean_absolute_error(pred,Y_test))
print('RMSE: ', np.sqrt(metrics.mean_squared_error(pred,Y_test)))
print('R-Squared: ', metrics.r2_score(pred,Y_test))

"""### Saving Model

**Saving the Model**
"""

filename = "Linear_Regression.pkl"
pickle.dump(model, open(filename, 'wb'))
print("Saved the Model")

"""Accuracy of the Linear Regression Model is 86%

### Pycaret

**Comparing Regression Models**
"""

s = setup(data = sales, target = 'Sales', session_id=123)

compare_models()

"""**Finalizing the Best Model**"""

etr = create_model('et')

etr = finalize_model(etr)
etr

preds = predict_model(etr)

"""Accuracy of the Model is 100%"""