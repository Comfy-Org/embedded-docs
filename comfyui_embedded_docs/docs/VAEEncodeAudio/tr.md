# VAESesKodla

VAE Encode Audio düğümü, ses verilerini bir Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak gizli bir temsile dönüştürür. Gelen sesi, daha ileri ses üretimi veya manipülasyon görevlerinde kullanılabilecek sıkıştırılmış gizli örnekler üretmek için VAE üzerinden işler. Sesin örnekleme hızı, VAE'nin beklediği örnekleme hızından farklıysa ses, kodlamadan önce otomatik olarak yeniden örneklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Kodlanacak ses verisi; dalga formu ve örnekleme hızı bilgilerini içerir | AUDIO | Evet | - |
| `vae` | Sesi gizli uzaya kodlamak için kullanılan Varyasyonel Otomatik Kodlayıcı modeli | VAE | Evet | - |

**Not:** Orijinal örnekleme hızı bu değerden farklıysa, ses girdisi VAE'nin beklediği örnekleme hızıyla (varsayılan: 44100 Hz) eşleşecek şekilde otomatik olarak yeniden örneklenir. Girdi sesi None ise (örneğin, kaynak videoda ses parçası yoksa), düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Gizli uzaydaki kodlanmış ses temsili; sıkıştırılmış örnekleri içerir | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`
