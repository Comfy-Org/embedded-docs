# Referans Gizli Değişken

Bir düzenleme modeli için yol gösterici latent'i ayarlar. Conditioning verisini ve isteğe bağlı bir latent girdisini alır, ardından conditioning'i referans latent bilgisi içerecek şekilde değiştirir. Model destekliyorsa, birden fazla referans görseli ayarlamak için birden çok ReferenceLatent düğümünü zincirleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Referans latent bilgisiyle değiştirilecek conditioning verisi | CONDITIONING | Evet | - |
| `latent` | Düzenleme modeli için referans olarak kullanılacak isteğe bağlı latent verisi | LATENT | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Referans latent bilgisi içeren değiştirilmiş conditioning verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/tr.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
