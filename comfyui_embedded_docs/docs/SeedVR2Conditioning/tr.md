# SeedVR2 Koşullandırma Uygula

Bu düğüm, SeedVR2 modeliyle kullanım için VAE latentinden pozitif ve negatif conditioning oluşturur. Girdi latentinin şeklini ve model yapısını doğrular, ardından görüntü veya video örneklemeyi yönlendiren hem pozitif hem de negatif conditioning üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 modeli. | MODEL | Evet | - |
| `vae_conditioning` | Conditioning oluşturmak için kullanılacak SeedVR2 VAE latent'i (görünen ad: latent). | LATENT | Evet | - |

Not: `vae_conditioning` latent'i, Comfy'nin kanal-öncelikli yerleşiminde (B, C, T, H, W) 5 boyutlu bir tensor olmalıdır; burada C, beklenen SeedVR2 VAE kanal sayısıdır. Düğüm, latent 5 boyutlu değilse, kanal sayısı eşleşmiyorsa veya kanal-son yerleşimde görünüyorsa hata verir. `model` girdisi, beklenen SeedVR2 yapısına sahip bir model olmalıdır. Dahili olarak, düğüm latent'e sabit bir maske kanalı ekler ve sonuçta oluşan koşulu hem pozitif hem de negatif conditioning havuzlarına bağlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Örnekleme için pozitif conditioning. | CONDITIONING |
| `negative` | Örnekleme için negatif conditioning. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
