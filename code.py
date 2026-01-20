import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler


# 1. Load Dataset
df = pd.read_csv("data/adult.csv")

# 2. Handle Missing Values
df.replace(" ?", pd.NA, inplace=True)
df.dropna(inplace=True)

print("Dataset loaded and cleaned.\n")

# 3. Identify Features
categorical_features = df.select_dtypes(include=['object']).columns.tolist()
numerical_features = df.select_dtypes(exclude=['object']).columns.tolist()

print("Categorical Features:", categorical_features)
print("Numerical Features:", numerical_features, "\n")

# 4. Label Encoding (Target Variable)
le = LabelEncoder()
df['income'] = le.fit_transform(df['income'])

print("Label Encoding applied on 'income'.\n")


# 5. One-Hot Encoding
df_encoded = pd.get_dummies(df, drop_first=True)

print("One-Hot Encoding completed.\n")


# 6. VISUALIZATION BEFORE SCALING
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_encoded[numerical_features])
plt.title("Numerical Features BEFORE Scaling")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Scaling Numerical Features
scaler = StandardScaler()
df_encoded[numerical_features] = scaler.fit_transform(
    df_encoded[numerical_features]
)

print("Standard Scaling applied.\n")

# 8. VISUALIZATION AFTER SCALING
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_encoded[numerical_features])
plt.title("Numerical Features AFTER Scaling")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Save Processed Datase
df_encoded.to_csv("data/adult_processed.csv", index=False)

print("Preprocessing completed successfully!")
print("Processed dataset saved as 'adult_processed.csv'")
