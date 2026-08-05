# --- FUNGSI FILE ----
# File khusus melakukan ekstraksi ciri terhadap morfologi & tekstur 

import cv2
import os
import csv
import numpy as np
from skimage.feature import graycomatrix, graycoprops

input_base = 'dataset_pipeline'
categories = ['Mata_Normal', 'Mata_Katarak']
hasil_csv = 'hasil_ekstraksi_ciri.csv'

header = ['Nama_File', 'Kategori', 'Luas', 'Kontras', 'Homogenitas']

with open(hasil_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for category in categories:
        path = os.path.join(input_base, category)
        print(f"Ekstraksi Tekstur & Morfologi: {category}...")
        for filename in os.listdir(path):
            if not filename.startswith('equ_'): continue 
            
            img = cv2.imread(os.path.join(path, filename), 0)
            if img is None: continue
            
            # Morfologi (Luas)
            area = cv2.countNonZero(cv2.Canny(img, 100, 200))
            
            # Tekstur (GLCM)
            glcm = graycomatrix(img, [1], [0], 256, symmetric=True, normed=True)
            contrast = graycoprops(glcm, 'contrast')[0, 0]
            homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
            
            writer.writerow([filename, category, area, round(contrast, 2), round(homogeneity, 2)])

print("Selesai! Data tekstur sudah siap.")
