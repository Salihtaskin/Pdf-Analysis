# 📄 Malicious PDF Analysis with peepdf
## Şüpheli PDF Dosyalarında Gömülü JavaScript ve OLE Nesnelerinin Tespiti

---

## 👤 Geliştiren
**Salih Taşkın**  
İstinye Üniversitesi – Bilişim Güvenliği Teknolojisi  

---

Bu proje, iş başvurusu senaryosuyla gelen ve içinde gizli zararlı yazılım barındıran bir PDF dosyasının (**evil.pdf**) statik analiz ve tersine mühendislik süreçlerini içermektedir. Analiz kapsamında, PDF hiyerarşisi çözümlenmiş ve içerisindeki gizli "payload" (yük) başarıyla ayıklanmıştır.

## 🎯 Proje Hedefi
- PDF dosyalarındaki şüpheli nesne (Object) yapılarını tespit etmek.
- Gizlenmiş JavaScript ve Otomatik Başlatma (Launch) komutlarını analiz etmek.
- PDF içine gömülmüş (Embedded) harici dosyaları (Payload) gün yüzüne çıkarmak.

## 🛠️ Kullanılan Araçlar & Ortam
- **İşletim Sistemi:** Kali Linux
- **Analiz Aracı:** `peepdf` (Python 2.7 tabanlı)
- **Yardımcı Araçlar:** `file`, `strings`, `Python 3` (Payload üretimi için)

## 🔍 Analiz Metodolojisi (Adım Adım)

### 1. İlk Tarama ve Bayrak Tespiti
`peepdf` ile yapılan ilk taramada, dosyanın standart bir dökümandan çok daha fazlasını içerdiği saptanmıştır.
- **/OpenAction:** Kullanıcı etkileşimi olmadan eylem başlatma.
- **/JS & /JavaScript:** Dosya içinde çalıştırılabilir kod bloğu.
- **/Launch:** Sistem üzerinde komut çalıştırma yetkisi.
- **/EmbeddedFiles:** PDF içine gizlenmiş harici veri.

### 2. Nesne Ağacı (Object Tree) Analizi
Hiyerarşik inceleme sonucunda saldırı zinciri şu şekilde deşifre edilmiştir:
- **Object 9 (JavaScript):** `this.exportDataObject` metodu kullanılarak, içerideki gizli dosyanın sessizce diske yazılması (Dropping) hedeflenmiştir.
- **Object 10 (Launch Action):** Windows `cmd.exe` üzerinden, dışa aktarılan dosyanın farklı sistem klasörlerinde (Desktop, Documents vb.) aranıp otomatik olarak çalıştırılması kurgulanmıştır.

### 3. Payload Extraction (Yükün Ayıklanması)
İz sürülen nesne zinciri (Object 5 -> 6 -> 7 -> 8) sonucunda, asıl zararlı verinin **8 numaralı nesne (Stream)** içinde olduğu tespit edilmiştir. 
`stream 8 > template_payload.bin` komutuyla ayıklanan dosyanın gerçek kimliği sorgulanmıştır.

## 📊 Bulgular (Final Report)
Analiz sonucunda, `template.pdf` ismiyle gizlenen dosyanın aslında bir PDF değil, **PE32+ executable (GUI) x86-64 (Windows .exe)** dosyası olduğu kanıtlanmıştır.

- **Tetikleyici:** `OpenAction`
- **Yöntem:** JavaScript Dropper + CMD Execution
- **Sonuç:** Başarılı Payload Ayıklama

---
**⚠️ Uyarı:** Bu proje tamamen eğitim ve savunma amaçlıdır. Analiz edilen dosyalar gerçek bir sistemde çalıştırılmamalıdır.
