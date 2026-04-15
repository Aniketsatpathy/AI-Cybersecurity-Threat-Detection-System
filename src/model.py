# src/model.py

from sklearn.ensemble import IsolationForest, RandomForestClassifier
import joblib

# 🔥 UPDATED: better contamination value
def train_isolation_forest(X):
    model = IsolationForest(
        contamination=0.15,   # was 0.05 → now improved
        random_state=42
    )
    model.fit(X)
    return model

def train_random_forest(X, y):
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X, y)
    return model

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)