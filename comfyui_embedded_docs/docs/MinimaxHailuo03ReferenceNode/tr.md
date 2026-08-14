# MiniMax H3 Referans ile Videoya

Bu düğüm, MiniMax H3 modelini kullanarak bir video oluşturur; sonucu koşullandırmak için referans görseller, videolar ve ses kullanır. Referanslara istemde bağlantı sırasına göre atıfta bulunulur: "Image 1", "Image 2", "Video 1", "Audio 1" vb.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model (varsayılan: "MiniMax H3"). "MiniMax H3" seçildiğinde aşağıdaki `prompt`, `resolution`, `ratio`, `duration`, `reference_images`, `reference_videos` ve `reference_audios` ayarları sağlanır. | STRING | Evet | "MiniMax H3" |
| `seed` | Rastgele seed. Aynı seed ile yapılan aynı istek benzer sonuçlar verir, ancak sonuçların birebir aynı olması garanti edilmez (varsayılan: 42). | INT | Evet | 0 ile 4294967295 arası |
| `watermark` | Videoya AIGC filigranı eklenip eklenmeyeceği (varsayılan: false). | BOOLEAN | Hayır | true<br>false |

### MiniMax H3 Girdileri

Bu girdiler, model olarak "MiniMax H3" seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Referans medyaya bağlantı sırasına göre atıfta bulunulabilir; örneğin "Image 1", "Image 2", "Video 1" veya "Audio 1". | STRING | Evet | Min length: 1 character |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | STRING | Evet | "768P"<br>"2K" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "adaptive"). | STRING | Evet | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 4 ile 15 arası |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: 1..9 öğe bağlayın (`image_1`...`image_9`). Konu veya stil referans görselleri; istemde bağlantı sırasına göre "Image 1".."Image 9" olarak anılır. En fazla 9 görsel. | IMAGE | Hayır | 0 ile 9 arası images |
| `reference_videos` | Genişletilebilir yuva: 1..3 öğe bağlayın (`video_1`...`video_3`). Hareket veya sahne referans videoları; istemde bağlantı sırasına göre "Video 1".."Video 3" olarak anılır. Her biri 2-15 saniye olmak üzere en fazla 3 video (toplamda 15 saniye). | VIDEO | Hayır | 0 ile 3 arası videos |
| `reference_audios` | Genişletilebilir yuva: 1..3 öğe bağlayın (`audio_1`...`audio_3`). Ses referansları; istemde bağlantı sırasına göre "Audio 1".."Audio 3" olarak anılır. Her biri 2-15 saniye olmak üzere en fazla 3 klip (toplamda 15 saniye). Referans görsel veya video olmadan kullanılamaz. | AUDIO | Hayır | 0 ile 3 arası clips |

### Parametre Kısıtlamaları

- En az bir referans görsel veya bir referans video gereklidir. Tek başına referans ses kabul edilmez.
- Her referans görselinin en-boy oranı yaklaşık 0.4 ile 2.5 (2:5 ile 5:2) arasında olmalı ve minimum genişliği ile yüksekliği 256 piksel olmalıdır.
- Her referans videosu 2 ila 15 saniye arasında olmalı ve kare hızı 23.976 ile 60 FPS arasında bulunmalıdır. Tüm referans videolarının toplam süresi 15 saniyeyi aşamaz.
- Her referans ses klibi 2 ila 15 saniye arasında olmalıdır. Tüm referans ses kliplerinin toplam süresi 15 saniyeyi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `f7e9c68addda6b48a2366139ecfa28ee57e6cda4aa5cd775c2d769517366573f`
