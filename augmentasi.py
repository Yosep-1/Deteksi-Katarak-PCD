# -- FUNGSI FILE ---
# File khusus melakukan augmentasi data asli (mata normal + mata katarak)

import cv2
import os

# konfigurasi Folder yang dibagi dalam dua kategori 
input_base = 'dataset_asli'
output_base = 'dataset_output'
categories = ['Mata_Normal', 'Mata_Katarak']

if not os.path.exists(output_base):
    os.makedirs(output_base)

for category in categories:
    path = os.path.join(input_base, category)
    save_path = os.path.join(output_base, category)
    if not os.path.exists(save_path): os.makedirs(save_path)
    
    print(f"Sedang menduplikasi data: {category}...")
    
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path, filename))
        if img is None: continue
        
        # Simpan Foto Asli ke folder output
        cv2.imwrite(os.path.join(save_path, f"asli_{filename}"), img)
        
        # Augmentasi: Flip Horizontal (Cermin)
        flip_h = cv2.flip(img, 1)
        cv2.imwrite(os.path.join(save_path, f"aug_flip_{filename}"), flip_h)
        
        # Augmentasi: Rotasi 90 Derajat
        rot_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(save_path, f"aug_rot_{filename}"), rot_90)
        
        # Augmentasi: Penyesuaian Kecerahan (Brightness)
        bright = cv2.convertScaleAbs(img, alpha=1.2, beta=30)
        cv2.imwrite(os.path.join(save_path, f"aug_bright_{filename}"), bright)

print("Selesai! Sekarang cek folder 'dataset_output'.")
