# Kling 3.0 İlk-Son-Kareden Videoya

Bu düğüm, Kling 3.0 modelini kullanarak video oluşturur. Videoyu bir metin istemine, belirtilen süreye ve sağlanan iki görsele (başlangıç karesi ve bitiş karesi) dayanarak oluşturur. Düğüm, video için eşlik eden ses de oluşturabilir.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model ve oluşturma ayarları. Bu seçeneğin seçilmesi, iç içe bir `resolution` parametresini ortaya çıkarır. | COMBO | Hayır | `"kling-v3"` |
| `prompt` | Video oluşturmayı yönlendiren metin açıklaması. 1 ile 2500 karakter arasında olmalıdır. | STRING | Evet | N/A |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Hayır | 3 ila 15 |
| `first_frame` | Video için başlangıç görseli. En az 300x300 piksel olmalı ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Evet | N/A |
| `end_frame` | Video için bitiş görseli. En az 300x300 piksel olmalı ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Evet | N/A |
| `generate_audio` | Video için ses oluşturulup oluşturulmayacağını kontrol eder (varsayılan: True). | BOOLEAN | Hayır | N/A |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak belirlenimci değildir (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |

### Kling V3 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Oluşturulan video için çözünürlük (varsayılan: `"1080p"`). | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` |

**Not:** `first_frame` ve `end_frame` görselleri, düğümün doğru çalışması için en az 300x300 piksel olmalı ve en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. `prompt` 1 ile 2500 karakter arasında olmalıdır. `resolution` seçeneği bir Kling oluşturma moduna karşılık gelir: `"4k"`, `"1080p"` (pro) ve `"720p"` (standart).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `b71119c3267e2a74d2180e5182463c78828e892bfcf1eeb7c33a0f4d7019997f`
