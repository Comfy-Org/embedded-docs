# VaeDecodeShapeTrellis

Bu düğüm, Trellis2 şekil latent temsillerini 3D mesh'e dönüştürür. Seyrek şekil latent verilerini mesh geometrisine dönüştürmek için bir VAE kullanır ve ayrıca kod çözme sırasında üretilen şekil alt bölüm verilerini çıktı olarak verir. Düğüm hem tek hem de toplu latent girdileri destekler ve mesh yönünü beklenen koordinat çerçevesine otomatik olarak ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Kod çözülecek latent örnekler; örnek tensörünü ve seyrek koordinat verilerini içerir. Latent sözlüğü ayrıca isteğe bağlı alanlar içerebilir: toplu şekiller için `coord_counts`, mesh çözünürlüğünü kontrol etmek için `coord_resolution` ve koordinat yönelimi için `model_frame`. | LATENT | Evet | None |
| `vae` | Şekil latentini mesh'e dönüştürmek için kullanılan VAE modeli. | VAE | Evet | None |

### `samples` Üzerine Notlar

- `samples` girdisi, `samples` tensörünü ve `coords` seyrek koordinatlarını içermesi gereken bir latent sözlüktür.
- `coord_counts` mevcutsa, negatif olmayan tam sayılardan oluşan 1 boyutlu bir tensör olmalıdır ve tüm sayıların toplamı toplam koordinat satırı sayısına eşit olmalıdır. Her sayı, toplu işlemdeki bir şekli temsil eder.
- `coord_resolution` sağlanırsa, mesh çözünürlüğü `coord_resolution * 16` olarak hesaplanır. Aksi takdirde, VAE'nin yerleşik çözünürlük arabelleği kullanılır (varsayılan değer: 1024).
- `model_frame` `"z_up"` olarak ayarlanırsa, kod çözülen mesh köşeleri Z-up koordinat sisteminden glTF tarafından kullanılan Y-up kuralına döndürülür. Varsayılan değer `"y_up"`tir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Kod çözülen 3D mesh; köşe konumlarını ve yüz indekslerini içerir. | MESH |
| `shape_subdivides` | Kod çözme işleminin her aşamasında üretilen şekil alt bölüm verileri. | SHAPE_SUBDIVIDES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/tr.md)

---
**Source fingerprint (SHA-256):** `50f1b8200bd750671473278aaf94e6b08d6f9a6a72d5d1dc882ea7ab87084681`
