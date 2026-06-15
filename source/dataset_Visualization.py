import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading both the original and pre-processed datasets

original_df = pd.read_csv("data/Employee_Details.csv")
processed_df = pd.read_csv("data/Employee_Details_Encoded.csv")

# Setting the Plot-Style

sns.set_style("whitegrid")

# Visualization 1 - Experience v/s Salary
# SCATTER PLOT

plt.figure(figsize=(10, 6))
sns.scatterplot(x = "YearsOfExperience", y = "Salary", data = original_df, color = "blue", alpha = 0.6)
plt.title("Experience v/s Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Visualization 2 - Average Salry by Job Role
# BAR PLOT

average_Salary_By_Job_Role = original_df.groupby("JobRole")["Salary"].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x = average_Salary_By_Job_Role.index, y = average_Salary_By_Job_Role.values, palette = "viridis")
plt.title("Average Salary by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.show()

# Visualization 3 - Correlation Heatmap
# HEATMAP

numeric_df = processed_df.select_dtypes(include = ["int64", "float64"])

correlation_Matrix = numeric_df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_Matrix, annot = True, cmap = "coolwarm", fmt = ".2f", linewidths = 0.5)
plt.title("Correlation Heatmap")
plt.show()

# Visualization 4 - Salary Distribution by Education Level
# BOX PLOT

plt.figure(figsize=(10, 6))
sns.boxplot(x = "EducationLevel", y = "Salary", data = original_df)
plt.title("Salary Distribution by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Salary")
plt.show()

print("Visualizations generated successfully")