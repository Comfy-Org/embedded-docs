# Kontrol Noktası Yükle

Bir difüzyon modeli checkpoint dosyasını yükler ve onu üç temel bileşene ayırır: latentleri gürültüden arındırmak için kullanılan ana model, CLIP metin kodlayıcı ve VAE görüntü kodlayıcı/kod çözücü. Düğüm, `ComfyUI/models/checkpoints` klasöründeki tüm model dosyalarını ve `extra_model_paths.yaml` dosyanızda yapılandırılmış ek yolları otomatik olarak algılar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ckpt_adı` | Yüklenecek checkpoint (model) adı. Sonraki görüntü üretiminde kullanılacak AI modelini belirleyen checkpoint model dosyası adını seçin. | COMBO | Evet | checkpoints klasöründe bulunan tüm model dosyaları |

**Not:** ComfyUI çalışırken yeni model dosyaları eklenirse, açılır listede yeni dosyaları görebilmek için tarayıcıyı yenilemeniz (Ctrl+R) gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Latentleri gürültüden arındırmak için kullanılan model. Görüntü üretimi için kullanılan temel difüzyon modelidir. | MODEL |
| `CLIP` | Metin istemlerini kodlamak için kullanılan CLIP modeli; metin açıklamalarını AI'nın anlayabileceği bilgiye dönüştürür. | CLIP |
| `VAE` | Görüntüleri latent uzaya kodlamak ve latent uzaydan kodunu çözmek için kullanılan VAE modeli. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/tr.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
