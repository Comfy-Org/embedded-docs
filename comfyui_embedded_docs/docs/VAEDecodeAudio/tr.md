# VAESesKodunuÇöz

Bu düğüm, bir ses latent temsilini Varyasyonel Otokodlayıcı (VAE) kullanarak yeniden oynatılabilir bir ses dalga formuna dönüştürür. Kodlanmış örnekleri alır, seçilen VAE üzerinden çözer ve ardından genel ses seviyesi tutarlı kalacak şekilde ortaya çıkan dalga formunu normalleştirir. Çıktı sesi, VAE'nin ses örnekleme hızını (varsayılan olarak 44100 Hz) veya girdi örneklerinde bir örnekleme hızı mevcutsa bu değeri kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Latent uzayda kodlanmış, yeniden bir ses dalga formuna çözülecek ses örnekleri. Örnekler kendi örnekleme hızını taşıyorsa çıktı için bu değer kullanılır. | LATENT | Evet | - |
| `vae` | Latent örnekleri sese çözmek için kullanılan Varyasyonel Otokodlayıcı modeli. Girdi örnekleri bir örnekleme hızı belirtmediğinde, ses çıktısı örnekleme hızı (varsayılan 44100 Hz) ortaya çıkan dalga formunun örnekleme hızını belirler. | VAE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | Normalleştirilmiş ses seviyesine sahip, çözülmüş ses dalga formu; örnekleme hızıyla birlikte döndürülür (girdi `samples` içinde varsa bu örnekleme hızı, aksi halde VAE'nin ses örnekleme hızı, varsayılan 44100 Hz). | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
