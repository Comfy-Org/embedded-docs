# Vidu Q3 Başlangıç/Bitiş Kareden Videoya Oluşturma

Bu düğüm, sağlanan başlangıç karesi ile bitiş karesi arasında enterpolasyon yaparak, bir metin istemi rehberliğinde video oluşturur. Vidu Q3 modelini kullanarak iki görüntü arasında kesintisiz bir geçiş üretir ve belirtilen süre ve çözünürlükte bir video ortaya çıkarır.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. Bir seçenek seçilmesi, `resolution`, `duration` ve `audio` için ek yapılandırma parametrelerini ortaya çıkarır. | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `first_frame` | Video dizisi için başlangıç görüntüsü. | IMAGE | Evet | - |
| `end_frame` | Video dizisi için bitiş görüntüsü. | IMAGE | Evet | - |
| `prompt` | İstem açıklaması (en fazla 2000 karakter). | STRING | Evet | - |
| `seed` | Oluşturmanın rastgeleliğini kontrol etmek için kullanılan tohum değeri (varsayılan: 1). | INT | Hayır | 0 ila 2147483647 |

### viduq3-pro ve viduq3-turbo Girdileri

Aşağıdaki parametreler her iki model seçeneği tarafından da (`viduq3-pro` ve `viduq3-turbo`) paylaşılır. Bir model seçildikten sonra görüntülenirler.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | Çıktı videosunun çözünürlüğü. Bu parametre, bir `model` seçildikten sonra görüntülenir. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `model.duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). Bu parametre, bir `model` seçildikten sonra görüntülenir. | INT | Evet | 1 ila 16 |
| `model.audio` | Etkinleştirildiğinde, videoyu sesle (diyaloglar ve ses efektleri dahil) çıkarır (varsayılan: False). Bu parametre, bir `model` seçildikten sonra görüntülenir. | BOOLEAN | Evet | `True`<br>`False` |

**Not:** En iyi sonuçlar için `first_frame` ve `end_frame` görüntüleri benzer en-boy oranlarına sahip olmalıdır. İki görüntünün en-boy oranı birbirinin %80'i ile %125'i arasında olmalıdır (göreli yakınlık 0,8 ile 1,25 arasında).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
