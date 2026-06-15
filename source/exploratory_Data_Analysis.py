import pandas as pd


# Loading the Datasets [original and encoded]


original_df = pd.read_csv("data/Employee_Details.csv")

processed_df = pd.read_csv("data/Employee_Details_Encoded.csv")

print("\n========================================")
print("EMPLOYEE SALARY DATASET ANALYSIS")
print("========================================")


# Relationship Between Experience and Salary


print()
print("EXPERIENCE VS SALARY ANALYSIS")
print()

experience_Salary_correlation = (original_df["YearsOfExperience"].corr(original_df["Salary"]))

print(
    f"\nCorrelation between Experience and Salary: "
    f"{experience_Salary_correlation:.4f}"
)

if experience_Salary_correlation > 0:
    print("Observation: Salary increases as experience increases.")
else:
    print("Observation: No positive relationship found.")


# Education Level Impact


print()
print("EDUCATION LEVEL ANALYSIS")
print()

education_Salary = (original_df.groupby("EducationLevel")["Salary"].mean().sort_values(ascending=False))

print("\nAverage Salary by Education Level:")
print(education_Salary)

highest_Education_Salary = education_Salary.idxmax()

print(f"\nHighest Average Salary: {highest_Education_Salary}")


# Job Role Analysis


print()
print("JOB ROLE ANALYSIS")
print()

job_Role_Salary = (original_df.groupby("JobRole")["Salary"].mean().sort_values(ascending=False))

print("\nAverage Salary by Job Role:")
print(job_Role_Salary)

highest_Paid_Role = job_Role_Salary.idxmax()

print(f"\nHighest Paying Role: {highest_Paid_Role}")


# Company Type Analysis


print()
print("COMPANY TYPE ANALYSIS")
print()

company_Salary_By_Company_Type = (original_df.groupby("CompanyType")["Salary"].mean().sort_values(ascending=False))

print("\nAverage Salary by Company Type:")
print(company_Salary_By_Company_Type)


# Skills Score Analysis


print()
print("SKILLS SCORE ANALYSIS")
print()

skills_corr = (original_df["SkillScore"].corr(original_df["Salary"]))

print(
    f"\nCorrelation between Skills Score and Salary: "
    f"{skills_corr:.4f}")


# Certifications Analysis


print()
print("CERTIFICATION ANALYSIS")
print()

certification_Correlation = (original_df["Certifications"].corr(original_df["Salary"]))

print(
    f"\nCorrelation between Certifications and Salary: "
    f"{certification_Correlation:.4f}")


# 7. Correlation Analysis


print()
print("CORRELATION ANALYSIS")
print()

numeric_df = processed_df.select_dtypes(include=["int64", "float64"])

corr_matrix = numeric_df.corr()

salary_correlations = (corr_matrix["Salary"].sort_values(ascending=False))

print("\nCorrelation with Salary:")
print(salary_correlations)

print("\nTop Features Affecting Salary:")

top_features = (salary_correlations.drop("Salary").head(5))

print(top_features)


# Final Conclusions


print("\n========================================")
print("EDA CONCLUSIONS")
print("========================================")

print(
    """
1. Experience shows a strong positive relationship with salary.

2. Higher education levels generally receive higher salaries.

3. Job roles significantly influence salary levels.

4. Skills Score positively impacts salary.

5. Certifications positively impact salary.

6. Company type influences salary distribution.

7. Correlation analysis identifies the most important factors affecting employee salaries.
"""
)