# MinimaxHailuo03TextToVideoNode

Bu düğüm, MiniMax H3 modelini kullanarak bir metin isteminden video oluşturur. Metni çözünürlük, süre ve en-boy oranı gibi video ayarlarıyla birlikte MiniMax API'sine gönderir ve ortaya çıkan videoyu çıktı olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. (varsayılan: "MiniMax H3"). Bu seçim aynı zamanda oluşturulan video için metin istemini, çözünürlüğü, süreyi ve en-boy oranı ayarlarını da içerir. | COMBO | Evet | `"MiniMax H3"` |
| `seed` | Rastgele tohum. Aynı istek aynı tohumla benzer, ancak birebir aynı olması garanti edilmeyen sonuçlar verir. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |

Not: `model` seçeneğinde bulunan metin istemi en az bir boşluk olmayan karakter içermelidir. Bu düğüm için gösterilen tahmini fiyat, seçilen video süresine göre hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Sağlanan metin isteminden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `9478576dd02ed407a39c95c7227eb8e1482db8b77adc814691fbd807e4cc2893`
