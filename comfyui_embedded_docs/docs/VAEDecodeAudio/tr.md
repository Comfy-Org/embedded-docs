# VAESesKodunuÇöz

VAEDecodeAudio düğümü, bir Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak gizli uzay temsillerini ses dalga formlarına dönüştürür. Kodlanmış ses örneklerini alır ve bunları VAE aracılığıyla işleyerek orijinal sesi yeniden oluşturur; tutarlı çıkış seviyeleri sağlamak için normalizasyon uygular. Ortaya çıkan ses, standart 44100 Hz örnekleme hızıyla döndürülür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Ses dalga formuna geri çözülecek olan, gizli uzaydaki kodlanmış ses örnekleri | LATENT | Evet | - |
| `vae` | Gizli örnekleri sese çözmek için kullanılan Varyasyonel Otomatik Kodlayıcı modeli | VAE | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `AUDIO` | Normalize edilmiş ses seviyesi ve 44100 Hz örnekleme hızına sahip, çözülmüş ses dalga formu | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `15848d3763324cbae986949146d57352c68369713cd99a27d216797560836824`
