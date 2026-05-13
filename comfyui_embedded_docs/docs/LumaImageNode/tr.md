> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/tr.md)

Bir metin istemi ve en-boy oranına göre eşzamanlı olarak görseller oluşturur. Bu düğüm, metin açıklamalarını kullanarak görseller oluşturur ve karakter ile stil görselleri dahil olmak üzere çeşitli referans girdileri aracılığıyla görsel boyutlarını ve stilini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Görsel oluşturma için istem (varsayılan: boş dize). En az 3 karakter uzunluğunda olmalıdır. |
| `model` | COMBO | Evet | `photon-flash-1`<br>`photon-1`<br>`photon` | Görsel oluşturma için model seçimi. Farklı modellerin farklı maliyetleri vardır. |
| `aspect_ratio` | COMBO | Evet | `16:9`<br>`1:1`<br>`4:3`<br>`3:2`<br>`21:9`<br>`9:16`<br>`3:4`<br>`2:3`<br>`9:21` | Oluşturulan görsel için en-boy oranı (varsayılan: `16:9`) |
| `seed` | INT | Evet | 0 ile 18446744073709551615 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; tohumdan bağımsız olarak gerçek sonuçlar deterministik değildir (varsayılan: 0) |
| `style_image_weight` | FLOAT | Hayır | 0.0 ile 1.0 arası | Stil görselinin ağırlığı. `style_image` sağlanmazsa yok sayılır (varsayılan: 1.0) |
| `image_luma_ref` | LUMA_REF | Hayır | - | Girdi görselleriyle oluşturmayı etkilemek için Luma Referans düğümü bağlantısı; en fazla 4 görsel dikkate alınabilir. |
| `style_image` | IMAGE | Hayır | - | Stil referans görseli; yalnızca 1 görsel kullanılacaktır. |
| `character_image` | IMAGE | Hayır | - | Karakter referans görselleri; birden fazla görselden oluşan bir grup olabilir, en fazla 4 görsel dikkate alınabilir. |

**Parametre Kısıtlamaları:**

- `prompt` parametresi, boşluklar temizlendikten sonra en az 3 karakter uzunluğunda olmalıdır.
- `image_luma_ref` parametresi en fazla 4 referans görseli kabul edebilir.
- `character_image` parametresi en fazla 4 karakter referans görseli kabul edebilir.
- `style_image` parametresi yalnızca 1 stil referans görseli kabul eder.
- `style_image_weight` parametresi yalnızca `style_image` sağlandığında kullanılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Girdi parametrelerine göre oluşturulan görsel. |

---
**Source fingerprint (SHA-256):** `f7878cd4df62c2f364e4e404215b18bf2f5745fb071ae2cd931d5e34b84eab46`
