# 📄 Malicious PDF Analysis with peepdf
## Şüpheli PDF Dosyalarında Gömülü JavaScript ve OLE Nesnelerinin Tespiti

---

## 👤 Geliştiren
**Salih Taşkın**  
İstinye Üniversitesi – Bilişim Güvenliği Teknolojisi  

---

## 🎯 Proje Amacı
Bu proje, iş başvurusu gibi güvenilir görünen ancak içinde zararlı kod barındırabilecek PDF dosyalarının analiz edilmesini amaçlamaktadır.

PDF dosyaları sadece metin içermez. Aynı zamanda:
- JavaScript kodları
- Gömülü dosyalar (Embedded Objects)
- Otomatik tetiklenen aksiyonlar (OpenAction)
- Obfuscation teknikleri

içerebilir.

Bu projede bir PDF dosyasının iç yapısı analiz edilerek şüpheli davranışlar tespit edilir.

---

## 🧠 Proje Kapsamı
Bu çalışma tamamen **savunmacı siber güvenlik yaklaşımıyla** hazırlanmıştır.

Proje kapsamında:
- PDF yapısı incelenir
- Şüpheli objeler tespit edilir
- JavaScript kodları analiz edilir
- Gömülü içerikler ortaya çıkarılır
- IOC (Indicator of Compromise) çıkarımı yapılır

> ⚠️ Not: Bu projede exploit çalıştırma veya saldırı gerçekleştirme yoktur.

---

## 🛠️ Kullanılan Araçlar

- peepdf → PDF iç yapısını analiz etmek için
- pdfid.py → Hızlı şüpheli etiket tespiti
- strings → Gizli metinleri çıkarmak için
- Python 3 → Araçları çalıştırmak için
- Kali Linux (opsiyonel) → Analiz ortamı

---

## 🔍 Analiz Süreci

### 1. Ön Tarama (Triage)
```bash
pdfid.py supheli.pdf
