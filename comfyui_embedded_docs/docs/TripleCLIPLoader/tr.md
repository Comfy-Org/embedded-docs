# ÜçlüCLIPYükleyici

TripleCLIPLoader düğümü, aynı anda üç farklı metin kodlayıcı modelini yükler ve bunları tek bir CLIP modelinde birleştirir. Bu, clip-l, clip-g ve t5 modellerinin birlikte çalışmasını gerektiren SD3 iş akışları gibi birden fazla metin kodlayıcıya ihtiyaç duyulan gelişmiş metin kodlama senaryoları için kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip_adı1` | Mevcut metin kodlayıcılar arasından yüklenecek ilk metin kodlayıcı modeli | STRING | Evet | Birden çok seçenek mevcut |
| `clip_adı2` | Mevcut metin kodlayıcılar arasından yüklenecek ikinci metin kodlayıcı modeli | STRING | Evet | Birden çok seçenek mevcut |
| `clip_adı3` | Mevcut metin kodlayıcılar arasından yüklenecek üçüncü metin kodlayıcı modeli | STRING | Evet | Birden çok seçenek mevcut |

**Not:** Her üç metin kodlayıcı parametresi de sisteminizdeki mevcut metin kodlayıcı modelleri arasından seçilmelidir. Düğüm, üç modeli de yükleyecek ve işleme için bunları tek bir CLIP modelinde birleştirecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CLIP` | Yüklenen üç metin kodlayıcıyı da içeren birleşik bir CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/tr.md)

---
**Source fingerprint (SHA-256):** `7a9e61090d9d3b0a776d49006dddece08bc4b463b2acd0a9a0f808170ebde348`
