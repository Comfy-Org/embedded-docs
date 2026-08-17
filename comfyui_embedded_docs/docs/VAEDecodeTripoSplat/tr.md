# TripoSplat Kod Çözme

Bir TripoSplat latent temsilini 3B gaussian splat olarak çözün. Bu düğüm, bir TripoSplat modelinden örneklenen latenti alır ve bunu, üretilen gaussian sayısı değiştirilerek yoğunluğu ayarlanabilen bir dizi 3B gaussian olarak yeniden yapılandırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Çözülecek latent örnekleri | LATENT | Evet | - |
| `vae` | TripoSplat VAE kod çözücü | VAE | Evet | - |
| `num_gaussians` | Üretilecek gaussian sayısı (32'nin katına yuvarlanır). 262144, sekizli ağacın nokta yoğunluğuyla eşleşir; daha yüksek değerler aynı noktaları aşırı örnekler (daha yoğun, ancak yeni ayrıntı yok) ve orantılı olarak daha fazla VRAM/zaman gerektirir. Varsayılan: 262144 | INT | Evet | 32 to 1048576 (step: 32) |
| `seed` | Deterministik çözümler için sekizli ağaç nokta örnekleyicisini (global RNG) tohumlar. Varsayılan: 0 | INT | Evet | 0 to 18446744073709551615 |

**Not:** `num_gaussians` değeri, VAE kod çözücünün nokta başına gaussian ayarının katına otomatik olarak yuvarlanır. Kullanılan gerçek sayı, girdi değerinden biraz farklı olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `splat` | Konumlar, ölçekler, dönüşler, opaklıklar ve küresel harmonik katsayılarını içeren çözülmüş 3B gaussian splat | SPLAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/tr.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
