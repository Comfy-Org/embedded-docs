# ModelÖrneklemeSürekliV

ModelSamplingContinuousV düğümü, sürekli V-tahmini örnekleme parametreleri uygulayarak bir modelin örnekleme davranışını değiştirir. Giriş modelinin bir kopyasını oluşturur ve gelişmiş örnekleme kontrolü için özel sigma aralığı ayarlarıyla yapılandırır. Bu, kullanıcıların örnekleme sürecini belirli minimum ve maksimum sigma değerleriyle ince ayar yapmasına olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Sürekli V-tahmini örnekleme ile değiştirilecek giriş modeli | MODEL | Evet | - |
| `sampling` | Uygulanacak örnekleme yöntemi. Şu anda yalnızca V-tahmini desteklenmektedir. | COMBO | Evet | `"v_prediction"` |
| `sigma_max` | Örnekleme için maksimum sigma değeri (varsayılan: 500.0) | FLOAT | Evet | 0.0 – 1000.0 (step 0.001) |
| `sigma_min` | Örnekleme için minimum sigma değeri (varsayılan: 0.03) | FLOAT | Evet | 0.0 – 1000.0 (step 0.001) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Sürekli V-tahmini örnekleme uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/tr.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
