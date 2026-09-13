# TripoSplat Koşullandırma

Bu düğüm, TripoSplat modeli için pozitif ve negatif koşullandırma verisi üretmek amacıyla bir giriş görüntüsünü DINOv3 görüntü kodlayıcısı ve Flux2 VAE ile kodlar. Ayrıca KSampler için başlangıç noktası işlevi gören sabit boyutlu bir gürültü hedefi (latent artı kamera verisi) oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ görüntü kodlayıcısı | CLIP_VISION | Evet | - |
| `vae` | Flux2 VAE | VAE | Evet | - |
| `image` | Kodlanacak giriş görüntüsü | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `positive` | DINOv3 öznitelik dizisini ve referans latent olarak taşınan Flux2 VAE latentini içeren pozitif koşullandırma verisi | CONDITIONING |
| `negative` | Sıfırla doldurulmuş DINOv3 özniteliklerini ve sıfırla doldurulmuş bir Flux2 VAE referans latentini içeren negatif koşullandırma verisi | CONDITIONING |
| `latent` | KSampler için sabit boyutlu gürültü hedefi (latent + kamera). Latent, tek bir kamera token'ı (1 x 5) ile eşleştirilmiş sabit şekilli bir shape-code dizisidir (8192 x 16) | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
