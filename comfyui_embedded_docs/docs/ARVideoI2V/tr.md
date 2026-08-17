# ARVideoI2V

## Genel Bakış

Bu düğüm, AR (Otoregresif) video modelleri için görüntüden videoya üretim kurulumu hazırlar. Bir başlangıç görüntüsünü alır, bir VAE kullanarak bunu gizli uzaya kodlar ve kodlanmış görüntüyü modelin yapılandırmasında saklar. Bu, video örnekleme sürecinin görüntüyü ilk kare olarak kullanmasını sağlayarak, ayrı bir görüntüden videoya model mimarisine ihtiyaç duymadan üretimi etkili bir şekilde başlatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim için kullanılacak AR video modeli. | MODEL | Evet | - |
| `vae` | Başlangıç görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `start_image` | Oluşturulan videonun ilk karesi olarak kullanılacak başlangıç görüntüsü. | IMAGE | Evet | - |
| `width` | Oluşturulan video karelerinin genişliği (varsayılan: 832). | INT | Evet | 16 ile 8192 (adım: 16) |
| `height` | Oluşturulan video karelerinin yüksekliği (varsayılan: 480). | INT | Evet | 16 ile 8192 (adım: 16) |
| `length` | Oluşturulan videodaki toplam kare sayısı (varsayılan: 81). | INT | Evet | 1 ile 1024 (adım: 4) |
| `batch_size` | Tek bir yığında (batch) oluşturulacak video dizisi sayısı (varsayılan: 1). | INT | Evet | 1 ile 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Kodlanmış başlangıç görüntüsü, video üretimi için yapılandırmasında saklanan klonlanmış model. | MODEL |
| `LATENT` | Şekli [batch_size, 16, lat_t, height/8, width/8] olan boş bir gizli tensör; burada lat_t = ((length - 1) // 4) + 1, istenen video uzunluğundan türetilen gizli kare sayısıdır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/tr.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
