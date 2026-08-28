# VAESesKodunuÇöz

VAEDecodeAudio düğümü, bir Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak gizli temsilleri ses dalga formlarına geri dönüştürür. Kodlanmış ses örneklerini alır ve bunları VAE üzerinden işleyerek orijinal sesi yeniden yapılandırır; tutarlı çıktı seviyelerini sağlamak için normalizasyon uygular. Ortaya çıkan ses, varsayılan olarak 44100 Hz örnekleme hızıyla veya sağlanmışsa girdi örneklerinden alınan örnekleme hızıyla döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `örnekler` | Ses dalga formuna geri çözülecek, gizli uzaydaki kodlanmış ses örnekleri | LATENT | Evet | - |
| `vae` | Gizli örnekleri sese çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı (VAE) modeli | VAE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | Normalize edilmiş ses seviyesi ve örnekleme hızına sahip çözülen ses dalga formu (varsayılan: 44100 Hz veya girdi `samples` içinde mevcutsa buradan alınan örnekleme hızı) | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
