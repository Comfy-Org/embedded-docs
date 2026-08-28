# Referans Gizli Değişken

Bu düğüm, bir düzenleme modeli için yönlendirici latent değerini ayarlar. Koşullandırma verilerini ve isteğe bağlı bir latent girdisini alır, ardından referans latent bilgisini içerecek şekilde koşullandırmayı değiştirir. Model destekliyorsa, birden fazla referans görseli ayarlamak için birden çok ReferenceLatent düğümünü zincirleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `koşullandırma` | Referans latent bilgisiyle değiştirilecek koşullandırma verisi | CONDITIONING | Evet | - |
| `gizli değişken` | Düzenleme modeli için referans olarak kullanılacak isteğe bağlı latent veri. Sağlanmazsa koşullandırma değiştirilmeden döndürülür | LATENT | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Referans latent bilgisini içeren değiştirilmiş koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/tr.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
