# SAM3 Tespit

## Genel Bakış

SAM3 Algılama düğümü, metin açıklamaları, sınırlayıcı kutular veya nokta istemleri kullanarak açık sözcük dağarcığıyla algılama ve bölütleme gerçekleştirir. Metin olarak tanımladıklarınıza, kutu çizdiğiniz yerlere veya nokta tıkladığınız konumlara göre bir görüntüdeki nesneleri tanımlayabilir ve bölütleyebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Algılama ve bölütleme için kullanılacak SAM3 modeli | MODEL | Evet | - |
| `görüntü` | İşlenecek giriş görüntüsü | IMAGE | Evet | - |
| `koşullandırma` | CLIPTextEncode'dan metin koşullandırması. Metin istemleri kullanılarak algılama yapılırken gereklidir | CONDITIONING | Hayır | - |
| `sınırlayıcı_kutular` | İçinde bölütleme yapılacak sınırlayıcı kutular. Tek bir kutu (tüm karelere uygulanır), kutu listesi (tüm karelere uygulanır) veya liste listesi (kare başına kutular) olabilir. Metin koşullandırması olmadan sağlandığında, düğüm her kutunun içini bölütler | BOUNDING_BOX | Hayır | - |
| `pozitif_koordinatlar` | JSON formatında pozitif nokta istemleri `[{"x": int, "y": int}, ...]` piksel koordinatları kullanılarak. Bunlar bölütlemeye dahil etmek istediğiniz noktalardır | STRING | Hayır | - |
| `negatif_koordinatlar` | JSON formatında negatif nokta istemleri `[{"x": int, "y": int}, ...]` piksel koordinatları kullanılarak. Bunlar bölütlemeden çıkarmak istediğiniz noktalardır | STRING | Hayır | - |
| `eşik` | Metin tabanlı algılamalar için güven eşiği. Bu değerin üzerinde puana sahip algılamalar korunur (varsayılan: 0.5) | FLOAT | Hayır | 0.0 ile 1.0 |
| `iyileştirme_iterasyonları` | SAM kodlayıcı iyileştirme geçiş sayısı. Daha yüksek değerler maske kalitesini artırabilir. İyileştirme olmadan ham dedektör maskelerini kullanmak için 0 olarak ayarlayın (varsayılan: 2) | INT | Hayır | 0 ile 5 |
| `bireysel_maskeler` | Etkinleştirildiğinde, algılanan her nesne için ayrı maskeler çıktı olarak verir, tek bir maskede birleştirmek yerine (varsayılan: False) | BOOLEAN | Hayır | True/False |

### Parametre Kısıtlamaları ve Notlar

- **Metin istemleri**: Metin tabanlı algılama kullanmak için `conditioning` girişi sağlamalısınız. Metin koşullandırması sağlandığında, düğüm görüntü üzerinde metin yönlendirmeli algılama çalıştırır.
- **Kutu istemleri**: `bboxes` metin koşullandırması olmadan sağlandığında, düğüm her sınırlayıcı kutunun içindeki alanı bölütler.
- **Nokta istemleri**: `positive_coords` veya `negative_coords` sağlandığında, düğüm nokta tabanlı bölütleme kullanır. Noktalar otomatik olarak modelin iç çözünürlüğüne ölçeklenir.
- **Birden çok istem türü**: Farklı istem türlerini birleştirebilirsiniz. Örneğin, metin algılamasını belirli alanlarla sınırlamak için hem metin koşullandırması hem de sınırlayıcı kutular sağlayabilirsiniz.
- **Toplu işleme**: Düğüm toplu görüntüleri destekler. Birden çok kare işlenirken, sınırlayıcı kutular liste listesi formatı kullanılarak kare başına sağlanabilir.
- **Noktalar için JSON formatı**: Nokta koordinatları, `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]` formatında geçerli JSON dizeleri olarak sağlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sınırlayıcı_kutular` | Bölütleme maskeleri. `bireysel_maskeler` False (varsayılan) olduğunda, kare başına tek bir birleşik maske döndürür. True olduğunda, algılanan her nesne için ayrı maskeler döndürür | MASK |
| `sınırlayıcı_kutular` | Koordinatlar ve güven puanlarıyla algılanan sınırlayıcı kutular. Her kutu `x`, `y`, `width`, `height` ve `score` değerlerini içerir | BOUNDING_BOX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/tr.md)

---
**Source fingerprint (SHA-256):** `d073bda7eca934f3c64e1be740f5fb5249d27046a8be5902ea5d2245d5f679ea`
