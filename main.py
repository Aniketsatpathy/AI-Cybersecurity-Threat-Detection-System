# main.py

import os
import joblib
import pandas as pd

from src.data_preprocessing import load_data, clean_data, encode_data, scale_data
from src.feature_engineering import create_features
from src.model import train_isolation_forest, train_random_forest, save_model
from src.evaluate import evaluate
from src.predict import convert_iso_preds
from src.visualize import plot_distribution

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CREATE OUTPUT FOLDERS
# =========================
os.makedirs("data/preprocessed", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# =========================
# LOAD DATA
# =========================
train_df = load_data("data/raw/UNSW_NB15_training-set.csv")

print("Columns:", train_df.columns)

# =========================
# CLEAN DATA
# =========================
train_df = clean_data(train_df)

# =========================
# FEATURE ENGINEERING
# =========================
train_df = create_features(train_df)

# =========================
# SAVE PREPROCESSED DATA (🔥 NEW)
# =========================
train_df.to_csv("data/preprocessed/processed_data.csv", index=False)
print("✅ Saved preprocessed data")

# =========================
# SPLIT FEATURES & TARGET
# =========================
X = train_df.drop(columns=['label', 'attack_cat'], errors='ignore')
y = train_df['label']

# =========================
# ENCODE
# =========================
X, encoders = encode_data(X)

# =========================
# SAVE FEATURE ORDER
# =========================
feature_columns = X.columns.tolist()
joblib.dump(feature_columns, "models/feature_columns.pkl")

# =========================
# SCALE
# =========================
X_scaled, scaler = scale_data(X)

# =========================
# SAVE PREPROCESSING
# =========================
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(encoders, "models/encoders.pkl")

# =========================
# TRAIN-TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# =========================
# TRAIN MODELS
# =========================
print("\n🔷 Training Isolation Forest...")
iso_model = train_isolation_forest(X_train)

print("🔷 Training Random Forest...")
rf_model = train_random_forest(X_train, y_train)

# =========================
# SAVE MODELS
# =========================
save_model(iso_model, "models/isolation_forest.pkl")
save_model(rf_model, "models/random_forest.pkl")

# =========================
# EVALUATE
# =========================
print("\n🔷 Isolation Forest (Test):")
iso_preds = convert_iso_preds(iso_model.predict(X_test))

iso_report = classification_report(y_test, iso_preds)
print(iso_report)

# Save report
with open("outputs/isolation_report.txt", "w") as f:
    f.write(iso_report)

print("\n🔷 Random Forest (Test):")
rf_preds = rf_model.predict(X_test)

rf_report = classification_report(y_test, rf_preds)
print(rf_report)

with open("outputs/random_forest_report.txt", "w") as f:
    f.write(rf_report)

# =========================
# CONFUSION MATRIX (SAVE IMAGE)
# =========================
cm = confusion_matrix(y_test, rf_preds)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.savefig("outputs/confusion_matrix.png")
plt.close()

print("✅ Saved confusion matrix")

# =========================
# DISTRIBUTION GRAPH (SAVE IMAGE)
# =========================
plt.figure()
sns.countplot(x=iso_preds)
plt.title("Anomaly Distribution")
plt.savefig("outputs/anomaly_distribution.png")
plt.close()

print("✅ Saved anomaly distribution graph")

# =========================
# VISUALIZATION (OPTIONAL DISPLAY)
# =========================
plot_distribution(iso_preds)

print("\n✅ Training Complete")