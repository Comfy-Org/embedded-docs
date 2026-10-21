# VEED Fabric 1.0

VEED Fabric ile hareketsiz bir görüntüyü ve konuşma kaydını konuşan, dudakları senkronize edilmiş bir videoya dönüştürün. Yüz açıkça göründüğü sürece fotoğraflar, illüstrasyonlar ve maskotlarla çalışır; video görüntünün en-boy oranını korur ve sesin süresi kadar uzun olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak model. Bir model seçildiğinde ona özgü parametreler görünür: `image`, `audio` ve `resolution`. | DYNAMIC_COMBO | Evet | `"fabric-1.0"` |
| `image` | Yüzü net görünen görüntü. Video, en-boy oranını korur. | IMAGE | Evet | - |
| `audio` | Dudak senkronizasyonu yapılacak konuşma, 300 saniyeye kadar. Video uzunluğunu belirler. | AUDIO | Evet | 300 saniyeye kadar |
| `resolution` | Çıktı boyutu sınıfı: `"480p"` için yaklaşık 0,4 megapiksel (16:9'da 864x480) ve `"720p"` için 0,9 megapiksel (16:9'da 1312x736). (varsayılan: `"720p"`) | COMBO | Evet | `"480p"`<br>`"720p"` |

Konuşma kaydı 300 saniyeden uzun olduğunda düğüm hatayla durur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `VIDEO` | Konuşan video: konuşma kaydına uyacak şekilde hareketlendirilmiş giriş görüntüsü. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/tr.md)

---
**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`
