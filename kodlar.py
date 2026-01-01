def encode(text):
    """
    Verilen metni RLE ile sıkıştırır.
    
    """
    if not text:
        return ""
    
    encoded =""
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded += str(count) + current_char
            current_char = text[i]
            count = 1
    
    
    encoded += str(count) + current_char
    
    return encoded


def decode(encoded_text):
    """
    Sıkıştırılmış metni orijinal haline döndürür.
   
    """
    if not encoded_text:
        return ""
    
    decoded = ""
    i = 0
    
    while i < len(encoded_text):
        # Sayıyı okumaya yardımcı olur
        count_str = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            count_str += encoded_text[i]
            i += 1
        
        # Karakteri okur
        if i < len(encoded_text):
            char = encoded_text[i]
            count = int(count_str)
            decoded += char * count
            i += 1
    
    return decoded


def compression_ratio(original, compressed):
    """
    Sıkıştırma oranını yüzde olarak hesaplar.
    """
    original_size = len(original)
    compressed_size = len(compressed)
    
    if original_size == 0:
        return 0
    
    ratio = ((original_size - compressed_size) / original_size) * 100
    return ratio


def display_results(original, compressed, decoded):
    """
    Sonuçları düzenli bir şekilde gösterir.
    """
    print("=" * 60)
    print("RUN-LENGTH ENCODING (RLE) SIKIŞTIRMA ARACI")
    print("=" * 60)
    
    print(f"\n Orijinal Metin:")
    print(f"   '{original}'")
    print(f"   Boyut: {len(original)} karakter")
    
    print(f"\n Sıkıştırılmış Metin:")
    print(f"   '{compressed}'")
    print(f"   Boyut: {len(compressed)} karakter")
    
    print(f"\n Çözülmüş Metin:")
    print(f"   '{decoded}'")
    print(f"   Boyut: {len(decoded)} karakter")
    
    ratio = compression_ratio(original, compressed)
    print(f"\n Sıkıştırma Oranı: %{ratio:.2f}")
    
    if len(compressed) < len(original):
        print(f"    Sıkıştırma başarılı! ({len(original) - len(compressed)} karakter tasarruf)")
    elif len(compressed) > len(original):
        print(f"     Sıkıştırma verimsiz! ({len(compressed) - len(original)} karakter artış)")
    else:
        print(f"   Boyut değişmedi")
    
    print(f"\n Doğrulama: {'BAŞARILI ' if original == decoded else 'HATA '}")
   


# Ana Program
if __name__ == "__main__":
    print("\n RLE Sıkıştırma Aracı kullanabilirsiniz!\n")
    
    #  Kullanıcıdan girdi aldı
    print("1️  Kendi metninizi girin ():")
    user_input = input("   Metin: ").strip()
    
    if not user_input:
        # veri örneği
        test_data = [
            "AAAAABBBCCDAA",
            "111110001110000",
            "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWW",
            "ABCD",
            "AAAAA"
        ]
        
        print(f"\n  Örnek veriler kullanılıyor...\n")
        
        for test in test_data:
            # Sıkıştırma 
            compressed = encode(test)
            
            # Çöz
            decompressed = decode(compressed)
            
            # Sonuçları gösteriyor
            display_results(test, compressed, decompressed)
            print()
    else:
        # Kullanıcı girdisini işlemek için 
        compressed = encode(user_input)
        decompressed = decode(compressed)
        display_results(user_input, compressed, decompressed)
    
    print("\n Program tamamlandı!")