# Deteksi Katarak Berbasis Pengolahan Citra Digital (PCD)

Proyek ini bertujuan untuk meningkatkan akurasi deteksi katarak menggunakan analisis tekstur (GLCM) dan augmentasi data, melampaui standar penelitian sebelumnya (78%) menjadi **85%**.

## Fitur Utama
- **Augmentasi Data**: Memperluas dataset dari 100 menjadi 400 citra.
- **Preprocessing**: Histogram Equalization & Canny Edge Detection.
- **Ekstraksi Ciri**: Morfologi (Luas/Keliling) & Tekstur (GLCM).
- **Klasifikasi**: XGBoost Classifier.

## Cara Menjalankan
1. Instal library: `pip install -r requirements.txt`
2. Jalankan seluruh proses: `python main.py`

## Hasil
- Akurasi Sistem: **85.00%**
- Lokasi Penelitian: Universitas Katholik Santo Thomas Medan.