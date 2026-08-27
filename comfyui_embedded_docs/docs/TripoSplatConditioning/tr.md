# TripoSplat Koşullandırma

Bu düğüm, giriş görüntüsünü DINOv3 görüntü kodlayıcı ve Flux2 VAE kullanarak kodlar; TripoSplat modeli için pozitif ve negatif koşullandırma verileri oluşturur. Ayrıca KSampler için başlangıç noktası görevi gören sabit boyutlu bir gürültü hedefi (latent artı kamera verisi) üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ görüntü kodlayıcı | CLIP_VISION | Evet | - |
| `vae` | Flux2 VAE | VAE | Evet | - |
| `görsel` | Kodlanacak giriş görüntüsü | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | DINOv3 özelliklerini ve Flux2 VAE latentini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negatif` | Sıfır doldurulmuş DINOv3 özelliklerini ve sıfır doldurulmuş Flux2 VAE latentini içeren negatif koşullandırma verileri | CONDITIONING |
| `latent` | KSampler için sabit boyutlu gürültü hedefi (latent + kamera) | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
