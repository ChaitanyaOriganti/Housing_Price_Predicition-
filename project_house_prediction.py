# -*- coding: utf-8 -*-
"""project_house_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RfM8rGySPHdbBVnhtWXq1ihw_8p1KnaG
"""

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv('kc_house_data.csv')

data.head()

data.info()

def onehot_encode(df, column, prefix):
    df = df.copy()
    dummies = pd.get_dummies(df[column], prefix=prefix)
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column, axis=1)
    return df

data = data.drop('id', axis=1)

data['year'] = data['date'].apply(lambda x: x[0:4])
data['month'] = data['date'].apply(lambda x: x[4:6])
data = data.drop('date', axis=1)

data = onehot_encode(data, 'zipcode', 'zip')

data.query('yr_renovated != 0')

data = data.drop('yr_renovated', axis=1)

y = data['price'].copy()
X = data.drop('price', axis=1).copy()

scaler = StandardScaler()
X = scaler.fit_transform(X)

tf_X_train, tf_X_test, tf_y_train, tf_y_test = train_test_split(X, y, train_size=0.7, random_state=1)

tf_X_test.shape

tf_y_test.shape

"""<b><h3> Regression Models </h3></b>"""

from sklearn.svm import SVR
svr = SVR(kernel='linear')
svr.fit(tf_X_train,tf_y_train)
y_pred=svr.predict(tf_X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Assuming you have already trained your SVR model and obtained predictions y_pred

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(tf_y_test, y_pred)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(tf_y_test, y_pred)

# Calculate R-squared (R2)
r2 = r2_score(tf_y_test, y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

from sklearn.ensemble import RandomForestRegressor

# Instantiate the regressor with oob_score=True
regressor = RandomForestRegressor(n_estimators=50, random_state=0, oob_score=True)

# Reshape tf_y_train
tf_y_train_reshaped = tf_y_train.ravel()

# Fit the regressor
regressor.fit(tf_X_train, tf_y_train_reshaped)

tf_y_pred=regressor.predict(tf_X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(tf_y_test, tf_y_pred)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(tf_y_test, tf_y_pred)

# Calculate Root Mean Squared Error (RMSE)
rmse = mean_squared_error(tf_y_test, tf_y_pred, squared=False)

# Calculate R-squared (R2) score
r2 = r2_score(tf_y_test, tf_y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2) Score:", r2)

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Instantiate the Gradient Boosting Regressor
gb_regressor = GradientBoostingRegressor(random_state=0)

# Fit the regressor to the training data
gb_regressor.fit(tf_X_train, tf_y_train.ravel())

# Predict the target variable for the test set
tf_y_pred_gb = gb_regressor.predict(tf_X_test)

# Calculate metrics
mae_gb = mean_absolute_error(tf_y_test, tf_y_pred_gb)
mse_gb = mean_squared_error(tf_y_test, tf_y_pred_gb)
rmse_gb = mean_squared_error(tf_y_test, tf_y_pred_gb, squared=False)
r2_gb = r2_score(tf_y_test, tf_y_pred_gb)

print("Gradient Boosting Regression Metrics:")
print("Mean Absolute Error (MAE):", mae_gb)
print("Mean Squared Error (MSE):", mse_gb)
print("Root Mean Squared Error (RMSE):", rmse_gb)
print("R-squared (R2) Score:", r2_gb)

import tensorflow as tf

temp_normalizer =tf.keras.layers.Normalization(input_shape=(1,),axis=None)
temp_normalizer.adapt(tf_X_test.reshape(-1))

temp_nn_model=tf.keras.Sequential([
    temp_normalizer,
    tf.keras.layers.Dense(1)
])
temp_nn_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),loss='mean_squared_error')

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.losses import MeanSquaredError

nn_model = Sequential([
    Dense(64, activation='relu', input_shape=(88,)),  # Adjust input shape to match the number of features
    Dense(32, activation='relu'),
    Dense(1, activation='relu')
])
nn_model.compile(optimizer='adam', loss=MeanSquaredError())

print("Shape of training data:", tf_X_train.shape)
print("Shape of testing data:", tf_X_test.shape)

y_pred=nn_model.predict(tf_X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Predictions
y_pred = nn_model.predict(tf_X_test)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(tf_y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae}")

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(tf_y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse}")

import pandas as pd

# Assuming 'data' is loaded correctly as a pandas DataFrame
data = pd.read_csv('kc_house_data.csv')
data = pd.DataFrame(data)  # Ensure 'data' is a DataFrame

def categorize_sqft(row):
    sqft, sqft_lot, floors, bedrooms, bathrooms, condition, view, waterfront, grade, yr_built, sqft_basement, sqft_above, sqft_living15 = row
    if (sqft < 2500 and sqft_lot < 10000 and floors <= 2 and
        bedrooms <= 4 and bathrooms <= 3 and view < 1 and waterfront == 0 and grade <= 7 and yr_built <= 1975 and
        sqft_basement <= 1000 and sqft_above > 1000 and sqft_living15 > 1000):
        return 'low_value'
    else:
        return 'high_value'

# Apply the function to create a new column
data['value_category'] = data[['sqft_living', 'sqft_lot', 'floors', 'bedrooms', 'bathrooms', 'condition',
                               'view', 'waterfront', 'grade', 'yr_built', 'sqft_basement', 'sqft_above', 'sqft_living15']].apply(categorize_sqft, axis=1)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Prepare features and target variable
X = data.drop(['id', 'date', 'price','value_category'], axis=1)
X = pd.get_dummies(X)  # One-hot encode categorical column
y = data['value_category']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = rf_classifier.predict(X_test)
u_u=rf_classifier.predict_proba(X_test)
print(u_u)
importances = rf_classifier.feature_importances_
print(importances)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print classification report and confusion matrix
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

from sklearn.neighbors import KNeighborsClassifier

# Initialize and train the K-Nearest Neighbors classifier
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred_knn = knn_classifier.predict(X_test)
u_u=rf_classifier.predict_proba(X_test)
print(u_u)
# Calculate accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print("Accuracy (K-Nearest Neighbors):", accuracy_knn)

# Print classification report and confusion matrix for K-Nearest Neighbors
print("Classification Report (K-Nearest Neighbors):")
print(classification_report(y_test, y_pred_knn))
print("Confusion Matrix (K-Nearest Neighbors):")
print(confusion_matrix(y_test, y_pred_knn))

