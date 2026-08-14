# Kling Omni İlk-Son-Kare'den Videoya (Pro)

Bu düğüm, bir başlangıç karesinden, isteğe bağlı bir bitiş karesinden veya referans görüntülerinden video oluşturmak için en son Kling AI modelini kullanır. Tek bir video veya her bölüm için ayrı istemler ve süreler içeren çok çekimli bir storyboard oluşturabilir. Düğüm, bu girdileri işleyerek belirtilen uzunluk ve çözünürlükte, isteğe bağlı ses üretimiyle birlikte bir video üretir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Video oluşturma için kullanılacak belirli Kling AI modeli. | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Video içeriğini açıklayan metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. Storyboard'lar etkinleştirildiğinde yok sayılır. | STRING | Evet | - |
| `duration` | Oluşturulan videonun saniye cinsinden istenen uzunluğu (varsayılan: 5). | INT | Evet | 3 ila 15 |
| `first_frame` | Video dizisi için başlangıç görüntüsü. | IMAGE | Evet | - |
| `end_frame` | Video için isteğe bağlı bir bitiş karesi. `reference_images` ile aynı anda kullanılamaz. Storyboard'larla çalışmaz. | IMAGE | Hayır | - |
| `reference_images` | En fazla 6 ek referans görüntüsü. | IMAGE | Hayır | - |
| `resolution` | Oluşturulan video için çıktı çözünürlüğü (varsayılan: "1080p"). | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Her biri için ayrı istemler ve süreler içeren bir dizi video bölümü oluşturun. Yalnızca `kling-v3-omni` için desteklenir. Etkinleştirildiğinde, her storyboard bir istem ve süre girdisi gerektirir. | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Video için ses oluşturun (varsayılan: False). Yalnızca `kling-v3-omni` için desteklenir. | BOOLEAN | Hayır | True / False |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |

### Storyboard Girdileri

`storyboards` değeri `"disabled"` dışında bir değere ayarlandığında, seçilen her bölüm için aşağıdaki girdiler eklenir (N, 1'den seçilen storyboard sayısına kadar değişir):

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Storyboard bölümü N için istem. En fazla 512 karakter. (varsayılan: "") | STRING | Evet | - |
| `storyboard_N_duration` | Storyboard bölümü N için saniye cinsinden süre (varsayılan: 4). | INT | Evet | 1 ila 15 |

**Önemli Kısıtlamalar:**

* `end_frame` girdisi, `reference_images` girdisiyle aynı anda kullanılamaz.
* `end_frame` girdisi, storyboard'larla aynı anda kullanılamaz.
* `kling-video-o1` modeli, 10 saniyeden uzun süreleri, ses üretimini, 4k çözünürlüğü veya storyboard'ları desteklemez.
* `kling-video-o1` modelinde bir `end_frame` veya herhangi bir `reference_images` sağlamazsanız, `duration` yalnızca 5 veya 10 saniye olarak ayarlanabilir.
* Tüm girdi görüntüleri (`first_frame`, `end_frame` ve herhangi bir `reference_images`) hem genişlikte hem de yükseklikte minimum 300 piksel boyutuna sahip olmalıdır.
* Tüm girdi görüntülerinin en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.
* `reference_images` girdisi aracılığıyla en fazla 6 görüntü sağlanabilir.
* `prompt` metni 1 ile 2500 karakter uzunluğunda olmalıdır (storyboard'lar etkinleştirildiğinde 0 karaktere izin verilir).
* İstem, girdi görüntülerine `@image`, `@image1`, `@image2` vb. yer tutucularını kullanarak başvurabilir; bunlar otomatik olarak API uyumlu görüntü referans biçimine dönüştürülür.
* Storyboard'lar etkinleştirildiğinde, tüm storyboard bölümlerinin toplam süresi genel `duration` değerine eşit olmalıdır.
* Her storyboard istemi 1 ile 512 karakter uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`
