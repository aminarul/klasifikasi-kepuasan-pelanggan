<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Naive%20Bayes-blue">
  <img src="https://img.shields.io/badge/Accuracy-86.57%25-green">
  <img src="https://img.shields.io/badge/Deployment-Streamlit-red">
</p>
# ✈️ Klasifikasi Tingkat Kepuasan Pelanggan Menggunakan Naive Bayes

## 📌 Deskripsi Proyek

Proyek Machine Learning ini bertujuan untuk mengklasifikasikan tingkat kepuasan pelanggan maskapai penerbangan menggunakan algoritma **Gaussian Naive Bayes** dengan pendekatan **CRISP-DM (Cross Industry Standard Process for Data Mining)**.

Model yang dibangun mampu memprediksi apakah pelanggan termasuk kategori **Satisfied (Puas)** atau **Neutral/Dissatisfied (Tidak Puas)** berdasarkan berbagai aspek layanan penerbangan.

---

## 🎯 Tujuan Proyek

* Mengembangkan model klasifikasi kepuasan pelanggan.
* Mengukur performa model menggunakan metrik evaluasi.
* Mengimplementasikan model ke dalam aplikasi web menggunakan Streamlit.

---

## 🏢 Business Understanding

Kepuasan pelanggan merupakan indikator penting dalam menilai kualitas layanan perusahaan. Pelanggan yang puas cenderung memberikan ulasan positif dan melakukan pembelian ulang.

Target klasifikasi:

| Kelas                | Keterangan           |
| -------------------- | -------------------- |
| Satisfied            | Pelanggan Puas       |
| Neutral/Dissatisfied | Pelanggan Tidak Puas |

---

## 📊 Data Understanding

Dataset yang digunakan adalah **Airline Passenger Satisfaction Dataset**.

### Informasi Dataset

| Informasi        | Nilai   |
| ---------------- | ------- |
| Jumlah Data      | 103.904 |
| Jumlah Atribut   | 25      |
| Data Numerik     | 20      |
| Data Kategorikal | 5       |

### Fitur yang Digunakan

* Gender
* Customer Type
* Age
* Type of Travel
* Class
* Flight Distance
* Online Boarding
* Seat Comfort
* Inflight Entertainment
* Cleanliness
* Departure Delay
* Arrival Delay
* Inflight Wifi Service

### Target Variable

**Satisfaction**

* Satisfied
* Neutral or Dissatisfied

### Missing Value

Ditemukan 310 data kosong pada atribut:

* Arrival Delay in Minutes

---

## 🛠 Data Preparation

### Penghapusan Kolom

Kolom yang tidak digunakan:

* Unnamed: 0
* id

### Penanganan Missing Value

* Data numerik → Median
* Data kategorikal → Modus

### Label Encoding

Dilakukan pada:

* Gender
* Customer Type
* Type of Travel
* Class
* Satisfaction

### Pembagian Dataset

| Dataset  | Jumlah Data |
| -------- | ----------- |
| Training | 83.123      |
| Testing  | 20.781      |

Jumlah fitur yang digunakan: **22 fitur**

---

## 🤖 Modeling

Algoritma yang digunakan:

### Gaussian Naive Bayes

Alasan pemilihan:

* Mudah diimplementasikan
* Cepat dalam proses training
* Cocok untuk data numerik

### Waktu Training

```text
0.04 detik
```

---

## 📈 Evaluation

### Accuracy Score

```text
86.57%
```

### Confusion Matrix

| Aktual     | Prediksi Tidak Puas | Prediksi Puas |
| ---------- | ------------------- | ------------- |
| Tidak Puas | 10.544              | 1.169         |
| Puas       | 1.622               | 7.446         |

### Interpretasi

✅ 10.544 pelanggan tidak puas berhasil diprediksi dengan benar.

✅ 7.446 pelanggan puas berhasil diprediksi dengan benar.

❌ 1.169 pelanggan tidak puas diprediksi sebagai puas.

❌ 1.622 pelanggan puas diprediksi sebagai tidak puas.

---

## 📋 Classification Report

              precision    recall  f1-score   support

           0       0.87      0.90      0.88     11713
           1       0.86      0.82      0.84      9068

    accuracy                           0.87     20781
   macro avg       0.87      0.86      0.86     20781
weighted avg       0.87      0.87      0.87     20781

---

## 🚀 Deployment

Model telah diimplementasikan menggunakan:

* Python
* Scikit-Learn
* Streamlit

Aplikasi dapat melakukan prediksi kepuasan pelanggan secara real-time melalui antarmuka web.

---
Aplikasi web memungkinkan pengguna melakukan prediksi tingkat kepuasan pelanggan secara real-time berdasarkan data layanan penerbangan yang dimasukkan.

### 🌐 Demo Aplikasi

🔗 **Live Demo:**

https://klasifikasi-kepuasan-pelanggan-dwvwghhtkyzqgy2b5ccbzr.streamlit.app/

## 🏆 Hasil Akhir

| Metrik        | Nilai                |
| ------------- | -------------------- |
| Accuracy      | 86.57%               |
| Training Data | 83.123               |
| Testing Data  | 20.781               |
| Algoritma     | Gaussian Naive Bayes |

---

## 📝 Kesimpulan

Penelitian berhasil menerapkan algoritma Gaussian Naive Bayes untuk mengklasifikasikan tingkat kepuasan pelanggan pada Airline Passenger Satisfaction Dataset.

Model yang dibangun memperoleh akurasi sebesar **86.57%** dan berhasil diimplementasikan ke dalam aplikasi berbasis Streamlit sehingga dapat digunakan untuk prediksi secara real-time.

Hasil ini menunjukkan bahwa Gaussian Naive Bayes merupakan metode yang sederhana namun efektif dalam membantu analisis kepuasan pelanggan berdasarkan data layanan penerbangan.
