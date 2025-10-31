> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/tr.md)

Bu düğüm, bir düzenleme modeli için kılavuz gizli katmanı (latent) ayarlar. Koşullandırma verilerini ve isteğe bağlı bir gizli katman girdisini alır, ardından koşullandırmayı referans gizli katman bilgilerini içerecek şekilde değiştirir. Model destekliyorsa, birden fazla referans görüntü ayarlamak için birden fazla ReferenceLatent düğümünü zincirleyebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Evet | - | Referans gizli katman bilgileri ile değiştirilecek koşullandırma verileri |
| `latent` | LATENT | Hayır | - | Düzenleme modeli için referans olarak kullanılacak isteğe bağlı gizli katman verisi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | CONDITIONING | Referans gizli katman bilgilerini içeren değiştirilmiş koşullandırma verileri |