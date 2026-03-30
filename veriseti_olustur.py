import csv
import random
import matplotlib.pyplot as plt

# 1. Rastgele Normal Dağılımlı Veri Üretimi
# En az 500 satır (n=1000 kullanıyoruz)
n = 1000

# Lise türleri (Kategorik renk katmak için)
liseler = ["Anadolu Lisesi", "Fen Lisesi", "Meslek Lisesi", "İmam Hatip Lisesi", "Özel Lise"]

veri_seti = []
for _ in range(n):
    # Değişken 1: YKS Puanı (Ortalama=320, Standart Sapma=45)
    # Maksimum 500, minimum 100 civarı puanlar
    yks_puani = int(random.gauss(320, 45))
    if yks_puani > 500: yks_puani = 500
    if yks_puani < 100: yks_puani = 100
    
    # Değişken 2: Diploma Notu (OBP) (Ortalama=78, Standart Sapma=12)
    # Maksimum 100, minimum 50
    diploma_notu = round(random.gauss(78, 12), 1)
    if diploma_notu > 100: diploma_notu = 100
    if diploma_notu < 50: diploma_notu = 50

    # Lise türü seçimi (Rastgele)
    lise_turu = random.choices(liseler, weights=[45, 10, 20, 15, 10], k=1)[0]
    
    veri_seti.append([yks_puani, diploma_notu, lise_turu])

# 2. CSV Dosyasına Yazma
csv_dosya = "yks_ve_liseler_veriseti.csv"
with open(csv_dosya, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['YKS_Puani', 'Diploma_Notu_OBP', 'Lise_Turu']) 
    writer.writerows(veri_seti)

print(f"'{csv_dosya}' adlı CSV dosyası başarıyla oluşturuldu ve {n} öğrenci eklendi.")

# 3. Matplotlib ile Görselleştirme
yks_verileri = [satir[0] for satir in veri_seti]
diploma_verileri = [satir[1] for satir in veri_seti]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Öğrenci Sınav Performansı - Normal Dağılım Çan Eğrisi', fontsize=16)

# YKS Puanı Histogramı
ax1.hist(yks_verileri, bins=35, color='#8b5cf6', edgecolor='black', alpha=0.8)
ax1.set_title('YKS Puanı Dağılımı', fontsize=13)
ax1.set_xlabel('YKS Puanı (100 - 500)')
ax1.set_ylabel('Öğrenci Sayısı')
ax1.grid(axis='y', alpha=0.3)

# Diploma Notu Histogramı
ax2.hist(diploma_verileri, bins=30, color='#f43f5e', edgecolor='black', alpha=0.8)
ax2.set_title('Diploma Notu (OBP) Dağılımı', fontsize=13)
ax2.set_xlabel('Diploma Notu (50 - 100)')
ax2.set_ylabel('Öğrenci Sayısı')
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()

# Grafiği resim olarak kaydetme
grafik_dosya = "yks_dagilim_grafigi.png"
plt.savefig(grafik_dosya)
print(f"Grafik '{grafik_dosya}' olarak kaydedildi.")

