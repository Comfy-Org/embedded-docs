# Grok Referans-Video

Grok Reference-to-Video düğümü, bir metin isteminden video üretir; çıktının stilini ve içeriğini yönlendirmek için en fazla yedi referans görseli kullanır. `grok-imagine-video-1.5` modeliyle, en fazla üç önceden tanımlı ses referansı ekleyebilir ve `@ImageN` ile `@AudioN` etiketlerini kullanarak görsellere ve seslere doğrudan istemde atıfta bulunabilirsiniz. Düğüm isteği harici bir API'ye gönderir, üretimin tamamlanmasını bekler ve ortaya çıkan videoyu indirir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak model. | DYNAMIC_COMBO | Evet | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `istem` | İstenen videonun metin açıklaması. Boş olmayan bir dize olmalıdır. | STRING | Evet | N/A |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum (seed); gerçek sonuçlar tohumdan bağımsız olarak belirleyici değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 arası |

### Grok Imagine Video 1.5 Girdileri

`model` `grok-imagine-video-1.5` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice_1` | İsteğe bağlı önceden tanımlı ses referansı; istemde @Audio1 olarak atıfta bulunun. API yalnızca bu önceden tanımlı sesleri destekler, özel sesi desteklemez (varsayılan: yok). | COMBO | Hayır | Önceden tanımlı ses seçenekleri, `"none"` dahil |
| `voice_2` | İsteğe bağlı ikinci ses referansı; istemde @Audio2 (varsayılan: yok). | COMBO | Hayır | Önceden tanımlı ses seçenekleri, `"none"` dahil |
| `voice_3` | İsteğe bağlı üçüncü ses referansı; istemde @Audio3 (varsayılan: yok). | COMBO | Hayır | Önceden tanımlı ses seçenekleri, `"none"` dahil |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). | INT | Evet | 1 ile 15 arası |

### Grok Imagine Video Girdileri

`model` `grok-imagine-video` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 6). | INT | Evet | 2 ile 10 arası |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: Video üretimini yönlendirmek için 1 ila 7 referans görseli bağlayın. `grok-imagine-video-1.5` ile, istemde bunlara @Image1 ... @Image7 olarak atıfta bulunun; girdi sırasına göre numaralandırılır; toplu girdi her görsel için bir kez sayılır. | IMAGE | Evet | 1 ile 7 görsel arası |

**Not:** Görüntülenen alt parametreler seçili `model`e bağlıdır; `grok-imagine-video-1.5`, `voice_1`, `voice_2` ve `voice_3` girdilerini ekler. En az bir referans görseli gereklidir ve toplam 7 ile sınırlıdır (toplu girdi her görsel için bir kez sayılır). `grok-imagine-video-1.5` ile istem, bağlı görsellere `@Image1` ... `@Image7` ve ses yuvalarına `@Audio1`, `@Audio2`, `@Audio3` olarak atıfta bulunabilir; numarasız `@image` veya `@audio` ilkine atıfta bulunur. `@AudioN`, `voice_N` widget'ına atıfta bulunur, etkin seslerin sırasına değil. Bağlı olmayan bir görsele veya `none` olarak ayarlanmış bir ses yuvasına atıfta bulunmak hataya neden olur. API yalnızca önceden tanımlı sesleri destekler, özel sesi desteklemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `e584c450563eaa7fcb7751d2325f9ef847fa34a4342df01f2bd9ce2e4ff8f2c3`
