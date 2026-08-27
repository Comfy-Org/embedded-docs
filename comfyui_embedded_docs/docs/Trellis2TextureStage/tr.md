# Trellis2TextureStage

Bu düğüm, Trellis2 üretimi için doku aşaması örnekleme geçişini ayarlar. Gelen şekil latent'inden koordinat düzenini ve voksel başına şekil latent'ini okur, aynı koordinat düzeninde 32 kanallı boş bir seyrek latent oluşturur ve gerekli doku aşaması meta verilerini koşullandırmaya ekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Doku üretim geçişinde kullanılan pozitif koşullandırma. Doku aşaması meta verileri buna eklenir. | CONDITIONING | Evet | - |
| `negative` | Doku üretim geçişinde kullanılan negatif koşullandırma. Doku aşaması meta verileri buna eklenir. | CONDITIONING | Evet | - |
| `shape_latent` | Trellis2ShapeStage veya Trellis2UpsampleStage tarafından üretilen latent sözlüğü. `coords` (koordinat düzeni, şekil [N, 4]) ve `samples` (voksel başına şekil latent'i) içermelidir; `coord_resolution` ve `model_frame` isteğe bağlıdır. | LATENT | Evet | - |

Notlar:
- `shape_latent`, Trellis2ShapeStage veya Trellis2UpsampleStage çıktısı olmalıdır; doku geçişinde kullanılan koordinat düzenini ve voksel başına şekil latent'ini sağlar.
- Koordinat düzeni doğrulanır: `coords` ilk sütunundaki batch kimlikleri negatif olmayan ve ardışık olmalıdır; toplam satır sayısı koordinat sayılarıyla eşleşmelidir.
- `positive` bir projeksiyon özellik paketi (Pixal3D koşullandırması) taşıdığında ve `shape_latent` `coord_resolution` içerdiğinde, 1024 doku çözünürlüğünde projeksiyon özellikleri hesaplanır ve koşullandırmaya eklenir.
- Model çerçevesi `shape_latent`'inden okunur; bulunmadığında, projeksiyon özellikleri mevcutsa `"y_up"`, aksi takdirde `"z_up"` varsayılan değeri kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Doku aşaması meta verileri eklenmiş pozitif koşullandırma (üretim modu, koordinatlar, koordinat sayıları, şekil latent'i, model çerçevesi ve varsa projeksiyon özellikleri). | CONDITIONING |
| `negative` | Aynı doku aşaması meta verileri eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Gelen şekil latent'iyle aynı koordinat düzeninde, 32 kanallı yeni bir boş seyrek latent. Sözlüğü `samples`, `type` ("trellis2"), `coords`, `coord_counts` ve `model_frame` içerir; `coord_resolution` varsa dahil edilir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/tr.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
