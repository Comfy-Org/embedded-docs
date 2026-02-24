> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/tr.md)

Wan Referanstan Video düğümü, bir veya daha fazla girdi referans videosundan görsel görünüm ve sesi, bir metin istemiyle birlikte kullanarak yeni bir video oluşturur. Referans materyalindeki karakterlerle tutarlılığı korurken, açıklamanıza dayalı yeni içerik oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"wan2.6-r2v"` | Video oluşturma için kullanılacak belirli AI modeli. |
| `prompt` | STRING | Evet | - | Yeni video için öğelerin ve görsel özelliklerin açıklaması. İngilizce ve Çince destekler. Referans videolardaki karakterlere atıfta bulunmak için `character1` ve `character2` gibi tanımlayıcılar kullanın. |
| `negative_prompt` | STRING | Hayır | - | Oluşturulan videoda kaçınılması gereken öğelerin veya özelliklerin açıklaması. |
| `reference_videos` | AUTOGROW | Evet | - | Karakter görünümü ve sesi için referans olarak kullanılan video girdilerinin listesi. En az bir video sağlamalısınız. Her videoya `character1`, `character2` veya `character3` gibi bir isim atanabilir. |
| `size` | COMBO | Evet | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` | Çıktı videosu için çözünürlük ve en-boy oranı. |
| `duration` | INT | Evet | 5 ila 10 | Oluşturulan videonun saniye cinsinden uzunluğu. Değer 5'in katı olmalıdır (varsayılan: 5). |
| `seed` | INT | Hayır | 0 ila 2147483647 | Tekrarlanabilir sonuçlar için rastgele tohum değeri. 0 değeri rastgele bir tohum oluşturacaktır. |
| `shot_type` | COMBO | Evet | `"single"`<br>`"multi"` | Oluşturulan videonun tek bir sürekli çekim mi yoksa kesmeler içeren birden fazla çekim mi içerdiğini belirtir. |
| `watermark` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, son videoya AI tarafından oluşturulmuş bir filigran eklenir (varsayılan: False). |

**Kısıtlamalar:**

* `reference_videos` içinde sağlanan her video 2 ila 30 saniye arasında bir süreye sahip olmalıdır.
* `duration` parametresi belirli değerlerle (5 veya 10 saniye) sınırlıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Yeni oluşturulan video dosyası. |
