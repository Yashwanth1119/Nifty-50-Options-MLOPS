# pipeline/model_training.py

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import os

def train_and_save_model(X, y, model_path="artifacts/nifty_rf_model.joblib", scaler_path="artifacts/scaler.joblib"):
    # 🔀 Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 🧼 Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 🧠 Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # ✅ Evaluate
    y_pred = model.predict(X_test_scaled)
    print("📊 Classification Report:\n", classification_report(y_test, y_pred))

    # 💾 Save
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

    print(f"✅ Model saved to: {model_path}")
    return model, scaler
