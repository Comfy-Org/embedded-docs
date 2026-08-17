# Grok Referans-Video

Grok Reference-to-Video düğümü, çıktının stilini ve içeriğini yönlendirmek için en fazla yedi referans görseli kullanarak bir metin isteminden video üretir. `grok-imagine-video-1.5` modeliyle, en fazla üç ön tanımlı ses referansı ekleyebilir ve istemde doğrudan `@ImageN` ve `@AudioN` etiketlerini kullanarak görsellere ve seslere atıfta bulunabilirsiniz. Düğüm, isteği harici bir API'ye gönderir, üretimin tamamlanmasını bekler ve sonuçta oluşan videoyu indirir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. | DYNAMIC_COMBO | Evet | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `istem` | İstenen videonun metin açıklaması. Boş olmayan bir string olmalıdır. | STRING | Evet | N/A |
| `tohum` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 arası |

### Grok Imagine Video 1.5 Girdileri

`model` parametresi `grok-imagine-video-1.5` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice_1` | İsteğe bağlı ön tanımlı ses referansı; istemde @Audio1 olarak atıfta bulunun. API yalnızca bu ön tanımlı sesleri destekler, özel sesleri desteklemez (varsayılan: none). | COMBO | Hayır | Ön tanımlı ses seçenekleri (`"none"` dahil) |
| `voice_2` | İsteğe bağlı ikinci ses referansı; istemde @Audio2 olarak atıfta bulunun (varsayılan: none). | COMBO | Hayır | Ön tanımlı ses seçenekleri (`"none"` dahil) |
| `voice_3` | İsteğe bağlı üçüncü ses referansı; istemde @Audio3 olarak atıfta bulunun (varsayılan: none). | COMBO | Hayır | Ön tanımlı ses seçenekleri (`"none"` dahil) |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). | INT | Evet | 1 ile 15 arası |

### Grok Imagine Video Girdileri

`model` parametresi `grok-imagine-video` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). | INT | Evet | 2 ile 10 arası |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: video oluşturmayı yönlendirmek için 1 ila 7 referans görseli bağlayın. `grok-imagine-video-1.5` ile istemde bunlara girdi sırasına göre numaralandırılmış şekilde @Image1 ... @Image7 olarak atıfta bulunun; toplu bir girdi her görsel için bir kez sayılır. | IMAGE | Evet | 1 ila 7 görsel |

**Not:** Görüntülenen alt parametreler seçilen `model`'e bağlıdır; `grok-imagine-video-1.5`, `voice_1`, `voice_2` ve `voice_3` girdilerini ekler. En az bir referans görseli gereklidir ve toplam 7 ile sınırlıdır (toplu bir girdi her görsel için bir kez sayılır). `grok-imagine-video-1.5` ile istem, bağlı görsellere `@Image1` ... `@Image7` ve etkin seslere `@Audio1`, `@Audio2`, `@Audio3` olarak atıfta bulunabilir; bağlı olmayan bir görsele veya `none` olarak ayarlanmış bir sese atıfta bulunmak hataya neden olur. API yalnızca ön tanımlı sesleri destekler, özel sesleri desteklemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `ac068b34ad7efe786d29f51052a623eaf324041a99b124f6b5f81fadea661a83`
