> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/tr.md)

Bu düğüm, Kling AI modelini kullanarak bir metin açıklamasından video oluşturur. İsteğinizi uzak bir API'ye gönderir ve oluşturulan videoyu döndürür. Düğüm, videonun uzunluğu, şekli ve kalitesini kontrol etmenizi sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-video-o1"` | Video oluşturma için kullanılacak belirli Kling modeli. |
| `prompt` | STRING | Evet | 1 ila 2500 karakter | Video içeriğini tanımlayan bir metin isteği. Bu, hem olumlu hem de olumsuz açıklamalar içerebilir. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulacak videonun şekli veya boyutları. |
| `duration` | COMBO | Evet | `5`<br>`10` | Videonun saniye cinsinden uzunluğu. |
| `resolution` | COMBO | Hayır | `"1080p"`<br>`"720p"` | Videonun kalitesi veya piksel çözünürlüğü (varsayılan: `"1080p"`). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Sağlanan metin isteğine dayalı olarak oluşturulan video. |
