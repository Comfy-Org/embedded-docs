> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/tr.md)

Bu, sağlanan bir başlangıç karesi ile bitiş karesi arasında enterpolasyon yaparak, bir metin istemi rehberliğinde video oluşturan bir düğümdür. İki görüntü arasında kesintisiz bir geçiş oluşturmak için Vidu Q3 modelini kullanarak belirtilen süre ve çözünürlükte bir video üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` | Video oluşturma için kullanılacak model. Bir seçenek belirlenmesi, `resolution`, `duration` ve `audio` için ek yapılandırma parametrelerini ortaya çıkarır. |
| `model.resolution` | COMBO | Evet | `"720p"`<br>`"1080p"` | Çıktı videosunun çözünürlüğü. Bu parametre, bir `model` seçildikten sonra görünür hale gelir. |
| `model.duration` | INT | Evet | 1 ila 16 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). Bu parametre, bir `model` seçildikten sonra görünür hale gelir. |
| `model.audio` | BOOLEAN | Evet | `True` / `False` | Etkinleştirildiğinde, videoyu sesli olarak (diyalog ve ses efektleri dahil) çıkarır (varsayılan: False). Bu parametre, bir `model` seçildikten sonra görünür hale gelir. |
| `ilk kare` | IMAGE | Evet | - | Video dizisi için başlangıç görüntüsü. |
| `bitiş karesi` | IMAGE | Evet | - | Video dizisi için bitiş görüntüsü. |
| `komut istemi` | STRING | Evet | - | Video oluşturmayı yönlendiren metin açıklaması (maksimum 2000 karakter). |
| `tohum` | INT | Hayır | 0 ila 2147483647 | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). |

**Not:** En iyi sonuçlar için `first_frame` ve `end_frame` görüntüleri benzer en-boy oranlarına sahip olmalıdır. İki görüntünün en-boy oranı birbirinin %80 ila %125'i arasında olmalıdır (0,8 ile 1,25 arasında göreceli bir yakınlık).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `4a0a8d6657702d80278dc9239370683f408d7c051e91e8396939b7b81b87b4ed`
