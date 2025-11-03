> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/tr.md)

VAEEncodeAudio düğümü, ses verilerini Varyasyonel Otokodlayıcı (VAE) kullanarak gizli temsile dönüştürür. Ses girişini alır ve VAE üzerinden işleyerek, daha sonraki ses üretimi veya manipülasyon görevlerinde kullanılabilecek sıkıştırılmış gizli örnekler üretir. Düğüm, kodlamadan önce gerekirse sesi otomatik olarak 44100 Hz'e yeniden örnekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses` | AUDIO | Evet | - | Kodlanacak ses verisi; dalga formu ve örnekleme hızı bilgisini içerir |
| `vae` | VAE | Evet | - | Sesi gizli uzaya kodlamak için kullanılan Varyasyonel Otokodlayıcı modeli |

**Not:** Orijinal örnekleme hızı bu değerden farklıysa, ses girişi otomatik olarak 44100 Hz'e yeniden örneklenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Gizli uzayda kodlanmış ses temsili; sıkıştırılmış örnekler içerir |