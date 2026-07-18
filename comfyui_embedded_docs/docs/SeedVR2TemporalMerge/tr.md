# SeedVR2TemporalMerge

Bu düğüm, Split SeedVR2 Latent düğümü tarafından daha önce bölünmüş olan geçici gizli video verisi parçalarını yeniden birleştirir. Örtüşen bölgeler üzerinde bir Hann penceresi çapraz geçişi kullanarak parçalar arasında yumuşak bir geçiş oluşturur veya örtüşme belirtilmediğinde basit bir birleştirme gerçekleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `latents` | Sıralı olarak örneklenmiş geçici parçalar. | LATENT | Evet | Gizli değişken listesi |
| `temporal_overlap` | Split SeedVR2 Latent çıktısındaki temporal_overlap değeri. 0 = düz birleştirme. | INT | Evet | 0 ile 16384 arası (varsayılan: 0) |

**Not:** `temporal_overlap` parametresi, Split SeedVR2 Latent düğümünün `temporal_overlap` çıktısına bağlanmalıdır. Tüm giriş gizli değişkenleri aynı grup boyutuna, kanal sayısına, yüksekliğe ve genişliğe sahip olmalıdır. Yalnızca son parça, diğerlerinden daha kısa bir geçici boyuta sahip olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `latent` | Yeniden birleştirilmiş tam uzunluktaki gizli değişken. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/tr.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
