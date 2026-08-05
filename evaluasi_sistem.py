# --- FUNGSI FILE ----
# File khusus melakukan evaluasi dari hasil program 

import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load data hasil ekstraksi ciri
df = pd.read_csv('hasil_ekstraksi_ciri.csv')

# Ubah kategori jadi angka (0: Normal, 1: Katarak) agar XGBoost bisa memprosesnya
df['Kategori_Num'] = df['Kategori'].map({'Mata_Normal': 0, 'Mata_Katarak': 1})

X = df[['Luas', 'Kontras', 'Homogenitas']]
y = df['Kategori_Num']

# Hitung statistik , dimana hasilnya akan ditampilkan pada terminal 
mean_normal = df[df['Kategori'] == 'Mata_Normal']['Luas'].mean()
mean_katarak = df[df['Kategori'] == 'Mata_Katarak']['Luas'].mean()
threshold = (mean_normal + mean_katarak) / 2

# Bagi data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

# Konfigurasi Model XGBoost (Hyperparameter Tuning)
model = XGBClassifier(
    n_estimators=1000, 
    learning_rate=0.01, 
    max_depth=6, 
    use_label_encoder=False, 
    eval_metric='logloss'
)
model.fit(X_train, y_train)

# Prediksi hasil terhadap data uji
y_pred = model.predict(X_test)

# Hitung akurasi akhir
akurasi = accuracy_score(y_test, y_pred) * 100

# --- OUTPUT TERMINAL ---
print("\n--- HASIL OPTIMASI ---")
print(f"Rata-rata Luas Normal: {mean_normal:.2f}")
print(f"Rata-rata Luas Katarak: {mean_katarak:.2f}")
print(f"Threshold Pemisah: {threshold:.2f}")
print(f"Akurasi Sistem Baru: {akurasi:.2f}%")
print("-----------------------\n")

# Visualisasi grafik perbandingan akurasi 
# Note : Pada dasarnya ini saya gunakan dalam penelitian
#        yang saya bandingkan dengan penelitian terdahulu
metode = ['Jurnal Rujukan (78%)', 'Sistem Katarak (Baru)'] 
skor = [78, akurasi]

plt.figure(figsize=(8,5))
plt.bar(metode, skor, color=['red', 'blue'])
plt.ylabel('Akurasi (%)')
plt.title('HASIL AKHIR PENELITIAN: Perbandingan Akurasi')
plt.ylim(0, 100)

# Menambahkan label angka di atas batang grafik
for i, v in enumerate(skor):
    plt.text(i, v + 2, f"{v:.1f}%", ha='center', fontweight='bold')

# Menyimpan hasil perbandingan akurasi dari jurnal & penelitian
plt.savefig('hasil_final_jurnal.png')
print("Grafik perbandingan berhasil disimpan: hasil_final_jurnal.png")
plt.show()

# Visualisasi Confusion Matrix dengan label lengkap
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8,6))

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Prediksi Normal', 'Prediksi Katarak'],
            yticklabels=['Asli Normal', 'Asli Katarak'])

plt.title(f'Confusion Matrix (Akurasi: {akurasi:.2f}%)')
plt.xlabel('Hasil Prediksi Sistem')
plt.ylabel('Kenyataan (Ground Truth)')

# Simpan hasil Confusion Matrix
plt.savefig('cm_final_berlabel.png')
print("Confusion Matrix berlabel berhasil disimpan: cm_final_berlabel.png")
plt.show()
