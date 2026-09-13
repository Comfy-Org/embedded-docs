# VaeDecodeShapeTrellis

Bu düğüm, Trellis2 şekil latent temsillerini 3B bir mesh'e çözer. Seyrek şekil latent verilerini mesh geometrisine dönüştürmek için bir VAE kullanır ve ayrıca çözme işlemi sırasında üretilen şekil alt bölümleme verilerini de çıktı olarak verir. Düğüm, hem tek hem de toplu latent girdilerini destekler ve mesh yönünü beklenen koordinat çerçevesine otomatik olarak ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Çözülecek latent örnekleri; örnek tensörünü ve seyrek koordinat verilerini içerir. Latent sözlüğü ayrıca isteğe bağlı alanlar içerebilir: toplu şekiller için `coord_counts`, mesh çözünürlüğünü denetlemek için `coord_resolution` ve koordinat yönelimi için `model_frame`. | LATENT | Evet | None |
| `vae` | Şekil latentini bir mesh'e çözmek için kullanılan VAE modeli. | VAE | Evet | None |

### `samples` Hakkında Notlar

- `samples` girdisi, `samples` tensörünü ve `coords` seyrek koordinatlarını içermesi gereken bir latent sözlüğüdür.
- `coord_counts` mevcutsa, negatif olmayan tam sayılardan oluşan 1B bir tensör olmalıdır ve tüm sayımların toplamı toplam koordinat satırı sayısına eşit olmalıdır. Her sayım, toplu işlemdeki bir şekli temsil eder.
- `coord_resolution` sağlanırsa, mesh çözünürlüğü `coord_resolution * 16` olarak hesaplanır. Aksi takdirde, VAE'nin yerleşik çözünürlük arabelleği kullanılır (varsayılan değer: 1024).
- `model_frame`, `"z_up"` olarak ayarlanırsa, çözülen mesh tepe noktaları Z-up koordinat sisteminden glTF tarafından kullanılan Y-up kuralına döndürülür. Varsayılan değer `"y_up"`'tır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `mesh` | Çözülen 3B mesh; tepe noktası konumlarını ve yüz indekslerini içerir. Birden çok şekil çözülürken, tümü aynı şekle sahipse mesh'ler tek bir yığılmış tensör olarak, aksi takdirde paketlenmiş değişken boyutlu bir toplu işlem olarak döndürülür. | MESH |
| `shape_subdivides` | Çözme işleminin her aşamasında üretilen şekil alt bölümleme verileri. | SHAPE_SUBDIVIDES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/tr.md)

---
**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`
