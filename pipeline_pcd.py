# -- FUNGSI FILE --
# fungsi file untuk memberikan visual pipeline (Citra Asli + Grayscale + Filtering + ROI/Segmentasi + Histogram + Edge Detection + Morfologi) 

import cv2
import os

# folder input (data yang sudah di augmentasi) dan folder hasil pipeline
input_base = 'dataset_output'
pipeline_base = 'dataset_pipeline'
categories = ['Mata_Normal', 'Mata_Katarak']

if not os.path.exists(pipeline_base):
    os.makedirs(pipeline_base)

for category in categories:
    path = os.path.join(input_base, category)
    save_path = os.path.join(pipeline_base, category)
    if not os.path.exists(save_path): os.makedirs(save_path)
    
    print(f"Sedang memproses Visual Pipeline: {category}...")
    
    # proses semua 200 foto per kategori
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path, filename))
        if img is None: continue
        
        # 1. Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 2. Histogram Equalization 
        equ = cv2.equalizeHist(gray)
        
        # 3. Edge Detection 
        edges = cv2.Canny(equ, 100, 200)
        
        # Simpan hasil 
        cv2.imwrite(os.path.join(save_path, f"gray_{filename}"), gray)
        cv2.imwrite(os.path.join(save_path, f"equ_{filename}"), equ)
        cv2.imwrite(os.path.join(save_path, f"edge_{filename}"), edges)

print("Visual Pipeline Selesai! Cek folder 'dataset_pipeline'.")
