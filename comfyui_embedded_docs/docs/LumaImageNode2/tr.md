# Luma UNI-1 Image

Bu düğüm, Luma UNI-1 modelini kullanarak metin açıklamalarından görüntüler oluşturur. Bir metin istemi ile en-boy oranı ve stil gibi isteğe bağlı ayarları alır, ardından görüntü oluşturmak için isteği Luma API'sine gönderir. İki model varyantı mevcuttur: `uni-1` ve `uni-1-max`.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | İstenen görüntünün metin açıklaması. 1–6000 karakter. (varsayılan: "") | STRING | Evet | 1 ila 6000 karakter |
| `model` | Oluşturma için kullanılacak model. Bir model seçmek, o model için ek ayarları gösterir. (varsayılan: ilk seçenek, `"uni-1"`) | DYNAMIC_COMBO | Evet | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |

### uni-1 ve uni-1-max Girdileri

`uni-1` ve `uni-1-max` model seçenekleri tarafından paylaşılır. Bu ayarlar, iki modelden biri seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı. `"auto"`, modelin isteme göre seçmesini sağlar. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Stil ön ayarı. `"auto"`, isteme göre seçim yapar; `"manga"` manga/anime estetiği uygular ve dikey en-boy oranı gerektirir (2:3, 9:16, 1:2, 1:3). (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"manga"` |
| `web_search` | Oluşturmadan önce görsel referanslar için web'de arama yapın. (varsayılan: False) | BOOLEAN | Evet | True / False |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image_ref` | Büyütülebilir yuva: 1 ila 9 öğe bağlayın (örn. `image_1` ile `image_9`). Stil/içerik yönlendirmesi için en fazla 9 referans görüntüsü. | IMAGE | Hayır | En fazla 9 görüntü |

**Not:** `style` `"manga"` olarak ayarlanmışsa, `aspect_ratio` ya `"auto"` ya da dikey oranlardan biri olan `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"` olmalıdır. `"manga"` stiliyle başka bir oran kullanmak hataya neden olur. Referans görüntülerinin maksimum sayısı hem `uni-1` hem de `uni-1-max` için 9'dur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Oluşturulan görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/tr.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`
