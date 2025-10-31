> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/tr.md)

Görüntüleri eşzamanlı olarak prompt ve en-boy oranına dayalı olarak oluşturur. Bu düğüm, metin açıklamalarını kullanarak görüntüler oluşturur ve çeşitli referans girdileri aracılığıyla görüntü boyutlarını ve stilini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Görüntü oluşturma için prompt (varsayılan: boş string) |
| `model` | COMBO | Evet | Birden fazla seçenek mevcut | Görüntü oluşturma için model seçimi |
| `aspect_ratio` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan görüntü için en-boy oranı (varsayılan: 16:9 oranı) |
| `seed` | INT | Evet | 0 ile 18446744073709551615 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed; gerçek sonuçlar seed'den bağımsız olarak belirsizdir (varsayılan: 0) |
| `style_image_weight` | FLOAT | Hayır | 0.0 ile 1.0 arası | Stil görüntüsünün ağırlığı. style_image sağlanmazsa dikkate alınmaz (varsayılan: 1.0) |
| `image_luma_ref` | LUMA_REF | Hayır | - | Girdi görüntüleriyle oluşturmayı etkilemek için Luma Referans düğüm bağlantısı; en fazla 4 görüntü dikkate alınabilir |
| `style_image` | IMAGE | Hayır | - | Stil referans görüntüsü; sadece 1 görüntü kullanılacaktır |
| `character_image` | IMAGE | Hayır | - | Karakter referans görüntüleri; birden fazla görüntüden oluşan bir batch olabilir, en fazla 4 görüntü dikkate alınabilir |

**Parametre Kısıtlamaları:**

- `image_luma_ref` parametresi en fazla 4 referans görüntüsü kabul edebilir
- `character_image` parametresi en fazla 4 karakter referans görüntüsü kabul edebilir
- `style_image` parametresi sadece 1 stil referans görüntüsü kabul eder
- `style_image_weight` parametresi sadece `style_image` sağlandığında kullanılır

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Girdi parametrelerine dayalı olarak oluşturulan görüntü |