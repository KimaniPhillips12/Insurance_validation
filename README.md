# 📊 Insurance Charges Data Cleaning & Modeling Project

## Overview
This project involves cleaning and preprocessing a dataset to prepare it for analysis and predictive modeling. The goal is to understand the factors influencing medical insurance charges and build a linear regression model to predict these charges.

## 🧼 Data Cleaning & Preprocessing

### 1. Initial Inspection
- Displayed the first five rows of the dataset to understand its structure and contents.

### 2. Dataset Dimensions
- Checked the number of rows and columns to understand the size of the dataset.

### 3. Handling Missing Values
- Removed rows with missing values to ensure data integrity.
- Verified that no missing values remain in the dataset.

### 4. Standardizing Categorical Data
- Standardized the categories in the `region` column to ensure consistency.
- Simplified the `sex` column to just two categories: `male` and `female`.

### 5. Boolean Conversion
- Converted the `smoker` column to boolean values (`True` for smokers, `False` for non-smokers).

### 6. Data Type Standardization
- Ensured the `charges` column is of float type for accurate numerical analysis.

## 📈 Exploratory Data Analysis

### 7. Relationships Between Variables & Charges
- Created scatterplots to visualize relationships between `charges` and each feature variable.
- Identified trends and potential outliers that may influence model performance.

## 🤖 Linear Regression Modeling

### 8. Model Development
- Built a Linear Regression model to predict medical insurance charges based on cleaned features.

### 9. Model Evaluation
- Assessed model performance using:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R² Score (coefficient of determination)

### 10. Feature Importance
- Extracted and sorted model coefficients to understand the impact of each feature on predicted charges.

---

This cleaned and analyzed dataset is now ready for further exploration, visualization, and advanced modeling.


   
