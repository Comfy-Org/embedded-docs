# Kare Enterpolasyon Modeli Yükle

## Genel Bakış

Bu düğüm, bir dosyadan kare enterpolasyon modeli yükler ve onu iş akışında kullanıma hazırlar. Model türünü (FILM veya RIFE) otomatik olarak algılar ve modeli donanımınızda en iyi performans için yapılandırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Yüklenecek bir kare enterpolasyon modeli seçin. Modeller 'frame_interpolation' klasörüne yerleştirilmelidir. | COMBO | Evet | `frame_interpolation` klasöründeki model dosyalarının listesi |

Not: Seçilen dosya tanınan bir FILM veya RIFE kare enterpolasyon modeli değilse, düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | Yüklenmiş, yapılandırılmış ve diğer düğümlerde kullanıma hazır kare enterpolasyon modeli. | INTERP_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/tr.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
