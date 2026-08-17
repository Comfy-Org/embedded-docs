# Klasörden Görsel Veri Kümesi Yükle

Bu düğüm, seçilen bir klasörden bir görüntü veri kümesi yükler ve bunları bir liste olarak döndürür. Klasör, ComfyUI'nin ana giriş dizini içinde bir alt klasör olmalıdır. Desteklenen görüntü formatları PNG, JPG, JPEG ve WEBP'dir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görüntülerin yükleneceği klasör. Kullanılabilir seçenekler, ComfyUI'nin ana giriş dizininde bulunan alt klasörlerdir. Bu dizinin dışına çözümlenen değerler (örneğin, ".." kullanmak) reddedilir. | COMBO | Evet | *Birden fazla seçenek mevcuttur* — ComfyUI giriş dizininde bulunan alt klasörler |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Yüklenen görüntülerin listesi. Düğüm, seçilen klasörde bulunan tüm geçerli görüntü dosyalarını (PNG, JPG, JPEG, WEBP) yükler ve bunları bir liste olarak döndürür. Klasörde desteklenen görüntü dosyası yoksa bir hata oluşturulur. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
