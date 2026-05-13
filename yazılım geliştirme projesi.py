import re

izinli_uzantilar = ['jpg', 'jpeg', 'png', 'gif', 'pdf', 'txt', 'docx', 'xlsx', 'pptx', 'zip', 'rar']

print("=" * 50)
print("DOSYA UZANTISI DOĞRULAYICI")
print("=" * 50)

dosya_adi = input("\nDosya adını uzantısıyla birlikte girin: ").strip()

if not re.search(r'\.', dosya_adi):
    print("\n[HATA] Geçersiz dosya adı! Uzantı bulunamadı.")
else:
    uzanti = dosya_adi.split('.')[-1].lower()
    
    print(f"\nAlgılanan uzantı: {uzanti}")
    
    if uzanti in izinli_uzantilar:
        print(f"\n✓ BAŞARILI: '{uzanti}' uzantısı izin verilen dosya türlerindendir.")
    else:
        print(f"\n✗ BAŞARISIZ: '{uzanti}' uzantısı izin verilen dosya türlerinde değil.")
        print(f"\nİzin verilen uzantılar: {', '.join(izinli_uzantilar)}")

print("\n" + "=" * 50)