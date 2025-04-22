# index.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# 1. Load dataset
df = pd.read_csv("QS World University Rankings 2025 (Top global universities).csv", encoding='ISO-8859-1')

# 2. Tampilkan info dasar
print("Jumlah baris dan kolom:", df.shape)
print("\nInformasi dataset:")
print(df.info())
print("\nStatistik deskriptif:")
print(df.describe(include='all'))
print("\nMissing value per kolom:")
print(df.isnull().sum())

# 3. Visualisasi missing value
msno.matrix(df)
plt.title("Visualisasi Missing Values")
plt.show()

# 4. Ubah RANK_2025 menjadi angka (jika memungkinkan)
def extract_numeric_rank(rank):
    try:
        return int(rank)
    except:
        return None  # untuk nilai seperti '701+' atau '1201-1400'

df['RANK_2025_NUM'] = df['RANK_2025'].apply(extract_numeric_rank)

# 5. Filter 10 besar universitas
top_10 = df[df['RANK_2025_NUM'].notnull()].sort_values(by='RANK_2025_NUM').head(10)
print("\n10 Besar Universitas Tahun 2025:")
print(top_10[['RANK_2025', 'Institution_Name', 'Location', 'Academic_Reputation_Score']])

# 6. Visualisasi 10 besar berdasarkan skor reputasi akademik
plt.figure(figsize=(12,6))
sns.barplot(
    data=top_10,
    x='Academic_Reputation_Score',
    y='Institution_Name',
    hue='Institution_Name',
    palette='viridis',
    legend=False
)
plt.title('Top 10 Universitas berdasarkan Academic Reputation Score (2025)')
plt.xlabel('Academic Reputation Score')
plt.ylabel('University')
plt.tight_layout()
plt.show()


# 7. Distribusi nilai rank numerik (jika ingin lihat semua)
plt.figure(figsize=(10,5))
sns.histplot(df['RANK_2025_NUM'].dropna(), bins=50, kde=True, color='skyblue')
plt.title("Distribusi Ranking 2025 (Numerik)")
plt.xlabel("Rank")
plt.ylabel("Jumlah Universitas")
plt.tight_layout()
plt.show()
