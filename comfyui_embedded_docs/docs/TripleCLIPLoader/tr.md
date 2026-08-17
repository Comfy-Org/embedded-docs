# ÜçlüCLIPYükleyici

TripleCLIPLoader düğümü, üç metin kodlayıcı modelini aynı anda yükler ve bunları tek bir CLIP modelinde birleştirir. Bu, birden fazla metin kodlayıcının gerekli olduğu gelişmiş metin kodlama senaryolarında kullanışlıdır; örneğin clip-l, clip-g ve t5 modellerinin birlikte çalışmasını gerektiren SD3 iş akışlarında.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | Kullanılabilir metin kodlayıcılarından yüklenecek ilk metin kodlayıcı modeli | COMBO | Evet | text_encoders klasöründeki tüm metin kodlayıcı dosyaları |
| `clip_name2` | Kullanılabilir metin kodlayıcılarından yüklenecek ikinci metin kodlayıcı modeli | COMBO | Evet | text_encoders klasöründeki tüm metin kodlayıcı dosyaları |
| `clip_name3` | Kullanılabilir metin kodlayıcılarından yüklenecek üçüncü metin kodlayıcı modeli | COMBO | Evet | text_encoders klasöründeki tüm metin kodlayıcı dosyaları |

**Not:** Üç metin kodlayıcı parametresinin tümü, sisteminizdeki kullanılabilir metin kodlayıcı modelleri arasından seçilmelidir. Düğüm, üç modeli de belirtilen sırayla yükler ve işleme için bunları tek bir CLIP modelinde birleştirir. SD3 iş akışları için üç kodlayıcı olarak clip-l, clip-g ve t5 kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-------------|-----------|
| `CLIP` | Yüklenen üç metin kodlayıcıyı içeren birleşik bir CLIP modeli | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/tr.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
