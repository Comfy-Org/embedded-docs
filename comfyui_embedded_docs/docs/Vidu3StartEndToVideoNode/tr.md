> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/tr.md)

Bu düğüm, sağlanan bir başlangıç karesi ile bir bitiş karesi arasında, bir metin istemi tarafından yönlendirilen bir enterpolasyon yaparak video oluşturur. İki görüntü arasında sorunsuz bir geçiş oluşturmak için Vidu Q3 modelini kullanır ve belirtilen süre ve çözünürlükte bir video üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` | Video oluşturma için kullanılacak model. Bir seçenek seçmek, `çözünürlük`, `süre` ve `ses` için ek yapılandırma parametrelerini görünür kılar. |
| `model.resolution` | COMBO | Evet | `"720p"`<br>`"1080p"` | Çıktı videosunun çözünürlüğü. Bu parametre bir `model` seçildikten sonra görünür hale gelir. |
| `model.duration` | INT | Evet | 1 ila 16 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). Bu parametre bir `model` seçildikten sonra görünür hale gelir. |
| `model.audio` | BOOLEAN | Evet | `True` / `False` | Etkinleştirildiğinde, sesli (diyalog ve ses efektleri dahil) video çıktısı verir (varsayılan: False). Bu parametre bir `model` seçildikten sonra görünür hale gelir. |
| `first_frame` | IMAGE | Evet | - | Video dizisi için başlangıç görüntüsü. |
| `end_frame` | IMAGE | Evet | - | Video dizisi için bitiş görüntüsü. |
| `prompt` | STRING | Evet | - | Video oluşturmayı yönlendiren bir metin açıklaması (maksimum 2000 karakter). |
| `seed` | INT | Hayır | 0 ila 2147483647 | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). |

**Not:** En iyi sonuçlar için `first_frame` ve `end_frame` görüntülerinin benzer en-boy oranlarına sahip olması önerilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |