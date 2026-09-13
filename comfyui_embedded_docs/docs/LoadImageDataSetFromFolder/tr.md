# Klasörden Görsel Veri Kümesi Yükle

Bu düğüm, ComfyUI'nin ana girdi dizini içindeki seçili bir alt klasörden birden çok görsel yükler ve bunları liste olarak döndürür. Seçilen klasörü PNG, JPG, JPEG veya WEBP biçimindeki görsel dosyaları için tarar; bu da onu toplu işleme veya görsel veri kümeleri hazırlama için kullanışlı hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görsellerin yükleneceği klasör. Seçenekler, ComfyUI'nin ana girdi dizininde bulunan alt klasörlerdir. | COMBO | Evet | Birden çok seçenek mevcut |

Not: Seçilen klasör, ComfyUI'nin ana girdi dizininin bir alt klasörü olmalıdır; dışına çıkan herhangi bir değer (örneğin `..`, mutlak yollar, sürücü harfleri veya sembolik bağlantılar kullanılarak) reddedilir. Yalnızca .png, .jpg, .jpeg veya .webp uzantılı dosyalar yüklenir ve uzantı kontrolü büyük/küçük harfe duyarsızdır. Yüklenen görseller RGB'ye dönüştürülür ve 0-1 aralığına ölçeklenir. Seçilen klasörde geçerli görsel dosyası yoksa düğüm bir hata verir. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Yüklenen görsellerin listesi. Düğüm, seçilen klasörde bulunan tüm geçerli görsel dosyalarını (PNG, JPG, JPEG, WEBP) yükler. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/tr.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
