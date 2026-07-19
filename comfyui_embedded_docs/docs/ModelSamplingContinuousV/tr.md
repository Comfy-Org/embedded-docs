# ModelÖrneklemeSürekliV

**ModelSamplingContinuousV** düğümü, sürekli V-tahmin örnekleme parametrelerini uygulayarak bir modelin örnekleme davranışını değiştirir. Giriş modelinin bir kopyasını oluşturur ve gelişmiş örnekleme kontrolü için özel sigma aralığı ayarlarıyla yapılandırır. Bu, kullanıcıların belirli minimum ve maksimum sigma değerleriyle örnekleme sürecini ince ayar yapmasına olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Sürekli V-tahmin örnekleme ile değiştirilecek giriş modeli | MODEL | Evet | - |
| `örnekleme` | Uygulanacak örnekleme yöntemi (şu anda yalnızca V-tahmini desteklenmektedir) | STRING | Evet | `"v_prediction"` |
| `sigma_maks` | Örnekleme için maksimum sigma değeri (varsayılan: 500.0) | FLOAT | Evet | 0.0 - 1000.0 |
| `sigma_min` | Örnekleme için minimum sigma değeri (varsayılan: 0.03) | FLOAT | Evet | 0.0 - 1000.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Sürekli V-tahmin örnekleme uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/tr.md)

---
**Source fingerprint (SHA-256):** `8095b5024c0d33011f6a81ed496cf1711981701e0f35f9527646b150f5033d45`
