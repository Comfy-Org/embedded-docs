# SeedVR2 Koşullandırma Uygula

Bir VAE latentinden SeedVR2 modeliyle kullanılmak üzere pozitif ve negatif koşullandırma oluşturur. Girdi latentini ve model yapısını doğrular, latente bir maske kanalı ekler ve her iki koşullandırma çıktısını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 modeli. | MODEL | Evet | - |
| `vae_conditioning` | Koşullandırma oluşturmak için SeedVR2 VAE latentı (görünen ad: latent). | LATENT | Evet | - |

Not: `vae_conditioning` latentı, Comfy kanal-önce düzeninde (B, C, T, H, W) 5 boyutlu bir tensör olmalıdır; burada C, beklenen SeedVR2 VAE kanal sayısıdır. Latent 5 boyutlu değilse, kanal sayısı eşleşmiyorsa veya tensör kanal-son düzeninde görünüyorsa düğüm bir hata verir. `model` girdisi beklenen SeedVR2 yapısına sahip olmalıdır; düğüm iç difüzyon modelini çözer ve pozitif ve negatif koşullandırmasını okur. Düğüm dahili olarak latente sabit bir maske kanalı ekler ve elde edilen koşulu hem pozitif hem de negatif koşullandırma çıktılarına bağlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `positive` | Örnekleme için pozitif koşullandırma. | CONDITIONING |
| `negative` | Örnekleme için negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
