# Vidu Çok Kareli Video Üretimi

Bu düğüm, birden çok anahtar kare arasında geçişler oluşturarak bir video üretir. Bir başlangıç görüntüsünden başlar ve kullanıcı tanımlı bitiş görüntüleri ile istemlerden oluşan bir dizi boyunca animasyon oluşturur; çıktı olarak tek bir video dosyası üretir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak Vidu modeli. | COMBO | Evet | "viduq2-pro"<br>"viduq2-turbo" |
| `start_image` | Başlangıç kare görüntüsü. En-boy oranı 1:4 ile 4:1 arasında olmalıdır. | IMAGE | Evet | En-boy oranı 1:4 ila 4:1 |
| `seed` | Yeniden üretilebilir sonuçları sağlamak için rastgele sayı üretimine yönelik tohum değeri (varsayılan: 1). | INT | Evet | 0 - 2147483647 |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "720p"<br>"1080p" |
| `frames` | Anahtar kare geçişlerinin sayısı (2-9). Bir değer seçmek, her kare için gerekli girdileri dinamik olarak gösterir. | DYNAMIC_COMBO | Evet | "2"<br>"3"<br>"4"<br>"5"<br>"6"<br>"7"<br>"8"<br>"9" |

### Kare Girdileri (tüm kare sayısı seçenekleri tarafından paylaşılır)

`frames` bir sayıya ayarlandığında, 1'den o sayıya kadar her `i` karesi için aşağıdaki üç girdi gösterilir. Örneğin, "3" seçildiğinde `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2` ve `prompt3` / `end_image3` / `duration3` eklenir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt{i}` | Kare {i} geçişi için metin istemi. Çok satırlı metin alanı. En fazla 2000 karakter. | STRING | Evet | En fazla 2000 karakter |
| `end_image{i}` | {i} segmenti için bitiş kare görüntüsü. En-boy oranı 1:4 ile 4:1 arasında olmalıdır. | IMAGE | Evet | En-boy oranı 1:4 ila 4:1 |
| `duration{i}` | {i} segmenti için saniye cinsinden süre (varsayılan: 4). | INT | Evet | 2 - 7 |

**Notlar:**

- Tüm girdiler zorunludur. `seed` varsayılan bir değere sahiptir ancak yine de zorunlu bir girdidir.
- `start_image` ve her `end_image{i}` 1:4 ile 4:1 arasında bir en-boy oranına sahip olmalıdır.
- Her `prompt{i}` en fazla 2000 karakter uzunluğundadır.
- Her `duration{i}` 2 ile 7 saniye arasında olmalıdır.
- Kare sayısı 2 ile 9 arasında olabilir, bu nedenle olası kare indeksleri 1'den 9'a kadar gider.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Tüm animasyonlu geçişleri içeren oluşturulmuş video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
