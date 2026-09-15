# LTXV Latent'i Dondur

LTXV Freeze Latent düğümü, bir latentin gürültü maskesini sıfıra ayarlar; bu, örnekleme çalışırken o latentin temiz ve değişmemiş kalmasını sağlar. Hem video hem de ses latentleri üzerinde çalışır; böylece bir latent, başkalarıyla birleştirilmeden önce veya hiç gürültüden arındırılmaması gerektiğinde dondurulabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `latent` | Dondurulacak video veya ses latentı. Ses 4D'dir; video 5D'dir. | LATENT | Evet | N/A |

### Kısıtlamalar

- Latent düz bir tensör içermelidir. Birleştirilmiş bir ses-video latentı kabul edilmez; önce Separate AV Latent düğümüyle ayrılmalıdır.
- Yalnızca 4D latentler (ses) ve 5D latentler (video) desteklenir. Başka herhangi bir şekil hataya neden olur.
- Oluşturulan gürültü maskesi, girdi tensörüyle aynı cihaz kullanılarak sıfırlarla oluşturulur. Video latentleri için maskenin şekli (batch, 1, frames, 1, 1); ses latentleri için şekli (batch, 1, frames, 1) olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `latent` | Örnekleme sırasında temiz kalması için sıfırlardan oluşan bir gürültü maskesi eklenmiş girdi latentı. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/tr.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
