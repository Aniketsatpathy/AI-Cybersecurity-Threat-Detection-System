from src.data_preprocessing import load_data, clean_data, encode_data, scale_data
from src.feature_engineering import create_features
from src.model import load_model
from src.predict import convert_iso_preds

# LOAD TEST DATA
df = load_data("data/raw/UNSW_NB15_testing-set.csv")

df = clean_data(df)
df = create_features(df)

X = df.drop(columns=['Label'])
y = df['Label']

X, _ = encode_data(X)
X_scaled, _ = scale_data(X)

model = load_model("models/isolation_forest.pkl")

preds = model.predict(X_scaled)
preds = convert_iso_preds(preds)

print("Sample Predictions:", preds[:10])