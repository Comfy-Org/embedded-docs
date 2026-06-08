Bu, sağlanan bir başlangıç karesi ile bitiş karesi arasında enterpolasyon yaparak, bir metin istemi rehberliğinde video oluşturan bir düğümdür. İki görüntü arasında kesintisiz bir geçiş oluşturmak için Vidu Q3 modelini kullanarak belirtilen süre ve çözünürlükte bir video üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak model. Bir seçenek belirlenmesi, `resolution`, `duration` ve `audio` için ek yapılandırma parametrelerini ortaya çıkarır. | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.resolution` | Çıktı videosunun çözünürlüğü. Bu parametre, bir `model` seçildikten sonra görünür hale gelir. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `model.duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). Bu parametre, bir `model` seçildikten sonra görünür hale gelir. | INT | Evet | 1 ila 16 |
| `model.audio` | Etkinleştirildiğinde, videoyu sesli olarak (diyalog ve ses efektleri dahil) çıkarır (varsayılan: False). Bu parametre, bir `model` seçildikten sonra görünür hale gelir. | BOOLEAN | Evet | `True` / `False` |
| `ilk kare` | Video dizisi için başlangıç görüntüsü. | IMAGE | Evet | - |
| `bitiş karesi` | Video dizisi için bitiş görüntüsü. | IMAGE | Evet | - |
| `komut istemi` | Video oluşturmayı yönlendiren metin açıklaması (maksimum 2000 karakter). | STRING | Evet | - |
| `tohum` | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). | INT | Hayır | 0 ila 2147483647 |

**Not:** En iyi sonuçlar için `first_frame` ve `end_frame` görüntüleri benzer en-boy oranlarına sahip olmalıdır. İki görüntünün en-boy oranı birbirinin %80 ila %125'i arasında olmalıdır (0,8 ile 1,25 arasında göreceli bir yakınlık).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `4a0a8d6657702d80278dc9239370683f408d7c051e91e8396939b7b81b87b4ed`
