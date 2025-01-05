
# NHANES Body Measurements Analysis  
### Introduction  
# This notebook analyzes body measurements of adult males and females from the National Health and Nutrition Examination Survey (NHANES).   
# The focus will be on weight distributions, BMI calculations, and correlations between different body measurements.  

# 1. Data Acquisition  
import numpy as np   
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  

# Load the datasets from local files  
male_data = pd.read_csv(r'C:\Users\alina\Downloads\nhanes_adult_male_bmx_2020.csv', on_bad_lines='skip')  
female_data = pd.read_csv(r'C:\Users\alina\Downloads\nhanes_adult_female_bmx_2020.csv', on_bad_lines='skip')  

# Check the datasets (optional but useful for debugging)  
print("Male Data Head:\n", male_data.head())  
print("Female Data Head:\n", female_data.head())  

# Print the column names before normalization  
print("Male Data Columns (Before):", male_data.columns.tolist())  
print("Female Data Columns (Before):", female_data.columns.tolist())  

# Normalize column names by stripping any leading/trailing whitespace  
male_data.columns = male_data.columns.str.strip()  
female_data.columns = female_data.columns.str.strip()  

# Print normalized column names to check  
print("Male Data Columns (After):", male_data.columns.tolist())  
print("Female Data Columns (After):", female_data.columns.tolist())  

# We have successfully loaded the datasets for adult males and females.   
# Each dataset contains various body measurements, including weight, height, and circumferences.   

# 2. Converting Data to Numpy Matrices  
# Ensure that required columns exist in the loaded data  
expected_columns = ['Weight', 'Height', 'Upper_arm_length', 'Upper_leg_length', 'Arm_circumference', 'Hip_circumference', 'Waist_circumference']  

# Identify missing columns in each dataset  
missing_male_columns = [col for col in expected_columns if col not in male_data.columns]  
missing_female_columns = [col for col in expected_columns if col not in female_data.columns]  

# Print missing columns if any  
if missing_male_columns:  
    print("Missing columns in male dataset:", missing_male_columns)  

if missing_female_columns:  
    print("Missing columns in female dataset:", missing_female_columns)  

# Check if any of the expected columns are not found and handle it gracefully  
if not missing_male_columns and not missing_female_columns:  
    female = female_data[expected_columns].to_numpy()  
    male = male_data[expected_columns].to_numpy()  
else:  
    # Display the actual columns for debugging  
    print("Actual Male Data Columns:", male_data.columns.tolist())  
    print("Actual Female Data Columns:", female_data.columns.tolist())  
    raise ValueError("Expected columns not found in one or both datasets.")  

# 3. Plotting Histograms for Weights  
# We will plot histograms of the weights for females and males side by side.  

# Extracting weights  
female_weights = female[:, 0]  
male_weights = male[:, 0]  

# Plotting histograms  
plt.figure(figsize=(10, 8))  

# Female weight histogram  
plt.subplot(2, 1, 1)  
plt.hist(female_weights, bins=30, color='pink', alpha=0.7)  
plt.title('Female Weights Distribution')  
plt.xlabel('Weight (kg)')  
plt.ylabel('Frequency')  
plt.xlim(40, 150)  

# Male weight histogram  
plt.subplot(2, 1, 2)  
plt.hist(male_weights, bins=30, color='lightblue', alpha=0.7)  
plt.title('Male Weights Distribution')  
plt.xlabel('Weight (kg)')  
plt.ylabel('Frequency')  
plt.xlim(40, 150)  

plt.tight_layout()  
plt.show()  

# 4. Box-and-Whisker Plot for Weights  
# Next, we’ll create a box-and-whisker plot to compare the male and female weights.  
plt.figure(figsize=(8, 6))  
plt.boxplot([female_weights, male_weights], labels=['Females', 'Males'])  
plt.title('Box-and-Whisker Plot of Weights')  
plt.ylabel('Weight (kg)')  
plt.show()  

# 5. Numerical Aggregates for Weights  
female_stats = {  
    'mean': np.mean(female_weights),  
    'median': np.median(female_weights),  
    'std_dev': np.std(female_weights),  
    'min': np.min(female_weights),  
    'max': np.max(female_weights)  
}  

male_stats = {  
    'mean': np.mean(male_weights),  
    'median': np.median(male_weights),  
    'std_dev': np.std(male_weights),  
    'min': np.min(male_weights),  
    'max': np.max(male_weights)  
}  

# Output the calculated statistics  
print("Female Statistics:", female_stats)  
print("Male Statistics:", male_stats)
