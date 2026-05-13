import re
import tkinter as tk
from tkinter import messagebox

izinli_uzantilar = ['jpg', 'jpeg', 'png', 'gif', 'pdf', 'txt', 'docx', 'xlsx', 'pptx', 'zip', 'rar']

def dosya_kontrol():
    dosya_adi = entry_dosya.get().strip()
    
    if not dosya_adi:
        messagebox.showwarning("Uyarı", "Lütfen bir dosya adı girin!")
        return
    
    if not re.search(r'\.', dosya_adi):
        sonuc_label.config(text="❌ HATA: Uzantı bulunamadı!", fg="red")
        detay_label.config(text="Dosya adında nokta (.) ve uzantı olmalı")
    else:
        uzanti = dosya_adi.split('.')[-1].lower()
        
        if uzanti in izinli_uzantilar:
            sonuc_label.config(text=f"✓ GEÇERLİ: '{uzanti}' uzantısı izinli", fg="green")
            detay_label.config(text=f"'{dosya_adi}' dosyası kullanılabilir")
        else:
            sonuc_label.config(text=f"✗ GEÇERSİZ: '{uzanti}' uzantısı izinli değil", fg="red")
            detay_label.config(text=f"İzinli uzantılar: {', '.join(izinli_uzantilar)}")

def temizle():
    entry_dosya.delete(0, tk.END)
    sonuc_label.config(text="")
    detay_label.config(text="")

pencere = tk.Tk()
pencere.title("Dosya Uzantısı Doğrulayıcı")
pencere.geometry("500x350")
pencere.resizable(False, False)
pencere.configure(bg="#f0f0f0")

baslik_frame = tk.Frame(pencere, bg="#2c3e50", height=60)
baslik_frame.pack(fill="x")

baslik_label = tk.Label(baslik_frame, text="📁 DOSYA UZANTISI DOĞRULAYICI", 
                        font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
baslik_label.pack(pady=15)

ana_frame = tk.Frame(pencere, bg="#f0f0f0")
ana_frame.pack(pady=20)

bilgi_label = tk.Label(ana_frame, text="Dosya adını uzantısıyla birlikte girin:", 
                       font=("Arial", 11), bg="#f0f0f0")
bilgi_label.pack(pady=10)

entry_dosya = tk.Entry(ana_frame, width=40, font=("Arial", 12), bd=2, relief="solid")
entry_dosya.pack(pady=10)

buton_frame = tk.Frame(ana_frame, bg="#f0f0f0")
buton_frame.pack(pady=15)

kontrol_buton = tk.Button(buton_frame, text="Kontrol Et", command=dosya_kontrol,
                          bg="#27ae60", fg="white", font=("Arial", 11, "bold"),
                          width=12, height=1, bd=0, cursor="hand2")
kontrol_buton.pack(side="left", padx=5)

temizle_buton = tk.Button(buton_frame, text="Temizle", command=temizle,
                          bg="#95a5a6", fg="white", font=("Arial", 11, "bold"),
                          width=12, height=1, bd=0, cursor="hand2")
temizle_buton.pack(side="left", padx=5)

sonuc_frame = tk.Frame(ana_frame, bg="white", bd=2, relief="solid", height=80)
sonuc_frame.pack(pady=20, fill="x", padx=20)
sonuc_frame.pack_propagate(False)

sonuc_label = tk.Label(sonuc_frame, text="", font=("Arial", 12, "bold"), 
                       bg="white", wraplength=450)
sonuc_label.pack(pady=5)

detay_label = tk.Label(sonuc_frame, text="", font=("Arial", 9), 
                       bg="white", fg="#555", wraplength=450)
detay_label.pack()

alt_label = tk.Label(pencere, text="İzinli: jpg, jpeg, png, gif, pdf, txt, docx, xlsx, pptx, zip, rar",
                     font=("Arial", 8), fg="#7f8c8d", bg="#f0f0f0")
alt_label.pack(side="bottom", pady=10)

pencere.mainloop()