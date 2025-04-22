# 📊 Exploratory Data Analysis: QS World University Rankings 2025

## 👤 Identitas
- **Nama**: Fitri Anisa  
- **NPM**: 20123020  
- **Kelas**: 1AI4UTD  
- **Mata Kuliah**: Kecerdasan Buatan (AI)  
- **Dosen**: Kodrat Mahatma  

---

## 📁 Dataset
Dataset digunakan dari Kaggle:  
[QS World University Rankings 2025](https://www.kaggle.com/datasets/melissamonfared/qs-world-university-rankings-2025)

---

## 🎯 Tujuan
Melakukan **Exploratory Data Analysis (EDA)** terhadap peringkat universitas dunia tahun 2025 yang disediakan oleh QS Rankings. Tujuan analisis ini meliputi:
- Menemukan insight awal dari data peringkat universitas
- Menganalisis 10 besar universitas terbaik dunia
- Menjelaskan distribusi nilai peringkat dan skor reputasi akademik
- Menangani missing value dan konversi data non-numerik

---

## 🧪 Langkah EDA
1. **Data Loading**: Membaca file CSV dengan encoding `ISO-8859-1`
2. **Cleaning**: Menangani kolom `RANK_2025` yang bertipe object dan mengandung interval (`701+`, `1201-1400`)
3. **Feature Engineering**: Menambahkan kolom `RANK_2025_NUM` untuk versi numerik peringkat
4. **Handling Missing Values**: Visualisasi missing values menggunakan `missingno`
5. **Data Visualization**:
   - Barplot Top 10 Universitas berdasarkan `Academic_Reputation_Score`
   - Histogram distribusi `RANK_2025_NUM`
6. **Statistik Deskriptif & Insight**

---

## 📊 Tools & Library
- Python
- pandas
- seaborn
- matplotlib
- missingno

---

## 📌 Hasil Utama
- Universitas terbaik didominasi oleh institusi dari AS dan Inggris
- Skor reputasi akademik merupakan indikator dominan di 10 besar
- Banyak data peringkat tidak bisa dianalisis secara numerik karena bentuknya interval

---

## 📄 Laporan
Laporan lengkap tersedia di file `Laporan_EDA_Fitri_Anisa_20123020.docx`

---

## 💡 Rekomendasi Lanjutan
Dataset ini cocok untuk dikembangkan menjadi:
- Klasifikasi universitas berdasarkan ranking
- Clustering performa universitas
- Visualisasi interaktif untuk masing-masing region

---

## 📬 Kontak
Jika ada pertanyaan atau diskusi, silakan kontak melalui GitHub issue atau email.


