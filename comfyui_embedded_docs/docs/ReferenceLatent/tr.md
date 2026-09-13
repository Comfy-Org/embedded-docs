# Referans Gizli Değişken

Bu düğüm, bir düzenleme modeli için yol gösterici latentı ayarlar. Koşullandırma verisini ve isteğe bağlı bir latent girdisini alır, ardından koşullandırmayı referans latent bilgisini içerecek şekilde değiştirir. Model bunu destekliyorsa, birden fazla referans görüntüsü ayarlamak için birden çok Set Reference Latent düğümünü zincirleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `koşullandırma` | Referans latent bilgisiyle değiştirilecek koşullandırma verisi | CONDITIONING | Evet | - |
| `gizli değişken` | Düzenleme modeli için referans olarak kullanılacak isteğe bağlı latent verisi. Sağlanmazsa, koşullandırma değiştirilmeden döndürülür | LATENT | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Referans latent bilgisini içeren değiştirilmiş koşullandırma verisi | CONDITIONING |

## Notlar

- Referans latent, örnek tensörlerden oluşan bir liste olarak saklanır; bu nedenle birkaç Set Reference Latent düğümünü sırayla bağlamak, öncekinin yerini almak yerine ek referanslar ekler.
- `latent` bağlı olmadığında, düğüm gelen `conditioning` verisini değişiklik yapmadan geçirir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/tr.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
