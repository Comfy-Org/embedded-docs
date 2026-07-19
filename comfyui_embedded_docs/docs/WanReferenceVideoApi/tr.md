# Wan Reference to Video

ComfyUI Wan Referans Videodan Video düğümü, bir veya daha fazla referans videosunun görsel görünümünü ve sesini, bir metin istemiyle birlikte kullanarak yeni bir video oluşturur. Referans malzemedeki karakterlerle tutarlılığı korurken, açıklamanıza dayalı olarak yeni içerik oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak belirli AI modeli. | COMBO | Evet | `"wan2.6-r2v"` |
| `istem` | Yeni video için öğelerin ve görsel özelliklerin bir açıklaması. İngilizce ve Çinceyi destekler. Referans videolardaki karakterlere atıfta bulunmak için `character1` ve `character2` gibi tanımlayıcılar kullanın. | STRING | Evet | - |
| `negatif_istem` | Oluşturulan videoda kaçınılması gereken öğelerin veya özelliklerin bir açıklaması. | STRING | Hayır | - |
| `referans_videolar` | Karakter görünümü ve sesi için referans olarak kullanılan video girişlerinin bir listesi. En az bir video sağlamalısınız. Her videoya `character1`, `character2` veya `character3` gibi bir ad atanabilir. | AUTOGROW | Evet | - |
| `boyut` | Çıktı videosu için çözünürlük ve en boy oranı. | COMBO | Evet | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` |
| `süre` | Oluşturulan videonun saniye cinsinden uzunluğu. Değer 5'in katı olmalıdır (varsayılan: 5). | INT | Evet | 5 ila 10 |
| `tohum` | Tekrarlanabilir sonuçlar için rastgele bir tohum değeri. 0 değeri rastgele bir tohum oluşturacaktır. | INT | Hayır | 0 ila 2147483647 |
| `çekim_türü` | Oluşturulan videonun tek bir sürekli çekim mi yoksa kesmeler içeren birden çok çekim mi olduğunu belirtir. | COMBO | Evet | `"single"`<br>`"multi"` |
| `filigran` | Etkinleştirildiğinde, son videoya AI tarafından oluşturulmuş bir filigran eklenir (varsayılan: False). | BOOLEAN | Hayır | - |

**Kısıtlamalar:**

* `reference_videos` içinde sağlanan her video 2 ila 30 saniye arasında olmalıdır.
* `duration` parametresi belirli değerlerle (5 veya 10 saniye) sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Yeni oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `ed29f0bd3a1b30a81c94896976c4f9ff7bf5d0bcafaba66d70be61fce1418962`
