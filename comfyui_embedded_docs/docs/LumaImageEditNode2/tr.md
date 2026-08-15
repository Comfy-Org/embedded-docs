# Luma UNI-1 Image Edit

Bu düğüm, Luma UNI-1 modeli tarafından desteklenen bir metin istemi kullanarak mevcut bir görseli düzenler. Kaynak görseli ve istenen değişikliğin açıklamasını alır, ardından görselin yeni bir düzenlenmiş sürümünü oluşturur. `uni-1` ve `uni-1-max` modelleri arasında seçim yapabilir, stili ayarlayabilir, web aramasını etkinleştirebilir ve isteğe bağlı olarak 8'e kadar referans görseli sağlayabilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Düzenleme için kullanılacak model. Bir model seçmek, aşağıdaki modele özgü seçenekleri ortaya çıkarır. | MODEL | Evet | `"uni-1"`<br>`"uni-1-max"` |
| `source` | Düzenlenecek kaynak görsel. | IMAGE | Evet | - |
| `prompt` | İstenen düzenlemenin açıklaması. 1–6000 karakter. Varsayılan: "" (boş dize; en az bir karakter girilene kadar istek geçersizdir). | STRING | Evet | 1 ile 6000 karakter arası |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 ile 2147483647 arası |

### uni-1 ve uni-1-max Girdileri

Bu seçenekler hem `uni-1` hem de `uni-1-max` modelleri tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `style` | Stil ön ayarı. `"auto"`, isteme göre seçim yapar; `"manga"`, manga/anime estetiği uygular ve dikey bir en-boy oranı gerektirir (2:3, 9:16, 1:2, 1:3). Varsayılan: `"auto"`. | STRING | Evet | `"auto"`<br>`"manga"` |
| `web_search` | Oluşturmadan önce görsel referanslar için web'de arama yapar. Varsayılan: false. | BOOLEAN | Evet | `true`<br>`false` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_ref` | Genişletilebilir yuva: stil/içerik rehberliği için 8'e kadar referans görseli bağlayın (`image_1` ile `image_8` arası). İsteğe bağlı. | IMAGE | Hayır | 0 ile 8 görsel arası |

**Notlar:**
- `prompt` 1 ile 6000 karakter arasında olmalıdır.
- `style`, `web_search` ve `image_ref` girdileri, `model` `"uni-1"` veya `"uni-1-max"` olarak ayarlandığında görünür.
- Her iki model de 8'e kadar referans görseli dahil aynı modele özgü seçenekleri destekler.
- `"manga"` stili, dikey bir en-boy oranı gerektirir (2:3, 9:16, 1:2 veya 1:3).
- 8'den fazla referans görseli bağlamak hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Luma UNI-1 modeli tarafından oluşturulan düzenlenmiş görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/tr.md)

---
**Source fingerprint (SHA-256):** `66f62bb2807759edb405c2caeeefe32c341920924e267c32449a620190b9a7ab`
