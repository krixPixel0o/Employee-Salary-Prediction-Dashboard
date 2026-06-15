# 💼 Employee Salary Prediction System

## 📌 Project Overview

The Employee Salary Prediction System is a Machine Learning-based application developed to predict employee salaries based on various professional and personal attributes.

The project covers the complete Machine Learning lifecycle, including:

- Dataset Generation
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Model Development
- Model Evaluation
- Interactive Salary Prediction Dashboard using Streamlit

The objective of the project is to analyze factors affecting employee salaries and build a regression model capable of accurately predicting employee compensation.

---

# 📊 Dataset Generation Process

A synthetic dataset containing **2000 employee records** was generated using Python libraries such as Pandas and NumPy.

### Features Included

| Feature | Description |
|----------|-------------|
| EmployeeID | Unique employee identifier |
| Age | Employee age |
| Gender | Male/Female |
| EducationLevel | Bachelor's/Master's/PhD |
| YearsOfExperience | Total years of experience |
| JobRole | Employee role |
| SkillScore | Technical skill rating (1–10) |
| Certifications | Number of certifications |
| CompanyType | Startup/Medium/MNC |
| WorkHoursPerWeek | Weekly work hours |
| Salary | Target variable |

### Salary Generation Logic

Salary values were generated based on:

- Age
- Years of Experience
- Skill Score
- Certifications
- Education Level
- Company Type
- Job Role

Random noise was added to simulate real-world salary variations.

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

### Handling Missing Values

- Numerical features → Median Imputation
- Categorical features → Mode Imputation

### Duplicate Removal

- Duplicate records were identified and removed.

### Data Validation

Validation checks were applied on:

- Age
- Years of Experience
- Skill Score
- Certifications
- Salary

### Categorical Encoding

One-Hot Encoding was applied to categorical features:

- Gender
- Education Level
- Job Role
- Company Type

---

# 📈 Exploratory Data Analysis (EDA)

The dataset was analyzed to identify patterns and relationships among features.

### Analysis Performed

- Relationship between Experience and Salary
- Impact of Education Level on Salary
- Salary Distribution across Job Roles
- Skills Score vs Salary Analysis
- Certifications vs Salary Analysis
- Company Type vs Salary Analysis
- Feature Correlation Analysis

---

# 📊 Visualizations

The following visualizations were created:

### 1. Experience vs Salary

Scatter plot showing the relationship between experience and salary.

### 2. Average Salary by Job Role

Bar chart comparing salary levels across job roles.

### 3. Correlation Heatmap

Heatmap showing correlation between numerical features.

### 4. Salary Distribution by Education Level

Box plot comparing salary distributions for different education levels.

---

# 🤖 Machine Learning Models

The following regression algorithms were trained and evaluated:

### 1. Linear Regression

Used as the baseline regression model.

### 2. Decision Tree Regressor

Used to capture non-linear salary patterns.

### 3. Random Forest Regressor

Ensemble learning model for improved prediction performance.

---

# 📊 Model Performance Summary

| Model | MAE | RMSE | R² Score |
|---------|---------:|---------:|---------:|
| Linear Regression | ₹25,662 | ₹29,762 | **0.9848** |
| Decision Tree Regressor | ₹37,225 | ₹45,601 | 0.9643 |
| Random Forest Regressor | ₹27,946 | ₹33,856 | 0.9803 |

### Best Model

✅ Linear Regression

**R² Score:** 0.9848

**MAE:** ₹25,662

The Linear Regression model achieved the highest performance and was selected as the final model.

---

# 💻 Streamlit Dashboard

The project includes an interactive Streamlit dashboard where users can:

- Enter employee details
- Predict annual salary
- View prediction insights
- Access model information

### Dashboard Features

- Input Validation
- Error Handling
- Salary Prediction
- Model Performance Display
- Encoded Feature Preview

---

# 🔍 Key Insights from Analysis

### 1. Experience Strongly Influences Salary

Employees with more years of experience generally receive higher salaries.

### 2. Higher Education Leads to Higher Salaries

PhD and Master's degree holders typically earn more than Bachelor's degree holders.

### 3. Skill Score Positively Impacts Salary

Higher technical skill ratings contribute to increased salary predictions.

### 4. Certifications Improve Compensation

Employees with more certifications tend to earn higher salaries.

### 5. Company Type Affects Salary

MNCs generally offer higher salaries than startups.

### 6. Job Role Influences Compensation

Management and specialized technical roles tend to have higher salary ranges.

---

# 📚 Libraries Used

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn
- Joblib

### Web Application

- Streamlit

---

# 📂 Project Structure

```text
Employee-Salary-Prediction-System/

├── data/
│   ├── Employee_Details.csv
│   └── Employee_Details_Encoded.csv
│
├── model/
│   └── best_salary_prediction_model.pkl
│
├── source/
│   ├── generate_Dataset.py
│   ├── preprocessing_Dataset.py
│   ├── exploratory_Data_Analysis.py
│   ├── dataset_Visualization.py
│   └── train_Model.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ▶️ Steps to Run the Project

### Step 1: Clone Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to Project Directory

```bash
cd Employee-Salary-Prediction-System
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Launch Streamlit Application

```bash
streamlit run app.py
```

### Step 5: Open Browser

The application will automatically open in your default browser.

---

# ✅ Error Handling

The application includes:

- Input Validation
- Invalid Data Detection
- Model Loading Validation
- Prediction Error Handling
- Runtime Error Prevention

---

# 🚀 Future Enhancements

- Real-world dataset integration
- Advanced feature engineering
- Hyperparameter tuning
- Model deployment on cloud platforms
- Salary trend forecasting
- HR analytics dashboard

---

# 👨‍💻 Author

Employee Salary Prediction System

Machine Learning Internship Project

Built using Python, Scikit-Learn, and Streamlit.