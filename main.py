import os

def run_step(step_name, file_name):
    print(f"\n{'='*30}")
    print(f"MENJALANKAN: {step_name}")
    print(f"{'='*30}")
    os.system(f"python {file_name}")

if __name__ == "__main__":
    # Urutan proses penelitian Yosep
    run_step("1. Augmentasi Data (400 Citra)", "augmentasi.py")
    run_step("2. Visual Pipeline (Preprocessing)", "pipeline_pcd.py")
    run_step("3. Ekstraksi Ciri (Morfologi & Tekstur)", "ekstraksi_ciri.py")
    run_step("4. Evaluasi & Akurasi (XGBoost)", "evaluasi_sistem.py")
    
    print("\nPROSES SELESAI! Semua data dan grafik sudah siap di folder proyek.")