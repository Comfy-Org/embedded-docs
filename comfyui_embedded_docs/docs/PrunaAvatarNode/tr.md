# Pruna P-Video-2 Pro Avatar

Pruna P-Video-2 Pro Avatar ile bir portreyi konuşan videoya dönüştürün. Metinden sese kullanarak bir senaryoyu seslendirin veya kendi sesinizi bağlayın; kişi bu sesle dudak senkronizasyonu yapsın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Videonun başladığı portre. 1:2 ile 4:1 arasındaki en-boy oranları korunur; 1:5 gibi daha uç görüntüler 9:16 veya 16:9 olarak kırpılır. | IMAGE | Evet | - |
| `speech` | Videoyu metinden sese senaryosuyla veya kendi sesinizle yönlendirin. Bir seçeneğin seçilmesi, ilgili girdilerini aşağıda gösterir. | DYNAMIC_COMBO | Evet | `"script"`<br>`"audio"` |
| `prompt` | Videoda ne görüneceğini açıklar (varsayılan: "The person is talking."). En fazla 5000 karakter. | STRING | Evet | En fazla 5000 karakter |
| `resolution` | Çıktı çözünürlüğü (varsayılan: `"768p"`). 1080p, 2k ve 4k, oluşturulan 768p videoyu yükseltir. | COMBO | Evet | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `enhance_prompt` | Portrede görülen hareketi (arka plan, ışıklar ve vücut hareketi gibi) prompt'a ekler (varsayılan: True). Gelişmiş ayar. | BOOLEAN | Evet | `True`<br>`False` |
| `seed` | Üretim için tohum (varsayılan: 42). Aynı tohum, yalnızca `enhance_prompt` kapalıyken bir sonucu tam olarak yeniden üretir. | INT | Evet | 0 ile 2147483647 arası<br>Adım: 1 |

### `"script"` Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `speech.script` | Kişinin söylediği sözcükler. Videonun süresi konuşmanın süresiyle eşleşir ve 3 dakikadan uzun konuşmalar 3 dakikada kesilir. | STRING | Evet | Herhangi bir metin |
| `speech.voice` | Konuşma için kullanılan ses (varsayılan: `"Zephyr (Female)"`). | COMBO | Evet | 30 hazır ses |
| `speech.language` | Senaryonun konuşulduğu dil (varsayılan: `"English (US)"`). | COMBO | Evet | `"English (US)"`<br>`"English (UK)"`<br>`"Spanish"`<br>`"French"`<br>`"German"`<br>`"Italian"`<br>`"Portuguese (Brazil)"`<br>`"Japanese"`<br>`"Korean"`<br>`"Hindi"` |
| `speech.voice_prompt` | Senaryonun nasıl konuşulacağı: ton, tempo, aksan, duygu (varsayılan: "Say the following."). Bu metin kendisi seslendirilmez. | STRING | Evet | Herhangi bir metin |

### `"audio"` Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `speech.audio` | Kişinin dudak senkronizasyonu yaptığı konuşma. Videonun süresi bunun uzunluğuyla eşleşir. | AUDIO | Evet | En az 1 saniye |

**Notlar:**

- Daha uzun çıktı, sesin uzunluğunu sınırlar: 2k en fazla 150 saniyelik ses kabul eder, 4k ise en fazla 60 saniyelik ses. Bu çözünürlüklerde daha uzun ses, düğümü hatayla durdurur; bu nedenle daha düşük bir çözünürlük veya daha kısa bir klip kullanın.
- Portrenin en-boy oranı çıktının şeklini belirler. Çok uzun veya çok geniş portreler doldurulmak yerine kırpılır; bu nedenle özneyi kenarlardan uzak tutun.
- `enhance_prompt` kapalıyken prompt yazıldığı gibi kullanılır; aynı tohumun bir sonucu tam olarak yeniden üretmesini sağlayan da budur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Portreden oluşturulan konuşan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaAvatarNode/tr.md)

---
**Source fingerprint (SHA-256):** `58efc7a110734f8da0a771371c5230908bf8226a946d69c5315e51e259630043`
