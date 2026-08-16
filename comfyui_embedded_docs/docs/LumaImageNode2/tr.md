# Luma UNI-1 Image

## Genel Bakış

Bu düğüm, Luma UNI-1 modelini kullanarak metin açıklamalarından görüntü üretir. Metin istemi ve en boy oranı, stil gibi isteğe bağlı ayarları alır, ardından görüntü oluşturmak için isteği Luma API'sine gönderir. İki model çeşidi mevcuttur: `uni-1` ve `uni-1-max`.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim için kullanılacak model. Bir model seçmek, o modele özel ek ayarları görüntüler. | DYNAMIC_COMBO | Evet | `"uni-1"`<br>`"uni-1-max"` |
| `prompt` | İstenen görüntünün metin açıklaması. 1–6000 karakter. | STRING | Evet | 1 ila 6000 karakter |
| `seed` | Seed (tohum), düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak belirlenimci değildir. (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |

### uni-1 ve uni-1-max Girdileri

`uni-1` ve `uni-1-max` model seçenekleri tarafından paylaşılır. Bu ayarlar, her iki modelden biri seçildiğinde görüntülenir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Çıktı görüntüsünün en boy oranı. `"auto"`, modelin isteme göre seçim yapmasını sağlar. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Stil ön ayarı. `"auto"` isteme göre seçer; `"manga"` manga/anime estetiği uygular ve dikey bir en boy oranı (2:3, 9:16, 1:2, 1:3) gerektirir. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"manga"` |
| `web_search` | Üretimden önce web'de görsel referans araması yapar. (varsayılan: False) | BOOLEAN | Evet | True / False |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image_ref` | Büyütülebilir yuva: 1 ila 9 öğe bağlayın (örn. `image_1` ile `image_9` arası). Stil/içerik rehberliği için en fazla 9 referans görüntüsü. | IMAGE | Hayır | En fazla 9 görüntü |

**Not:** `style` değeri `"manga"` olarak ayarlanmışsa, `aspect_ratio` değeri `"auto"` veya dikey oranlardan biri (`"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`) olmalıdır. `"manga"` stiliyle başka bir oran kullanmak hataya neden olur. Hem `uni-1` hem de `uni-1-max` için maksimum referans görüntüsü sayısı 9'dur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan görüntü, tensör olarak. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/tr.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`
