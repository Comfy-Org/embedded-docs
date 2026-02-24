> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/tr.md)

Bu düğüm, Kling AI modelini kullanarak bir metin istemine ve en fazla yedi referans görseline dayalı olarak bir video oluşturur. Videoların en-boy oranını, süresini ve çözünürlüğünü kontrol etmenize olanak tanır. Düğüm, isteği harici bir API'ye gönderir ve oluşturulan videoyu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-video-o1"` | Video oluşturma için kullanılacak belirli Kling modeli. |
| `prompt` | STRING | Evet | - | Video içeriğini tanımlayan bir metin istemi. Bu, hem olumlu hem de olumsuz açıklamalar içerebilir. Metin otomatik olarak normalleştirilir ve 1 ile 2500 karakter arasında olmalıdır. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulacak video için istenen en-boy oranı. |
| `duration` | INT | Evet | 3 ila 10 | Videoyun saniye cinsinden uzunluğu. Değer bir kaydırıcı ile ayarlanabilir (varsayılan: 3). |
| `reference_images` | IMAGE | Evet | - | En fazla 7 referans görseli. Her görsel en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. |
| `resolution` | COMBO | Hayır | `"1080p"`<br>`"720p"` | Videoyun çıktı çözünürlüğü. Bu parametre isteğe bağlıdır (varsayılan: "1080p"). |

**Not:** `reference_images` girişi maksimum 7 görsel kabul eder. Daha fazlası sağlanırsa, düğüm bir hata verecektir. Her görsel minimum boyutlar ve en-boy oranı için doğrulanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |
