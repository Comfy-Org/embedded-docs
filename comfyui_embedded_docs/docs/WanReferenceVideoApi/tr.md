> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/tr.md)

ComfyUI Wan Referans Videodan Video düğümü, bir veya daha fazla referans videosunun görsel görünümünü ve sesini, bir metin istemiyle birlikte kullanarak yeni bir video oluşturur. Referans malzemedeki karakterlerle tutarlılığı korurken, açıklamanıza dayalı olarak yeni içerik oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"wan2.6-r2v"` | Video oluşturma için kullanılacak belirli AI modeli. |
| `istem` | STRING | Evet | - | Yeni video için öğelerin ve görsel özelliklerin bir açıklaması. İngilizce ve Çinceyi destekler. Referans videolardaki karakterlere atıfta bulunmak için `character1` ve `character2` gibi tanımlayıcılar kullanın. |
| `negatif_istem` | STRING | Hayır | - | Oluşturulan videoda kaçınılması gereken öğelerin veya özelliklerin bir açıklaması. |
| `referans_videolar` | AUTOGROW | Evet | - | Karakter görünümü ve sesi için referans olarak kullanılan video girişlerinin bir listesi. En az bir video sağlamalısınız. Her videoya `character1`, `character2` veya `character3` gibi bir ad atanabilir. |
| `boyut` | COMBO | Evet | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` | Çıktı videosu için çözünürlük ve en boy oranı. |
| `süre` | INT | Evet | 5 ila 10 | Oluşturulan videonun saniye cinsinden uzunluğu. Değer 5'in katı olmalıdır (varsayılan: 5). |
| `tohum` | INT | Hayır | 0 ila 2147483647 | Tekrarlanabilir sonuçlar için rastgele bir tohum değeri. 0 değeri rastgele bir tohum oluşturacaktır. |
| `çekim_türü` | COMBO | Evet | `"single"`<br>`"multi"` | Oluşturulan videonun tek bir sürekli çekim mi yoksa kesmeler içeren birden çok çekim mi olduğunu belirtir. |
| `filigran` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, son videoya AI tarafından oluşturulmuş bir filigran eklenir (varsayılan: False). |

**Kısıtlamalar:**

* `reference_videos` içinde sağlanan her video 2 ila 30 saniye arasında olmalıdır.
* `duration` parametresi belirli değerlerle (5 veya 10 saniye) sınırlıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Yeni oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `ed29f0bd3a1b30a81c94896976c4f9ff7bf5d0bcafaba66d70be61fce1418962`
