# MinimaxHailuo03ContextIRNode

Bu düğüm, metin açıklamanızı ve eklenen medyayı analiz etmek için MiniMax H3 Context IR kullanır ve ardından daha güçlü, yapılandırılmış bir video promptu üretir. Döndürülen prompt, bir MiniMax H3 video düğümünün prompt girdisine bağlanmak üzere tasarlanmıştır; oraya medya eklerseniz, aynı medyayı aynı sırayla ekleyin; çünkü geliştirilmiş prompt, medyaya konum bazında atıfta bulunur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Prompt geliştirme için kullanılacak model. | COMBO | Evet | `"MiniMax H3"` |
| `first_frame` | Oluşturmak istediğiniz videonun ilk karesi. Referans medya ile birleştirilemez. | IMAGE | Hayır | Tek görsel |
| `last_frame` | Oluşturmak istediğiniz videonun son karesi. Referans medya ile birleştirilemez. | IMAGE | Hayır | Tek görsel |

### MiniMax H3 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturmak istediğiniz videonun açıklaması. Boş olamaz. (varsayılan: `""`) | STRING | Evet | Herhangi bir metin (boş olamaz) |
| `duration` | Oluşturmak istediğiniz videonun süresi, saniye cinsinden (4-15). (varsayılan: 5) | INT | Evet | 4 ile 15 |
| `ratio` | Oluşturmak istediğiniz videonun en-boy oranı. `"adaptive"` en az bir görsel, video veya ses girdisi gerektirir. (varsayılan: `"adaptive"`) | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Konu veya stil referans görselleri; bağlantı sırasına göre promptta "Image 1".."Image 9" olarak anılır. En fazla 9 görsel. Genişletilebilir yuva: `image_1`...`image_9` bağlayın. | IMAGE | Hayır | 0-9 görsel |
| `reference_videos` | Hareket veya sahne referans videoları; bağlantı sırasına göre promptta "Video 1".."Video 3" olarak anılır. En fazla 3 video; her biri 2-15 saniye, toplamda 15 saniye. Genişletilebilir yuva: `video_1`...`video_3` bağlayın. | VIDEO | Hayır | 0-3 video |
| `reference_audios` | Ses referansları; bağlantı sırasına göre promptta "Audio 1".."Audio 3" olarak anılır. En fazla 3 klip; her biri 2-15 saniye, toplamda 15 saniye. Referans görsel veya video olmadan kullanılamaz. Genişletilebilir yuva: `audio_1`...`audio_3` bağlayın. | AUDIO | Hayır | 0-3 klip |

### Parametre Kısıtlamaları

- `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` ve `reference_audios` girdileri `model` seçenek grubunun parçasıdır ve "MiniMax H3" seçildiğinde görünür.
- `first_frame` ve `last_frame` herhangi bir referans medya ile birleştirilemez.
- `reference_audios`, en az bir `reference_image` veya `reference_video` da bağlı değilse kullanılamaz.
- Hiçbir kare ve hiçbir referans medya bağlı değilken, `ratio` değeri `"adaptive"` olarak ayarlanamaz.
- Referans videoları her biri yaklaşık 2-15 saniye olmalı ve toplam süre 15 saniyeyi geçmemelidir. Kare hızları 23.9 ile 60.5 FPS arasında olmalıdır.
- Referans sesleri her biri yaklaşık 2-15 saniye olmalı ve toplam süre 15 saniyeyi geçmemelidir.
- `first_frame`, `last_frame` ve her referans görseli en az 256x256 piksel olmalı ve 0.4 ile 2.5 arasında bir en-boy oranına sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | MiniMax H3 Context IR tarafından oluşturulan geliştirilmiş, yapılandırılmış video promptu. Bir MiniMax H3 video oluşturma düğümünün prompt girdisine bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/tr.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
