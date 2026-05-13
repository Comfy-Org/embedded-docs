> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/tr.md)

Vidu Q3 Metinden Videoya Oluşturma düğümü, bir metin açıklamasından video oluşturur. Vidu Q3 Pro veya Q3 Turbo modelini kullanarak, isteminize göre video içeriği üretir; videonun uzunluğunu, çözünürlüğünü, en boy oranını ve ses içerip içermediğini kontrol etmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"viduq3-pro"`<br>`"viduq3-turbo"` | Video oluşturma için kullanılacak model. Bir model seçmek, en boy oranı, çözünürlük, süre ve ses için ek yapılandırma parametrelerini ortaya çıkarır. |
| `model.aspect_ratio` | COMBO | Evet* | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` | Çıktı videosunun en boy oranı. Bu parametre, bir `model` seçildiğinde görünür hale gelir. |
| `model.resolution` | COMBO | Evet* | `"720p"`<br>`"1080p"` | Çıktı videosunun çözünürlüğü. Bu parametre, bir `model` seçildiğinde görünür hale gelir. |
| `model.duration` | INT | Evet* | 1 ila 16 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). Bu parametre, bir `model` seçildiğinde görünür hale gelir. |
| `model.audio` | BOOLEAN | Evet* | Doğru/Yanlış | Etkinleştirildiğinde, videoyu sesle (diyalog ve ses efektleri dahil) çıkarır (varsayılan: Yanlış). Bu parametre, bir `model` seçildiğinde görünür hale gelir. |
| `prompt` | STRING | Evet | Yok | Video oluşturma için metinsel bir açıklama, maksimum 2000 karakter uzunluğunda. |
| `seed` | INT | Hayır | 0 ila 2147483647 | Oluşturmanın rastgeleliğini kontrol etmek için bir tohum değeri (varsayılan: 1). |

*Not: `aspect_ratio`, `resolution`, `duration` ve `audio` parametreleri, bir `model` seçildikten sonra zorunlu hale gelir çünkü bunlar modelin yapılandırmasının bir parçasıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `a98b6c3093d659a5a4344c2c495063acf47a7922bf7d1fc851c3b8d8c0c87c5e`
