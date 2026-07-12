# SeedVR2TemporalMerge

Bu düğüm, örneklenmiş SeedVR2 latent zamansal parçalarını tek bir tam uzunlukta latent halinde yeniden birleştirir. Parçalar arasındaki örtüşme bölgesinde yumuşak geçişler oluşturmak için Hann penceresi çapraz geçişi kullanır veya örtüşme belirtilmediğinde düz birleştirme gerçekleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|--------|
| `latents` | Sıralı olarak örneklenmiş zamansal parçalar. | LATENT | Evet | Latent listesi |
| `temporal_overlap` | Split SeedVR2 Latent çıktısının temporal_overlap değeri. 0 = düz birleştirme. (varsayılan: 0) | INT | Evet | 0 ile 16384 arası |

**Not:** `temporal_overlap` değeri 0'dan büyük veya eşit olmalıdır. Dizideki son parça, diğer parçalardan daha az zamansal kareye sahip olabilir. Tüm parçalar, zamansal eksen (T) dışında eşleşen boyutlara sahip olmalıdır ve ilk parça 5 boyutlu (B, C, T, H, W) olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `latent` | Yeniden birleştirilmiş tam uzunlukta latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/tr.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
