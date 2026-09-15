# MiniMax H3 Context IR (İstem Geliştirici)

## Genel Bakış

Bu düğüm, metin açıklamanızı ve eklenen tüm medyayı analiz etmek için MiniMax H3 Context IR'yi kullanır, ardından daha güçlü, yapılandırılmış bir video istemi üretir. Döndürülen istem, bir MiniMax H3 video düğümünün istem girişine bağlanacak şekilde tasarlanmıştır; oraya medya eklerseniz, aynı medyayı aynı sırayla ekleyin, çünkü geliştirilmiş istem medyaya konuma göre atıfta bulunur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | İstem geliştirme için kullanılacak model. | DYNAMIC_COMBO | Evet | `"MiniMax H3"` |
| `first_frame` | Oluşturmayı amaçladığınız videonun ilk karesi. Referans medya ile birlikte kullanılamaz. | IMAGE | Hayır | Tek görüntü |
| `last_frame` | Oluşturmayı amaçladığınız videonun son karesi. Referans medya ile birlikte kullanılamaz. | IMAGE | Hayır | Tek görüntü |

### MiniMax H3 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturmayı amaçladığınız videonun açıklaması. Boş olamaz. (varsayılan: `""`) | STRING | Evet | Herhangi bir metin (boş olamaz) |
| `duration` | Oluşturmayı amaçladığınız videonun saniye cinsinden süresi (4-15). (varsayılan: 5) | INT | Evet | 4 - 15 |
| `ratio` | Oluşturmayı amaçladığınız videonun en boy oranı. `"adaptive"` en az bir görüntü, video veya ses girdisi gerektirir. (varsayılan: `"adaptive"`) | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Konu veya stil referans görüntüleri, istemde bağlantı sırasına göre "Image 1".."Image 9" olarak anılır. En fazla 9 görüntü. Genişletilebilir yuva: `image_1`...`image_9` bağlayın. | IMAGE | Hayır | 0 - 9 görüntü |
| `reference_videos` | Hareket veya sahne referans videoları, istemde bağlantı sırasına göre "Video 1".."Video 3" olarak anılır. En fazla 3 video, her biri 2-15 saniye, toplam 15 saniye. Genişletilebilir yuva: `video_1`...`video_3` bağlayın. | VIDEO | Hayır | 0 - 3 video |
| `reference_audios` | Ses referansları, istemde bağlantı sırasına göre "Audio 1".."Audio 3" olarak anılır. En fazla 3 klip, her biri 2-15 saniye, toplam 15 saniye. Bir referans görüntü veya video olmadan kullanılamaz. Genişletilebilir yuva: `audio_1`...`audio_3` bağlayın. | AUDIO | Hayır | 0 - 3 klip |

### Parametre Kısıtlamaları

- `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` ve `reference_audios` girdileri `model` seçenek grubunun bir parçasıdır ve "MiniMax H3" seçildiğinde görünür.
- `first_frame` ve `last_frame` herhangi bir referans medya ile birlikte kullanılamaz.
- En az bir `reference_image` veya `reference_video` de bağlanmadıkça `reference_audios` kullanılamaz.
- Hiçbir kare ve referans medya bağlı değilken `ratio` `"adaptive"` olarak ayarlanamaz.
- Referans videoların her biri yaklaşık 2-15 saniye olmalı ve toplam süre 15 saniyeyi aşmamalıdır. Kare hızları 23.9 ile 60.5 FPS arasında olmalıdır.
- Referans seslerin her biri yaklaşık 2-15 saniye olmalı ve toplam süre 15 saniyeyi aşmamalıdır.
- `first_frame`, `last_frame` ve her referans görüntü en az 256x256 piksel olmalı ve en boy oranı 0.4 ile 2.5 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `STRING` | MiniMax H3 Context IR tarafından oluşturulan geliştirilmiş, yapılandırılmış video istemi. Bir MiniMax H3 video oluşturma düğümünün istem girişine bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/tr.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
