# ÜçlüCLIPYükleyici

TripleCLIPLoader, aynı anda üç metin kodlayıcı modelini yükler ve bunları tek bir CLIP modelinde birleştirir. SD3 gibi clip-l, clip-g ve t5 modellerini kullanan birden fazla metin kodlayıcının birlikte çalışmasını gerektiren iş akışları için kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_adı1` | Mevcut metin kodlayıcıları arasından yüklenecek ilk metin kodlayıcı modeli | COMBO | Evet | Birden çok seçenek mevcuttur (text_encoders klasöründeki tüm dosyalar) |
| `clip_adı2` | Mevcut metin kodlayıcıları arasından yüklenecek ikinci metin kodlayıcı modeli | COMBO | Evet | Birden çok seçenek mevcuttur (text_encoders klasöründeki tüm dosyalar) |
| `clip_adı3` | Mevcut metin kodlayıcıları arasından yüklenecek üçüncü metin kodlayıcı modeli | COMBO | Evet | Birden çok seçenek mevcuttur (text_encoders klasöründeki tüm dosyalar) |

**Not:** Üç parametrenin tümü de gereklidir. Mevcut seçenekler, text_encoders klasörünüzdeki metin kodlayıcı dosyalarıdır. Seçilen bir dosya bulunamazsa düğüm hata verir. Düğüm, seçilen üç modeli de yükler ve bunları tek bir CLIP modelinde birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CLIP` | Yüklenen üç metin kodlayıcının tümünü içeren birleşik bir CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/tr.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
