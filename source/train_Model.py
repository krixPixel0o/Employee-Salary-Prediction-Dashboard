import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Loading the pre-processed dataset
try:
    df = pd.read_csv('data/Employee_Details_Encoded.csv')
    print("Pre-processed dataset loaded successfully")
    print("Dataset shape - ", df.shape)
    print("Dataset columns - ", df.columns)
except FileNotFoundError:
    print("Pre-processed dataset not found. Please preprocess the dataset first using 'preprocessing_Dataset.py' script.")

# Features Selection 

X = df.drop(columns = ["EmployeeID", "Salary"])
y = df["Salary"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.29, random_state = 42)


# Evaluating Model

def evaluate_model(name, model) :
    predictions = model.predict(X_test)

    mean_Ab_Error = mean_absolute_error(y_test, predictions)
    mean_Sq_Error = mean_squared_error(y_test, predictions)
    root_Mean_Sq_Error = mean_Sq_Error ** 0.5
    r2 = r2_score(y_test, predictions)

    print(f"\n{name} Model Evaluation Metrics:")
    print(f"Mean Absolute Error: {mean_Ab_Error:.2f}")
    print(f"Mean Squared Error: {mean_Sq_Error:.2f}")
    print(f"Root Mean Squared Error: {root_Mean_Sq_Error:.2f}")
    print(f"R-squared: {r2:.4f}")

    return r2

# Linear Regression Model

linear_Model = LinearRegression()
linear_Model.fit(X_train, y_train)

linear_r2 = evaluate_model("Linear Regression", linear_Model)

# Decision Tree Regressor Model

decision_Tree_Model = DecisionTreeRegressor(random_state = 42)
decision_Tree_Model.fit(X_train, y_train)
decision_Tree_r2 = evaluate_model("Decision Tree Regressor", decision_Tree_Model)

# Random Forest Regressor Model

random_Forest_Model = RandomForestRegressor(random_state = 42)
random_Forest_Model.fit(X_train, y_train)
random_Forest_r2 = evaluate_model("Random Forest Regressor", random_Forest_Model)


# Selecting the best model based on R-squared value

models = {"Linear Regression" : (linear_Model, linear_r2),
          "Decision Tree Regressor" : (decision_Tree_Model, decision_Tree_r2),
          "Random Forest Regressor" : (random_Forest_Model, random_Forest_r2)}

best_Model = max(models, key = lambda x : models[x][1])

best_Score = models[best_Model][1]

print(f"\nBest Model: {best_Model} with R-squared value: {best_Score:.4f}")


# Saving the best model !

joblib.dump(models[best_Model][0], "model/best_salary_prediction_model.pkl") 

print("Best model saved successfully.")