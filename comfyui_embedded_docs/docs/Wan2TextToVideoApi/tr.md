# Wan 2.7 Metinden Videoya

Bu düğüm, Wan 2.7 modelini kullanarak bir metin açıklamasından video üretir. İsteminizi Wan video oluşturma API'sine gönderir, görevin tamamlanmasını bekler ve sonuçtaki videoyu döndürür. İsteğe bağlı olarak, videonun hareketini ve zamanlamasını etkilemek için bir ses klibi bağlayabilirsiniz; ses sağlanmazsa, model otomatik olarak eşleşen ses üretir.

## Girdiler

### Ortak Girdiler

Bu girdiler düğümün en üst seviyesinde her zaman kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak belirli model. | DYNAMIC_COMBO | Evet | `"wan2.7-t2v"` |
| `ses` | Video oluşturmayı yönlendiren ses (örn. dudak senkronizasyonu, ritim eşlemeli hareket). Süre: 3sn-30sn. Sağlanmazsa, model otomatik olarak eşleşen arka plan müziği veya ses efektleri üretir. | AUDIO | Hayır | - |
| `tohum` | Üretim için kullanılacak tohum (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `istem_genişlet` | İstemin AI yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: True). | BOOLEAN | Evet | True<br>False |
| `filigran` | Sonuca AI tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Evet | True<br>False |

### wan2.7-t2v Girdileri

Bu ayarlar, `wan2.7-t2v` modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çince destekler. | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif istem. Varsayılan boş bir dizedir. | STRING | Hayır | - |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"720P"`<br>`"1080P"` |
| `ratio` | Çıktı videosunun en boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 2 ile 15 |

**Not:** `prompt` girdisi boş olmamalıdır. `audio` girdisi isteğe bağlıdır; sağlanırsa, düğüm 1,5 ile 60 saniye arasında ses kabul eder, ancak araç ipucu 3sn-30sn önerir. Ses sağlanmazsa, model otomatik olarak eşleşen ses üretir. `negative_prompt` boş bırakıldığında API'ye gönderilmez. `prompt_extend` ve `watermark` gelişmiş seçeneklerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`
