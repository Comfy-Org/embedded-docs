> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/tr.md)

Görüntüleri eşzamanlı olarak prompt ve en-boy oranına dayalı olarak oluşturur. Bu düğüm, metin açıklamalarını kullanarak görüntüler oluşturur ve çeşitli referans girdileri aracılığıyla görüntü boyutlarını ve stilini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görüntü oluşturma için prompt (varsayılan: boş string) |
| `model` | COMBO | Evet | Birden fazla seçenek mevcut | Görüntü oluşturma için model seçimi |
| `en_boy_oranı` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan görüntü için en-boy oranı (varsayılan: 16:9 oranı) |
| `tohum` | INT | Evet | 0 ile 18446744073709551615 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed; gerçek sonuçlar seed'den bağımsız olarak belirsizdir (varsayılan: 0) |
| `stil_görüntüsü_ağırlığı` | FLOAT | Hayır | 0.0 ile 1.0 arası | Stil görüntüsünün ağırlığı. style_image sağlanmazsa dikkate alınmaz (varsayılan: 1.0) |
| `görüntü_luma_referansı` | LUMA_REF | Hayır | - | Girdi görüntüleriyle oluşturmayı etkilemek için Luma Referans düğüm bağlantısı; en fazla 4 görüntü dikkate alınabilir |
| `stil_görüntüsü` | IMAGE | Hayır | - | Stil referans görüntüsü; sadece 1 görüntü kullanılacaktır |
| `karakter_görüntüsü` | IMAGE | Hayır | - | Karakter referans görüntüleri; birden fazla görüntüden oluşan bir batch olabilir, en fazla 4 görüntü dikkate alınabilir |

**Parametre Kısıtlamaları:**

- `image_luma_ref` parametresi en fazla 4 referans görüntüsü kabul edebilir
- `character_image` parametresi en fazla 4 karakter referans görüntüsü kabul edebilir
- `style_image` parametresi sadece 1 stil referans görüntüsü kabul eder
- `style_image_weight` parametresi sadece `style_image` sağlandığında kullanılır

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Girdi parametrelerine dayalı olarak oluşturulan görüntü |