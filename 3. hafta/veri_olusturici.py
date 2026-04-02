import csv
import random

def generate_data():
    data = []
    # Sütun başlıkları
    data.append(["ID", "Gelen Musteri", "Gelen Para"])
    
    for i in range(1, 501):
        # Gelen müşteri için normal dağılım (Ortalama: 100.5, Standart Sapma: 33.16)
        musteri = int(random.gauss(100.5, 33.16))
        # Değerlerin 1 ile 200 arasında kalmasını sağlıyoruz
        musteri = max(1, min(200, musteri))
        
        # Gelen para için normal dağılım (Ortalama: 17500, Standart Sapma: 4166.67)
        para = int(random.gauss(17500, 4166.67))
        # Değerlerin 5000 ile 30000 arasında kalmasını sağlıyoruz
        para = max(5000, min(30000, para))
        
        data.append([i, musteri, para])
        
    # Verileri data.csv dosyasına yazma
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == "__main__":
    generate_data()
    print("data.csv başarıyla oluşturuldu.")
