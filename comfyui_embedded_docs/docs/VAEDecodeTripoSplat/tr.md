# TripoSplat Kod Çözme

Bir TripoSplat latent temsilini 3D gaussian splat olarak çözer. Bu düğüm, bir TripoSplat modelinden örneklenen latent'i alır ve onu bir dizi 3D gaussians olarak yeniden yapılandırır; üretilen gaussians sayısı değiştirilerek yoğunluğu ayarlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `örnekler` | Kod çözülecek latent örneklemeler. Örneklemeler, latent akışın yanı sıra iç içe geçmiş bir kamera akışı içeriyorsa, yalnızca latent akış çözülür. | LATENT | Evet | - |
| `vae` | TripoSplat VAE kod çözücü | VAE | Evet | - |
| `gauss_sayısı` | Üretilecek gaussians sayısı (32'nin katına yuvarlanır). 262144, okt ağacının nokta yoğunluğuyla eşleşir; daha yüksek değerler aynı noktaları aşırı örnekler (daha yoğun, ancak yeni ayrıntı eklemez) ve orantılı olarak daha fazla VRAM/zaman maliyeti gerektirir. Varsayılan: 262144 | INT | Evet | 32 ile 1048576 (step: 32) |
| `tohum` | Okt ağacı nokta örnekleyicisini (global RNG) deterministik kod çözme için tohumlar. Varsayılan: 0 | INT | Evet | 0 ile 18446744073709551615 |

**Not:** `num_gaussians` değeri otomatik olarak izin verilen aralığa sınırlandırılır ve VAE kod çözücünün nokta başına gaussians ayarının katına yuvarlanır. Kullanılan gerçek sayı, girdi değerinden biraz farklı olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `splat` | Konumlar, ölçekler, dönüşler, opaklıklar ve küresel harmonik katsayılarını içeren çözülmüş 3D gaussian splat | SPLAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/tr.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
