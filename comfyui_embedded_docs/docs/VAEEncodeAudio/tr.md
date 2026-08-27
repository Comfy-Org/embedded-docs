# VAESesKodla

VAEEncodeAudio düğümü, bir Değişken Otomatik Kodlayıcı (VAE) kullanarak ses verilerini latent bir temsile dönüştürür. Ses girdisini alır ve VAE aracılığıyla işleyerek daha sonraki ses üretimi veya manipülasyon görevlerinde kullanılabilecek sıkıştırılmış latent örnekler üretir. Düğüm, kodlamadan önce gerekirse sesi VAE'nin beklenen örnekleme hızına uyacak şekilde otomatik olarak yeniden örnekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Kodlanacak ses verisi, dalga formu ve örnekleme hızı bilgisi içerir | AUDIO | Evet | - |
| `vae` | Sesi latent uzaya kodlamak için kullanılan Değişken Otomatik Kodlayıcı modeli | VAE | Evet | - |

**Not:** Orijinal örnekleme hızı bu değerden farklıysa, ses girdisi VAE'nin beklenen örnekleme hızına (varsayılan: 44100 Hz) uyacak şekilde otomatik olarak yeniden örneklenir. Ses girdisi None ise (örn. kaynak videoda ses parçası yoksa), düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Sıkıştırılmış örnekler içeren, latent uzayda kodlanmış ses temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/tr.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`
