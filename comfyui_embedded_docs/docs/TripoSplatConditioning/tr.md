# TripoSplat Koşullandırma

Bu düğüm, TripoSplat modeli için pozitif ve negatif koşullandırma verileri oluşturmak amacıyla bir girdi görüntüsünü DINOv3 görüş kodlayıcısı ve Flux2 VAE kullanarak kodlar. Ayrıca KSampler için başlangıç noktası görevi gören sabit boyutlu bir gürültü hedefi (bir latent dizi artı kamera belirteci) üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ görüntü kodlayıcı | CLIP_VISION | Evet | - |
| `vae` | Flux2 VAE | VAE | Evet | - |
| `image` | Kodlanacak girdi görüntüsü | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | DINOv3 görüntü özelliklerini ve girdi görüntüsünün Flux2 VAE latentini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Sıfır doldurulmuş DINOv3 özellikleri ve sıfır doldurulmuş Flux2 VAE latent içeren negatif koşullandırma verileri | CONDITIONING |
| `latent` | KSampler için sabit boyutlu gürültü hedefi (latent + kamera) | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
