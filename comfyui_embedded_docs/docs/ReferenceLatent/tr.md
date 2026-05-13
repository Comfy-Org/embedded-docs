> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/tr.md)

Bu düğüm, bir düzenleme modeli için yönlendirici gizli değişkeni (guiding latent) ayarlar. Koşullandırma verilerini ve isteğe bağlı bir gizli değişken girişini alır, ardından koşullandırmayı referans gizli değişken bilgisini içerecek şekilde değiştirir. Model destekliyorsa, birden fazla referans görseli ayarlamak için birden çok ReferenceLatent düğümünü zincirleyebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `koşullandırma` | CONDITIONING | Evet | - | Referans gizli değişken bilgisi ile değiştirilecek koşullandırma verileri |
| `gizli değişken` | LATENT | Hayır | - | Düzenleme modeli için referans olarak kullanılacak isteğe bağlı gizli değişken verileri |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | CONDITIONING | Referans gizli değişken bilgisini içeren değiştirilmiş koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `d233778cfa7d6f057509f93f8445a0bbf151308e430fc50e28577f48cf136b53`
