# SeedVR2Conditioning

Bu düğüm, SeedVR2 modeliyle kullanılmak üzere bir VAE gizil uzayından (latent) pozitif ve negatif koşullandırma (conditioning) oluşturur. Görüntü veya video oluşturma sürecini yönlendiren koşullandırma verilerini hazırlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | SeedVR2 modeli. | MODEL | Evet | - |
| `vae_conditioning` | Koşullandırmanın oluşturulacağı VAE gizil uzayı. | LATENT | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model` | SeedVR2 modeli. | MODEL |
| `positive` | Oluşturmayı yönlendiren pozitif koşullandırma. | CONDITIONING |
| `negative` | Oluşturmayı yönlendiren negatif koşullandırma. | CONDITIONING |
| `latent` | İşlenmiş gizil uzay örnekleri. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `8f99c0e712c5c6fc76261d6d72c5c08b7202c77827ecf2549240fc530c1b65bd`
