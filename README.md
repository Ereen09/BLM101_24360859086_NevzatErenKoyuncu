# BLM101_24360859086_NevzatErenKoyuncu
# Run-Length Encoding (RLE) Sıkıştırma Aracı
## 📚 Öğrenci ve Proje Bilgileri
| Kategori | Bilgi |

| **Ders Kodu** | BLM101 |
| **Öğrenci Adı** | Nevzat Eren Koyuncu |
| **Öğrenci Numarası** | 24360859086 |
| **Proje Konusu** | Veri Depolama ve Sıkıştırma Algoritmaları |

### 📺 Proje Videosu
Projenin detaylı anlatımına ve demolarına aşağıdaki bağlantıdan ulaşabilirsiniz:
[YouTube Linki](https://youtu.be/QShotrIh_80?si=E8LmFk83dxQu6fqE)

***

## 📝 Proje Açıklaması
Bu Python kodu, basit ve kayıpsız bir veri sıkıştırma tekniği olan **Run-Length Encoding (RLE)** algoritmasını kullanarak metin verilerini sıkıştırmayı ve sıkıştırılmış veriyi orijinal haline geri çözmeyi amaçlar.

RLE, özellikle ardışık olarak tekrar eden karakter dizilerinin bulunduğu verilerde (örneğin basit grafikler, desenli metinler) yüksek verimlilik sağlar.

## ✨ Özellikler

* `encode`: Metni RLE formatına sıkıştırır.
* `decode`: RLE formatındaki metni orijinal haline geri çözer.
* `compression_ratio`: Sıkıştırma oranını yüzde olarak hesaplar ve sıkıştırma etkinliğini gösterir.
* `display_results`: Sıkıştırma/Çözme sonuçlarını, boyutları ve doğrulama durumunu düzenli bir tablo halinde görüntüler.
* Kullanıcı girişi olmadığında test amaçlı ön tanımlı örnek verileri kullanır.

## 🛠️ Kullanılan Kütüphaneler
Bu betik, standart Python kütüphaneleri dışında herhangi bir harici bağımlılık kullanmamaktadır.

* **Temel Python (v3.x):** String, döngü (`for`, `while`), koşullu ifadeler (`if/else`) ve temel matematiksel işlemler (uzunluk, bölme) kullanılmıştır.

## 🧠 Algoritma Mantığı: Run-Length Encoding (RLE) 
RLE (Çalışma Uzunluğu Kodlaması), ardışık olarak tekrar eden aynı veri değerlerinin (bir "çalışma") bir kez saklanıp, bu değerin kaç kez tekrar ettiğinin (çalışma uzunluğu) yanına yazılması prensibine dayanır.

### 1. Sıkıştırma (`encode` fonksiyonu)
Bu işlev, orijinal metni karakter karakter tarar ve ardışık tekrar eden karakter gruplarını sayar.

* Metin üzerinde tekrar eden bir karakter serisi bittiğinde (ya da metin sona erdiğinde),
* Serinin **tekrar sayısı** ve ardından **karakterin kendisi** sıkıştırılmış metne eklenir.

**Örnek Sıkıştırma:**
`"AAAAABBBCCDAA"` **:** `"5A3B2C1D2A"`

### 2. Çözme (`decode` fonksiyonu)
Bu işlev, RLE formatındaki sıkıştırılmış metni okur ve orijinal metni yeniden oluşturur.

* Metin üzerinde sırayla sayı ve ardından karakter beklenir.
* Önce bir veya daha fazla basamaktan oluşan sayı (tekrar sayısı) okunur.
* Ardından gelen karakter, okunan sayı kadar çözülmüş metne eklenir.

**Örnek Çözme:**
`"5A3B2C1D2A"` **= (5 * 'A') + (3 * 'B') + (2 * 'C') + (1 * 'D') + (2 * 'A') **=** `"AAAAABBBCCDAA"`

### 3. Sıkıştırma Oranı Hesaplama (`compression_ratio` fonksiyonu)
Sıkıştırmanın etkinliğini ölçmek için kullanılır.

* **Formül:** $Oran = \frac{\text{Orijinal Boyut} - \text{Sıkıştırılmış Boyut}}{\text{Orijinal Boyut}} \times 100$
* Bu algoritma, özellikle uzun ardışık tekrar eden karakter dizilerine sahip metinlerde yüksek sıkıştırma oranları sunar.
* Ancak, tekrar etmeyen rastgele metinlerde (örneğin, `"ABCD"` **:** `"1A1B1C1D"`) sıkıştırılmış dosya orijinalinden **daha büyük** olabilir.

## 🚀 Kullanım
Kod, Python yorumlayıcısında doğrudan çalıştırılabilir.

```bash
python dosya_adi.py
