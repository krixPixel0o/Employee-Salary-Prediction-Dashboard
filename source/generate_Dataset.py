# Importing the modules for dataset generation 
import numpy as np
import pandas as pd

np.random.seed(42) # To ensure reproducibility

# ------------------------------
# Generating the Employee Data !
# ------------------------------

num_Records = 2000 # Required Number of Samples (2000)

# Generating Employee ID (Unique)

emp_IDs = np.arange(107, 107 + num_Records) # Employee IDs starting from 107

ages = np.random.randint(21, 60, size = num_Records) # Ages between 21 and 60

genders = np.random.choice(['Male', 'Female'], size = num_Records) # Randomly assigning genders

edu_Level = np.random.choice(["Bachelor's", "Master's", 'PhD'], size = num_Records) # Randomly assigning education levels

years_Of_Exp = np.random.randint(0, 40, size = num_Records) # Years of experience between 0 and 40

job_Role = np.random.choice(["Developer", "Data Analyst", "Manager", "Designer", "Quality Compliance Tester"], size = num_Records) # Randomly assigning job roles

skill_Score = np.random.randint(1, 11, size = num_Records) # Skill scores between 1 and 10

no_Certifications = np.random.randint(0, 11, size = num_Records) # Number of certifications between 0 and 10

company_Type = np.random.choice(["Startup", "MNC", "Medium"], size = num_Records) # Randomly assigning company types

work_Hours_Per_Week = np.random.randint(20, 61, size = num_Records) # Setting all the employees' work hours per week between 20 and 60

# ------------------------------------------------------
# Creating some additional features for salary formula !
# ------------------------------------------------------

education_bonus = {
    "Bachelor's": 0,
    "Master's": 200000,
    "PhD": 500000
}

company_bonus = {
    "Startup": 0,
    "Medium": 150000,
    "MNC": 300000
}

job_role_bonus = {
    "Developer": 100000,
    "Data Analyst": 80000,
    "Manager": 250000,
    "Designer": 70000,
    "Quality Compliance Tester": 60000
}

salaries_Of_Employees = []

# ------------------------------------------------------------
# Creating the salary formula and adding this to the dataset !
# ------------------------------------------------------------

for a in range(num_Records) :        # Salary generation formula
    noise = np.random.randint(-50000, 50001)

    salary = (45000
              + (ages[a] * 1000)
              + (years_Of_Exp[a] * 1500)
              + (skill_Score[a] * 2000)
              + (no_Certifications[a] * 3000)
              + education_bonus[edu_Level[a]]
              + company_bonus[company_Type[a]]
              + job_role_bonus[job_Role[a]]
              + noise
              )

    salaries_Of_Employees.append(salary)

# ----------------------
# Creating a DataFrame !
# ----------------------

df = pd.DataFrame({
    "EmployeeID" : emp_IDs,
    "Age" : ages,
    "Gender" : genders,
    "EducationLevel" : edu_Level,
    "YearsOfExperience" : years_Of_Exp,
    "JobRole" : job_Role,
    "SkillScore" : skill_Score,
    "Certifications" : no_Certifications,
    "CompanyType" : company_Type,
    "WorkHoursPerWeek" : work_Hours_Per_Week,
    "Salary" : salaries_Of_Employees
})

# ------------------------------------
# Saving the dataset to the CSV File !
# ------------------------------------

df.to_csv("data/Employee_Details.csv", index = False) 

# --------------
# Confirmation !
# --------------

print("Dataset generated succesfully")
print("About the dataset - ")
print(f"Number of records: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("First 5 records - ")
print(df.head(5))
print("Dataset Info - ")
print(df.info())