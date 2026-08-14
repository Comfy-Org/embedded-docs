# Kling Omni Görselden Videoya (Pro)

Bu düğüm, bir metin istemi ve en fazla yedi referans görseline dayalı video oluşturmak için Kling AI modelini kullanır. Videonun en-boy oranını, süresini ve çözünürlüğünü kontrol etmenize olanak tanır; isteğe bağlı olarak storyboard kullanabilir veya ses oluşturabilirsiniz. Düğüm isteği harici bir API'ye gönderir ve oluşturulan videoyu döndürür.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Video oluşturma için kullanılacak belirli Kling modeli (varsayılan: "kling-v3-omni"). | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Video içeriğini tanımlayan bir metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. `@image` veya `@video` gibi yer tutucular (isteğe bağlı olarak numaralandırılmış) otomatik olarak API uyumlu biçime dönüştürülür. 1 ile 2500 karakter arasında olmalıdır (storyboard'lar etkinleştirildiğinde boş olabilir). Storyboard'lar etkinleştirildiğinde yok sayılır. | STRING | Evet | - |
| `aspect_ratio` | Oluşturulan video için istenen en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Videonun saniye cinsinden uzunluğu; bir kaydırıcıyla ayarlanır (varsayılan: 5). | INT | Evet | 3 ile 15 arası |
| `reference_images` | En fazla 7 referans görseli. Her görsel en az 300x300 piksel olmalı ve 1:2.5 ile 2.5:1 arasında bir en-boy oranına sahip olmalıdır. | IMAGE | Evet | 1 ile 7 arası images |
| `resolution` | Videonun çıktı çözünürlüğü (varsayılan: "1080p"). | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Her biri ayrı istem ve süreye sahip bir dizi video segmenti oluşturur. Yalnızca `kling-v3-omni` için desteklenir. Etkinleştirildiğinde genel `prompt` yok sayılır ve tüm storyboard segmentlerinin toplam süresi genel `duration` değerine eşit olmalıdır (varsayılan: "disabled"). | COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Video için ses oluşturur. Yalnızca `kling-v3-omni` için desteklenir (varsayılan: false). | BOOLEAN | Hayır | `true`<br>`false` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; seed değerinden bağımsız olarak sonuçlar deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 arası |

### Storyboard Girdileri

`storyboards` etkinleştirildiğinde, seçilen her storyboard segmenti için aşağıdaki girdiler görünür. N, 1'den seçilen storyboard sayısına kadar değişir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Storyboard segmenti N için istem. En fazla 512 karakter. | STRING | Hayır | 1 ile 512 arası characters |
| `storyboard_N_duration` | Storyboard segmenti N için saniye cinsinden süre (varsayılan: 4). | INT | Hayır | 1 ile 15 arası |

**Not:** `reference_images` girdisi en fazla 7 görsel kabul eder. Daha fazla sağlanırsa düğüm bir hata verir. Her görsel minimum boyut ve en-boy oranı açısından doğrulanır.

**Modele özel kısıtlamalar:**
- `kling-video-o1` 10 saniyeden uzun süreleri desteklemez.
- `kling-video-o1` ses oluşturmayı desteklemez.
- `kling-video-o1` 4k çözünürlüğü desteklemez.
- `kling-video-o1` storyboard'ları desteklemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `ccf7881065d2a365cdaa0e164b8b1d46c67985067866ab0fe91d492a62015f07`
