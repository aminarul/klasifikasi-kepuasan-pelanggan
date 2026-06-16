import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# =====================
# BACA DATASET
# =====================
df = pd.read_csv("train.csv")

# =====================
# HAPUS KOLOM TIDAK DIPERLUKAN
# =====================
df.drop(columns=["Unnamed: 0", "id"], inplace=True, errors="ignore")

# =====================
# TANGANI MISSING VALUE
# =====================
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# =====================
# ENCODING DATA KATEGORI
# =====================
encoders = {}

for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# =====================
# FITUR DAN TARGET
# =====================
X = df.drop("satisfaction", axis=1)
y = df["satisfaction"]

# =====================
# SPLIT DATA
# =====================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Jumlah Data Training :", X_train.shape)
print("Jumlah Data Testing  :", X_test.shape)

# =====================
# MODEL NAIVE BAYES
# =====================
model = GaussianNB()

# Training
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# =====================
# EVALUASI
# =====================
accuracy = accuracy_score(y_test, y_pred)

print("\n" + "="*50)
print("HASIL EVALUASI MODEL")
print("="*50)

print(f"Akurasi : {accuracy*100:.2f}%")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# =====================
# SIMPAN MODEL
# =====================
pickle.dump(model, open("model.pkl", "wb"))

print("\nModel berhasil disimpan sebagai model.pkl")
print("Jumlah fitur:", len(X.columns))
print(X.columns.tolist())