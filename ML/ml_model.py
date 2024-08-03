# Cell 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cell 2: Data Extraction
data_path = '../data/OWID DataSet/owid-covid-data-master-file.csv'
df = pd.read_csv(data_path)

# Cell 3: Data Analysis
print(df.head())
print(df.describe())

plt.figure(figsize=(12, 8))
plt.plot(df['Date'], df['Cases'], label='COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Cases Over Time')
plt.legend()
plt.show()

# Cell 4: Prediction Model
X = df[['Date']].values.reshape(-1, 1)
y = df['Cases'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Cell 5: Visualization of Predictions
plt.figure(figsize=(12, 8))
plt.plot(df['Date'], df['Cases'], label='Actual Cases')
plt.plot(X_test, y_pred, label='Predicted Cases', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('Actual vs Predicted COVID-19 Cases')
plt.legend()
plt.show()

