# SeedVR2 Koşullandırma Uygula

Bu düğüm, SeedVR2 modeliyle kullanım için bir VAE latentinden pozitif ve negatif conditioning oluşturur. Latente bir maske kanalı ekler, ardından modelin yerleşik pozitif ve negatif conditioning embedding'leriyle eşleştirerek örnekleme için gereken conditioning değerlerini üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | SeedVR2 modeli. | MODEL | Evet | - |
| `vae_conditioning` | Conditioning oluşturmak için kullanılan VAE latenti. Görünen ad: latent. | LATENT | Evet | - |

`vae_conditioning` latenti, Comfy kanal-öncelikli düzende (B, C, T, H, W) 5 boyutlu bir tensör olmalı ve SeedVR2 VAE'sinin beklediği kanal sayısına sahip olmalıdır. Kanal-son (channel-last) düzenindeki latentler bir hatayla reddedilir. `model` girdisi, beklenen iç yapıya sahip geçerli bir SeedVR2 modeli olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `positive` | Örnekleme için pozitif conditioning. | CONDITIONING |
| `negative` | Örnekleme için negatif conditioning. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
