# SeedVR2 Latent'lerini Birleştir

Bu düğüm, örneklenmiş SeedVR2 latent zamansal parçalarını tek bir tam uzunlukta latent halinde yeniden birleştirir. Bir zamansal örtüşme belirtildiğinde, parçalar arasında yumuşak geçişler oluşturmak için her örtüşen bölgeye Hann pencereli çapraz geçiş uygular; örtüşme 0 olduğunda ise düz birleştirme yapar.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|--------|
| `latents` | Sıralı olarak örneklenmiş zamansal parçalar. | LATENT | Evet | Latent listesi |
| `temporal_overlap` | Split SeedVR2 Latent çıktısının temporal_overlap değeri. 0 = düz birleştirme. (varsayılan: 0) | INT | Evet | 0 ile 16384 arası |

**Not:** `temporal_overlap` değeri 0'dan büyük veya eşit olmalıdır. Tüm parçalar 5 boyutlu video latentleri (B, C, T, H, W) olmalı ve zamansal eksen (T) dışında her boyutta eşleşmelidir; yalnızca son parça diğerlerinden daha kısa olabilir. Yalnızca bir parça sağlanırsa, değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `latent` | Yeniden birleştirilmiş tam uzunlukta latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/tr.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
