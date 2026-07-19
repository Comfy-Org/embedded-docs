# TripoSplat Kod Çözme

TripoSplat gizli temsilini 3 boyutlu Gauss saçılımına dönüştürür. Bu düğüm, TripoSplat modelinden alınan örneklenmiş gizli veriyi alır ve üretilen Gauss sayısını değiştirerek yoğunluğu ayarlanabilen bir dizi 3 boyutlu Gauss olarak yeniden yapılandırır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `örnekler` | Kod çözülecek gizli örnekler | LATENT | Evet | - |
| `vae` | TripoSplat VAE kod çözücü modeli | VAE | Evet | - |
| `gauss_sayısı` | Üretilecek Gauss sayısı (32'nin katına yuvarlanır). 262144, sekizli ağacın nokta yoğunluğuyla eşleşir; daha yüksek değerler aynı noktaları aşırı örnekler (daha yoğun, ancak yeni detay eklemez) ve orantılı olarak daha fazla VRAM/zaman harcar. Varsayılan: 262144 | INT | Evet | 32 ile 1048576 arası (adım: 32) |
| `tohum` | Belirleyici kod çözme için sekizli ağaç nokta örnekleyicisini (küresel RNG) tohumlar. Varsayılan: 0 | INT | Evet | 0 ile 18446744073709551615 arası |

**Not:** `num_gaussians` değeri, VAE kod çözücünün nokta başına Gauss ayarına otomatik olarak yuvarlanır. Kullanılan gerçek sayı, giriş değerinden biraz farklı olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `splat` | Konumlar, ölçekler, dönüşler, opaklıklar ve küresel harmonik katsayılarını içeren kod çözülmüş 3 boyutlu Gauss saçılımı | SPLAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/tr.md)

---
**Source fingerprint (SHA-256):** `60fff70ade38bc820eaea9db26b714daf84a111fb3563477f56f4e8ffa96ff5b`
