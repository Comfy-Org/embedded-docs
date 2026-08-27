# ModelÖrneklemeSürekliV

ModelSamplingContinuousV düğümü, sürekli V-tahmini örnekleme uygulayarak bir modelin örnekleme davranışını ayarlar. Girdi modelinin bir klonunu oluşturur ve örnekleme süreci üzerinde daha hassas kontrol sağlamak için özel minimum ve maksimum sigma değerleriyle yapılandırır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Sürekli V-tahmini örnekleme ile değiştirilecek girdi modeli | MODEL | Evet | - |
| `örnekleme` | Uygulanacak örnekleme yöntemi; şu anda V-tahmini mevcut tek seçenektir (varsayılan: `"v_prediction"`) | COMBO | Evet | `"v_prediction"` |
| `sigma_maks` | Örnekleme için maksimum sigma değeri (gelişmiş parametre, varsayılan: 500.0) | FLOAT | Evet | 0.0 - 1000.0 |
| `sigma_min` | Örnekleme için minimum sigma değeri (gelişmiş parametre, varsayılan: 0.03) | FLOAT | Evet | 0.0 - 1000.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `model` | Sürekli V-tahmini örnekleme uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/tr.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
