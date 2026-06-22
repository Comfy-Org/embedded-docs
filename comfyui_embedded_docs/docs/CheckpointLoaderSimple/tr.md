# Kontrol Noktası Yükle

## Genel Bakış

Bir difüzyon modeli kontrol noktası (checkpoint) dosyasını yükler ve üç temel bileşene ayırır: gizli değişkenleri (latent) gürültüden arındırmak için kullanılan ana model, CLIP metin kodlayıcı ve VAE görüntü kodlayıcı/kod çözücü. Bu düğüm, `ComfyUI/models/checkpoints` klasöründeki ve `extra_model_paths.yaml` dosyanızda yapılandırılmış ek yollardaki tüm model dosyalarını otomatik olarak algılar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ckpt_adı` | Yüklenecek kontrol noktasının (model) adı. Sonraki görüntü oluşturma için kullanılacak AI modelini belirleyen kontrol noktası model dosyası adını seçin. | STRING | Evet | Kontrol noktaları klasöründeki tüm model dosyaları |

**Not:** ComfyUI çalışırken yeni model dosyaları eklenirse, açılır listede yeni dosyaları görmek için tarayıcıyı yenilemeniz (Ctrl+R) gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Gizli değişkenleri gürültüden arındırmak için kullanılan model. Görüntü oluşturma için kullanılan temel difüzyon modelidir. | MODEL |
| `CLIP` | Metin istemlerini (prompt) kodlamak için kullanılan CLIP modeli, metin açıklamalarını AI'nın anlayabileceği bilgilere dönüştürür. | CLIP |
| `VAE` | Görüntüleri gizli uzaya (latent space) kodlamak ve gizli uzaydan çözmek için kullanılan VAE modeli. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/tr.md)

---
**Source fingerprint (SHA-256):** `2fd8866ae659f8080f46c16d3a9864fa563d2090815d897ea2f42ba8d66d9b39`
