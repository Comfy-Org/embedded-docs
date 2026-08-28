# MiniMax H3 Metinden Videoya

Bu düğüm, MiniMax H3 modelini kullanarak bir metin isteminden video oluşturur. Metni, çözünürlük, en-boy oranı ve süre gibi video ayarlarıyla birlikte MiniMax API'sine gönderir, oluşturma görevinin tamamlanmasını bekler ve ortaya çıkan videoyu döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. (varsayılan: "MiniMax H3"). Bu modelin seçilmesi ayrıca oluşturulan video için metin istemi, çözünürlük, oran ve süre ayarlarını sağlar (aşağıdaki MiniMax H3 Girdileri'ne bakın). | DYNAMIC_COMBO | Evet | `"MiniMax H3"` |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer, ancak birebir aynı olması garanti edilmeyen sonuçlar verir. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |

### MiniMax H3 Girdileri

Bu ayarlar, "MiniMax H3" modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. | STRING | Evet | Any text |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "768P"<br>"2K" |
| `ratio` | Çıktı videosunun en-boy oranı. (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). (varsayılan: 5) | INT | Evet | 4 ile 15 |

Not: `model` seçeneğine dahil edilen metin istemi en az bir boşluk olmayan karakter içermelidir. Bu düğüm için gösterilen tahmini fiyat, seçilen çözünürlük ve video süresine göre hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Sağlanan metin isteminden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `93f7c81ba4053da999d29392bce23f7fd809d21876ea489747d203201ed0377f`
