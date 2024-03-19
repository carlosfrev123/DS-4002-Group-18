import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv('your_data.csv')

# Preprocess your data
# ...

# Create X and y
X = df[['average_points_per_game', 'years']]
y = df['average_salary']

# Split your data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit your model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate your model
score = model.score(X_test, y_test)
print(f'R^2 Score: {score}')

# Print the coefficients
coefficients = model.coef_
print(f'Coefficients: {coefficients}')

# Predict future salaries
future_data = [[20, 2029]]  # example data
predicted_salary = model.predict(future_data)
print(f'Predicted Salary: {predicted_salary}')