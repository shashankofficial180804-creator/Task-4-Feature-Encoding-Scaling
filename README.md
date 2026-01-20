# Task-4-Feature-Encoding-Scaling
Feature engineering project using Adult Income Dataset. Includes label encoding, one-hot encoding, feature scaling with StandardScaler, and dataset preprocessing to improve ML model readiness. Completed as part of AI &amp; ML Internship Task 4.

📌 Project Overview

This project demonstrates essential feature engineering techniques used in machine learning. Using the Adult Income Dataset, categorical and numerical features are processed through encoding and scaling to make the dataset suitable for ML algorithms.
This task was completed as part of an AI & ML Internship (Task 4).

🎯 Objectives
	•	Identify categorical and numerical features
	•	Apply Label Encoding where order exists
	•	Apply One-Hot Encoding where order does not exist
	•	Scale numerical features using StandardScaler
	•	Visually compare data before and after scaling
	•	Save a fully preprocessed, ML-ready dataset

🧰 Tools & Libraries Used
	•	Python
	•	Pandas
	•	Scikit-learn
	•	Matplotlib
	•	Seaborn

🔄 Steps Performed:
1️⃣ Data Loading & Cleaning
	•	Loaded Adult Income dataset
	•	Handled missing values by removing invalid entries

2️⃣ Feature Identification
	•	Categorical features identified using data types
	•	Numerical features separated for scaling

3️⃣ Label Encoding
	•	Applied to the target variable income
	•	Converts income categories into numerical labels

4️⃣ One-Hot Encoding
	•	Applied to categorical features without ordinal relationship
	•	Prevents misleading numerical ordering

5️⃣ Feature Scaling
	•	Numerical features scaled using StandardScaler
	•	Ensures all features have mean ≈ 0 and standard deviation ≈ 1

6️⃣ Visual Comparison
	•	Boxplots created to compare:
	•	Before scaling
	•	After scaling
	•	Clearly shows normalization effect

7️⃣ Dataset Export
	•	Final preprocessed dataset saved as adult_processed.csv

📊 Why Scaling is Important-
Feature scaling improves performance of algorithms such as:
	•	K-Nearest Neighbors (KNN)
	•	Support Vector Machines (SVM)
	•	Logistic Regression
	•	Linear Regression
	•	Neural Networks

✅ Final Outcome
	•	Dataset converted into ML-ready numerical format
	•	Clear understanding of feature engineering concepts
	•	Visual and statistical proof of scaling impact


🏁 Conclusion:
This project provides hands-on experience with real-world data preprocessing techniques that are critical in machine learning pipelines. It strengthens understanding of how encoding and scaling directly influence model performance
