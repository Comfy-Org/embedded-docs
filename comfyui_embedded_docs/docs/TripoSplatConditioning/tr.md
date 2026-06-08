# TripoSplat Koşullandırma

Bu düğüm, TripoSplat modeli için pozitif ve negatif koşullandırma verileri oluşturmak amacıyla bir giriş görüntüsünü DINOv3 ve Flux2 VAE kullanarak kodlar. Ayrıca KSampler için başlangıç noktası görevi gören sabit boyutlu bir gürültü hedefi (gizli katman artı kamera verisi) üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `clip_vision` | DINOv3 ViT-H/16+ görüntü kodlayıcı | CLIP_VISION | Evet | - |
| `vae` | Flux2 VAE | VAE | Evet | - |
| `görsel` | Kodlanacak giriş görüntüsü | IMAGE | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `positive` | DINOv3 özellikleri ve Flux2 VAE gizli katmanını içeren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Sıfır doldurulmuş DINOv3 özellikleri ve sıfır doldurulmuş Flux2 VAE gizli katmanını içeren negatif koşullandırma verileri | CONDITIONING |
| `latent` | KSampler için sabit boyutlu gürültü hedefi (gizli dizi artı kamera tokeni) | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `9187a4a020818b9adc762eb41e913086b59d62c47abe92d4bafdb14bc8779f51`
