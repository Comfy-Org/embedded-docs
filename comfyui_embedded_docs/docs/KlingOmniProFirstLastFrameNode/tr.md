> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/tr.md)

Bu düğüm, bir başlangıç karesi, isteğe bağlı bir bitiş karesi veya referans görüntüleri kullanarak en son Kling AI modeliyle video oluşturur. Her bir bölüm için ayrı istemler ve süreler içeren tek bir video veya çoklu çekimli bir storyboard (hikaye tahtası) oluşturabilir. Bu düğüm, bu girdileri işleyerek belirtilen uzunluk ve çözünürlükte, isteğe bağlı ses üretimiyle bir video üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` | Video oluşturma için kullanılacak belirli Kling AI modeli. |
| `prompt` | STRING | Evet | - | Video içeriğini tanımlayan bir metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. Storyboard'lar etkinleştirildiğinde yok sayılır. |
| `duration` | INT | Evet | 3 ila 15 | Oluşturulan videonun saniye cinsinden istenen uzunluğu (varsayılan: 5). |
| `first_frame` | IMAGE | Evet | - | Video dizisi için başlangıç görüntüsü. |
| `end_frame` | IMAGE | Hayır | - | Video için isteğe bağlı bir bitiş karesi. `reference_images` ile aynı anda kullanılamaz. Storyboard'lar ile çalışmaz. |
| `reference_images` | IMAGE | Hayır | - | En fazla 6 adet ek referans görüntüsü. |
| `resolution` | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` | Oluşturulan video için çıktı çözünürlüğü (varsayılan: "1080p"). |
| `hikaye_tahtaları` | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Her biri ayrı istemler ve süreler içeren bir dizi video bölümü oluşturun. Yalnızca `kling-v3-omni` için desteklenir. Etkinleştirildiğinde, her storyboard bir istem ve süre girdisi gerektirir. |
| `ses_oluştur` | BOOLEAN | Hayır | True / False | Video için ses oluşturun (varsayılan: False). Yalnızca `kling-v3-omni` için desteklenir. |
| `seed` | INT | Hayır | 0 ila 2147483647 | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 0). |

**Önemli Kısıtlamalar:**

* `end_frame` girdisi, `reference_images` girdisi ile aynı anda kullanılamaz.
* `end_frame` girdisi, storyboard'lar ile aynı anda kullanılamaz.
* `kling-video-o1` modeli, 10 saniyeden uzun süreleri, ses oluşturmayı, 4k çözünürlüğü veya storyboard'ları desteklemez.
* `kling-video-o1` modeli ile bir `end_frame` veya herhangi bir `reference_images` sağlamazsanız, `duration` yalnızca 5 veya 10 saniye olarak ayarlanabilir.
* Tüm girdi görüntüleri (`first_frame`, `end_frame` ve tüm `reference_images`) hem genişlik hem de yükseklik olarak minimum 300 piksel boyutunda olmalıdır.
* Tüm girdi görüntülerinin en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır.
* `reference_images` girdisi aracılığıyla en fazla 6 görüntü sağlanabilir.
* `prompt` metni 1 ile 2500 karakter arasında uzunlukta olmalıdır (storyboard'lar etkinleştirildiğinde 0 karaktere izin verilir).
* Storyboard'lar etkinleştirildiğinde, tüm storyboard bölümlerinin toplam süresi, genel `duration` değerine eşit olmalıdır.
* Her storyboard istemi 1 ile 512 karakter arasında uzunlukta olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `bd0fb11242b7f79062079b1aa48c3524abf59ecf06a90f013e57b6910cd8e224`
