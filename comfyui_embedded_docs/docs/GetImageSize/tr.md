# Resim Boyutunu Al

## Genel Bakış

GetImageSize düğümü, bir giriş görüntüsünden boyut ve toplu iş bilgilerini çıkarır. Görüntünün genişlik, yükseklik ve toplu iş boyutunu döndürürken, bu bilgileri düğüm arayüzünde ilerleme metni olarak da görüntüler. Orijinal görüntü verileri değişmeden geçer.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Boyut bilgisinin çıkarılacağı giriş görüntüsü | IMAGE | Evet | - |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `width` | Giriş görüntüsünün piksel cinsinden genişliği | INT |
| `height` | Giriş görüntüsünün piksel cinsinden yüksekliği | INT |
| `batch_size` | Toplu işteki görüntü sayısı | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/tr.md)

---
**Source fingerprint (SHA-256):** `5cd19ae762d2403c6c5d0740cd5f8c17913daea737fddcff8f0d9da2210e82ab`
