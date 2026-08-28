# Klasörden Görsel Veri Kümesi Yükle

Bu düğüm, ComfyUI ana girdi dizinindeki seçili bir alt klasörden birden fazla görüntü yükler ve bunları bir liste olarak döndürür. Seçilen klasörü PNG, JPG, JPEG veya WEBP formatındaki görüntü dosyaları için tarar; bu da onu toplu işleme veya görüntü veri kümeleri hazırlamak için kullanışlı hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görüntülerin yükleneceği klasör. Seçenekler, ComfyUI ana girdi dizininde bulunan alt klasörlerdir. | COMBO | Evet | Birden fazla seçenek mevcuttur |

Not: Seçilen klasör, ComfyUI ana girdi dizininin bir alt klasörü olmalıdır; bu dizinin dışına çözümlenen herhangi bir değer reddedilir. Yalnızca .png, .jpg, .jpeg veya .webp uzantılı dosyalar yüklenir ve uzantı denetimi büyük/küçük harf duyarlı değildir. Seçilen klasör geçerli görüntü dosyası içermiyorsa düğüm bir hata oluşturur. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Yüklenen görüntülerin listesi. Düğüm, seçilen klasörde bulunan tüm geçerli görüntü dosyalarını (PNG, JPG, JPEG, WEBP) yükler. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
