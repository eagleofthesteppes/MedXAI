import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

#load data
data = pd.read_csv('../data/OWID\ DataSet/owid-covid-data-master-file.csv')

#preprocess data
#assuming 'target' is the column you want to predict
X = data.drop('target', axis=1)
y = data['target']

#split data into training, testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#init, train  model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')

#save model
joblib.dump(model, 'trained_model.pkl')

# Load the model (for future use)
# model = joblib.load('trained_model.pkl')

# Make predictions on new data
# new_data = pd.read_csv('path_to_new_data.csv')
# predictions = model.predict(new_data)

