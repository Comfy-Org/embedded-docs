# Wan 2.7 Metinden Videoya

Bu düğüm, Wan 2.7 modelini kullanarak bir metin açıklamasından video oluşturur. İsteğinizi harici bir API'ye gönderir; API, istemi işler ve bir video dosyası döndürür. İsteğe bağlı olarak, videonun hareketini ve zamanlamasını etkilemek için bir ses klibi sağlayabilirsiniz.

## Girdiler

Girdiler, `wan2.7-t2v` modeli seçildiğinde görünen ortak ayarları ve modele özel ayarları içerir.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak belirli model. | COMBO | Evet | `"wan2.7-t2v"` |
| `audio` | Video oluşturmayı yönlendiren ses (örn. dudak senkronizasyonu, ritim eşlemeli hareket). Süre: 1.5sn-60sn. Sağlanmazsa, model otomatik olarak uygun arka plan müziği veya ses efektleri üretir. | AUDIO | Hayır | - |
| `seed` | Oluşturma için kullanılacak tohum (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |
| `prompt_extend` | İstemin yapay zeka yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True). | BOOLEAN | Hayır True / False |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır True / False |

### wan2.7-t2v Girdileri

Bu ayarlar, `wan2.7-t2v` modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif istem. | STRING | Hayır | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 ila 15 |

**Not:** `prompt` girdisi boş olmamalıdır. `audio` girdisi isteğe bağlıdır; sağlanırsa süresi 1,5 ile 60 saniye arasında olmalıdır. Atlanırsa, model otomatik olarak eşleşen ses üretir. `negative_prompt` boş bırakıldığında API'ye gönderilmez. `prompt_extend` ve `watermark` gelişmiş seçeneklerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`
