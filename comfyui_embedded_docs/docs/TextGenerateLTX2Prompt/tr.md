# TextGenerateLTX2Prompt

TextGenerateLTX2Prompt düğümü, metin üretimi düğümünün özelleştirilmiş bir sürümüdür. Kullanıcının metin istemini alır ve bir dil modeline geliştirme veya tamamlama için göndermeden önce LTX2'ye özgü sistem talimatlarıyla otomatik olarak biçimlendirir. Düğüm, yalnızca metin veya görsel referanslı modda çalışabilir ve bağlı CLIP modeline göre biçimlendirmesini otomatik olarak uyarlar; Gemma 4 modelleri için LTX 2.4 istem biçimini, Gemma 3 modelleri için LTX 2.0 biçimini kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin kodlama için kullanılan CLIP modeli. Model, istem biçimini belirler: Gemma 4 modelleri LTX 2.4 biçimini, Gemma 3 modelleri LTX 2.0 biçimini kullanır. | CLIP | Evet |  |
| `prompt` | Geliştirilecek veya tamamlanacak kullanıcıdan gelen ham metin girişi. | STRING | Evet |  |
| `max_length` | Dil modelinin üretmesine izin verilen maksimum token sayısı. | INT | Evet |  |
| `sampling_mode` | Metin üretimi sırasında bir sonraki token'ı seçmek için kullanılan örnekleme stratejisi. | COMBO | Evet | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | İsteğe bağlı bir giriş görseli. Sağlandığında, düğüm görüntüden videoya üretim için görsel bağlamını içeren farklı bir sistem istemi kullanır. | IMAGE | Hayır |  |
| `thinking` | Etkinleştirildiğinde, model nihai yanıttan önce akıl yürütme sürecini çıktı olarak verir. Akıl yürütme bloğu nihai sonuçtan çıkarılır. | BOOLEAN | Hayır |  |
| `use_default_template` | Etkinleştirildiğinde, düğüm biçimlendirme için varsayılan sohbet şablonunu kullanır. | BOOLEAN | Hayır |  |
| `video` | Üretim için ek bağlam olarak kullanılabilen isteğe bağlı bir video girişi. | VIDEO | Hayır |  |
| `audio` | Üretim için ek bağlam olarak kullanılabilen isteğe bağlı bir ses girişi. | AUDIO | Hayır |  |

**Notlar:** Düğümün davranışı `image` girişinin varlığına göre değişir. Bir görsel sağlanırsa, istem, görselin içeriğine dayalı olarak istemi genişleten bir sistem istemi kullanılarak görüntüden videoya görevi için biçimlendirilir. Görsel sağlanmazsa, biçimlendirme, istemi ayrıntılı bir video üretim açıklamasına genişleten bir sistem istemi kullanılarak metinden videoya görevi içindir.

Bağlı `clip` modeli ayrıca biçimlendirmeyi etkiler: CLIP tokenlayıcı bir Gemma 4 modeli olduğunda, düğüm LTX 2.4 sohbet biçimini ve sistem istemlerini kullanır; aksi takdirde Gemma 3 / LTX 2.0 sohbet biçimini kullanır. Üretimden sonra, herhangi bir akıl yürütme bloğu (örneğin `<think>...</think>`) çıktıdan çıkarılır ve elde edilen metin boşsa, orijinal `prompt` döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Dil modeli tarafından üretilen, akıl yürütme içeriği çıkarılmış, geliştirilmiş veya tamamlanmış metin dizesi. Model hiçbir metin üretmezse, orijinal istem döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/tr.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
