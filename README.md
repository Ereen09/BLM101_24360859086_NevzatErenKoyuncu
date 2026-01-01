# BLM101_24360859086_NevzatErenKoyuncu
Öğrenci Bilgileri: Nevzat Eren koyuncu  24360859086
o	Proje Konusu: Veri Depolama ve Sıkıştırma Algoritmaları 
o	YouTube Linki: https://youtu.be/QShotrIh_80?si=E8LmFk83dxQu6fqE


o	Proje Açıklaması: Run-Length Encoding (RLE) Sıkıştırma Aracı
Bu Python kodu, basit ve kayıpsız bir veri sıkıştırma tekniği olan Run-Length Encoding (RLE) algoritmasını kullanarak metin verilerini sıkıştırmayı ve sıkıştırılmış veriyi orijinal haline geri çözmeyi amaçlar.
 Özellikler
•	encode: Metni RLE formatına sıkıştırır.
•	decode: RLE formatındaki metni orijinal haline geri çözer.
•	compression_ratio: Sıkıştırma oranını yüzde olarak hesaplar.
•	display_results: Sıkıştırma/Çözme sonuçlarını, boyutları ve doğrulama durumunu düzenli bir şekilde gösterir.
•	Kullanıcı girişi olmadığında test amaçlı ön tanımlı örnek verileri kullanır.
🛠️ Kullanılan Kütüphaneler
Bu betik standart Python kütüphaneleri dışında herhangi bir harici kütüphane kullanmamaktadır.
•	Temel Python (v3.x): String, döngü (for, while), koşullu ifadeler (if/else) ve temel matematiksel işlemler (uzunluk, bölme) kullanılmıştır.
 Algoritma Mantığı: Run-Length Encoding (RLE)
RLE (Çalışma Uzunluğu Kodlaması), ardışık olarak tekrar eden aynı veri değerlerinin (bir "çalışma") bir kez saklanıp, bu değerin kaç kez tekrar ettiğinin (çalışma uzunluğu) yanına yazılması prensibine dayanır.
1. Sıkıştırma (encode fonksiyonu)
Bu işlev, orijinal metni karakter karakter  olarak tarar ve ardışık tekrar eden karakter gruplarını sayar.
•	Metin üzerinde tekrar eden bir karakter serisi bittiğinde (ya da metin sona erdiğinde),
•	Serinin tekrar sayısı ve ardından karakterin kendisi sıkıştırılmış metne eklenir.
Örnek:
•	"AAAAABBBCCDAA" : "5A3B2C1D2A"
2. Çözme (decode fonksiyonu)
Bu işlev, RLE formatındaki sıkıştırılmış metni okur ve orijinal metni yeniden oluşturur.
•	Metin üzerinde sırayla sayı ve ardından karakter beklenir.
•	Önce bir veya daha fazla basamaktan oluşan sayı (tekrar sayısı) okunur.
•	Ardından gelen karakter, okunan sayı kadar çözülmüş metne eklenir.
Örnek:
•	"5A3B2C1D2A" :(5 * 'A') + (3 * 'B') + (2 * 'C') + (1 * 'D') + (2 * 'A') "AAAAABBBCCDAA"
3. Sıkıştırma Oranı Hesaplama (compression_ratio fonksiyonu)
Sıkıştırmanın etkinliğini ölçmek için kullanılır. Oran, sıkıştırma sonrası kazanılan yerin orijinal boyuta oranıdır ve yüzde olarak ifade edilir:
•	Bu algoritma, özellikle uzun ardışık tekrar eden karakter dizilerine sahip metinlerde (örneğin, resim dosyaları veya basit desenler) yüksek sıkıştırma oranları sunar.
•	Ancak, tekrar etmeyen rastgele metinlerde (örneğin, "ABCD" `"1A1B1C1D") sıkıştırılmış dosya orijinalinden daha büyük olabilir.
 Kullanım
Kod, Python yorumlayıcısında doğrudan çalıştırılabilir.
Bash
python dosya_adi.py
1.	Program başladığında, sizden bir metin girmeniz istenir.
2.	Bir metin girdiğinizde, o metin için sıkıştırma ve çözme işlemleri gerçekleştirilir, sonuçlar ve sıkıştırma oranı görüntülenir.
 RLE Sıkıştırma Aracı kullanabilirsiniz!

1️  Kendi metninizi girin ():
  Metin: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWW
Örnek Çıktı (Yukarıdaki Girdi İçin):
============================================================
RUN-LENGTH ENCODING (RLE) SIKIŞTIRMA ARACI
============================================================

 Orijinal Metin:
   'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWW'
   Boyut: 36 karakter

 Sıkıştırılmış Metin:
   '12W1B12W3B8W'
   Boyut: 12 karakter

 Çözülmüş Metin:
   'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWW'
   Boyut: 36 karakter

 Sıkıştırma Oranı: %66.67
    Sıkıştırma başarılı! (24 karakter tasarruf)

 Doğrulama: BAŞARILI 




