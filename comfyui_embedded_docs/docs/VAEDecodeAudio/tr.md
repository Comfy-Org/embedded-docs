# VAESesKodunuÇöz

VAEDecodeAudio düğümü, Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak gizli temsilleri ses dalga biçimlerine geri dönüştürür. Kodlanmış ses örneklerini alır ve bunları VAE aracılığıyla işleyerek orijinal sesi yeniden yapılandırır; tutarlı çıkış seviyeleri sağlamak için normalizasyon uygular. Ortaya çıkan ses, standart 44100 Hz örnekleme hızıyla veya sağlanmışsa girdi örneklerindeki örnekleme hızıyla döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Ses dalga biçimine geri çözülecek, gizli uzaydaki kodlanmış ses örnekleri | LATENT | Evet | - |
| `vae` | Gizli örnekleri sese çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı modeli | VAE | Evet | - |

Not: `samples` iç içe geçmiş gizli veri içeriyorsa, kod çözme için yalnızca son öğe kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `AUDIO` | Normalize edilmiş ses seviyesi ve örnekleme hızıyla (varsayılan: 44100 Hz veya girdi `samples` içinde mevcutsa bu örneklerin örnekleme hızı) çözülmüş ses dalga biçimi | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
