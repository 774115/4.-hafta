import csv
import matplotlib.pyplot as plt

def gorsellestir():
    musteri_list = []
    para_list = []
    
    try:
        with open("data.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                musteri_list.append(int(row["Gelen Musteri"]))
                para_list.append(int(row["Gelen Para"]))
    except FileNotFoundError:
        print("Hata: data.csv dosyası bulunamadı. Lütfen önce veri_olusturici.py'yi çalıştırın.")
        return

    # Figür boyutu ayarla
    plt.figure(figsize=(12, 5))

    # 1. Alt grafik: Gelen Müşteri Dağılımı
    plt.subplot(1, 2, 1)
    plt.hist(musteri_list, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Gelen Müşteri Dağılımı")
    plt.xlabel("Müşteri Sayısı")
    plt.ylabel("Frekans (Gün Sayısı / Kişi)")

    # 2. Alt grafik: Gelen Para Dağılımı
    plt.subplot(1, 2, 2)
    plt.hist(para_list, bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
    plt.title("Gelen Para Dağılımı")
    plt.xlabel("Para Tutarı")
    plt.ylabel("Frekans")

    plt.tight_layout()
    
    # Görseli kaydet
    plt.savefig("gorsel.png")
    print("Grafik 'gorsel.png' olarak klasöre kaydedildi.")
    
    # Etkileşimli bir pencerede açmak isterseniz aşağıdaki yorum satırını kaldırabilirsiniz:
    # plt.show()

if __name__ == "__main__":
    gorsellestir()
