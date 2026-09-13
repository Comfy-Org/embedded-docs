# MiniMax H3 Referans ile Videoya

Bu düğüm, referans görüntüler, videolar ve sesle koşullandırılmış olarak MiniMax H3 modellerini kullanarak bir video üretir. Referanslara istemde bağlantı sıralarına göre atıfta bulunulur: "Image 1", "Image 2", "Video 1", "Audio 1" vb. İki model mevcuttur: "MiniMax H3" ve "MiniMax H3 Max".

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak model (varsayılan: "MiniMax H3"). "MiniMax H3" seçildiğinde aşağıdaki MiniMax H3 üretim ve referans girdileri sağlanır. "MiniMax H3 Max" seçildiğinde aşağıdaki MiniMax H3 Max üretim ve referans girdileri sağlanır. | DYNAMIC_COMBO | Evet | "MiniMax H3"<br>"MiniMax H3 Max" |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer sonuçlar verir, ancak aynı sonuçlar garanti edilmez (varsayılan: 42). | INT | Evet | 0 - 4294967295 |
| `watermark` | Videoya AIGC filigranı eklenip eklenmeyeceği (varsayılan: false). Yalnızca MiniMax H3 modeli tarafından desteklenir. | BOOLEAN | Hayır | true<br>false |

### MiniMax H3 Girdileri

Bu girdiler, model olarak "MiniMax H3" seçildiğinde kullanılabilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Referans medyaya sıralarına göre atıfta bulunulabilir; örneğin "Image 1", "Image 2", "Video 1" veya "Audio 1". | STRING | Evet | Minimum 1 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "768P"<br>"2K" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "adaptive"). | COMBO | Evet | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 4 - 15 |

### MiniMax H3 Max Girdileri

Bu girdiler, model olarak "MiniMax H3 Max" seçildiğinde kullanılabilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Referans medyaya sıralarına göre atıfta bulunulabilir; örneğin "Image 1", "Image 2", "Video 1" veya "Audio 1". | STRING | Evet | 1 - 50000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "adaptive"). | COMBO | Evet | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 5 - 15 |
| `prompt_expansion_mode` | Üretimden önce istemi yeniden yazmak için ne kadar çaba harcanacağı (varsayılan: "balanced"). | COMBO | Evet | "balanced"<br>"quality" |
| `reference_detail` | Referans görüntülerin gönderildiği ayrıntı düzeyi. "high", bunları modelin kullandığı en büyük boyutta gönderir (2048 piksele kadar kısa kenar); "standard", referans maliyetini azaltmak için bunları en fazla 2048x1024'e küçültür (varsayılan: "standard"). | COMBO | Evet | "high"<br>"standard" |

### Referans Girdileri

Bu referans girdileri her iki model tarafından paylaşılır. Her biri büyütülebilir bir yuvadır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Büyütülebilir yuva: en fazla 9 öğe bağlayın (`image_1`...`image_9`). İstemde bağlantı sırasına göre "Image 1".."Image 9" olarak atıfta bulunulan konu veya stil referans görüntüleri. En fazla 9 görüntü. | IMAGE | Hayır | 0 - 9 görüntü |
| `reference_videos` | Büyütülebilir yuva: en fazla 3 öğe bağlayın (`video_1`...`video_3`). İstemde bağlantı sırasına göre "Video 1".."Video 3" olarak atıfta bulunulan hareket veya sahne referans videoları. En fazla 3 video, her biri 2-15 saniye, toplam 15 saniye. | VIDEO | Hayır | 0 - 3 video |
| `reference_audios` | Büyütülebilir yuva: en fazla 3 öğe bağlayın (`audio_1`...`audio_3`). İstemde bağlantı sırasına göre "Audio 1".."Audio 3" olarak atıfta bulunulan ses referansları. En fazla 3 klip, her biri 2-15 saniye, toplam 15 saniye. Bir referans görüntü veya video olmadan kullanılamaz. | AUDIO | Hayır | 0 - 3 klip |

### Parametre Kısıtlamaları

- En az bir referans görüntü veya bir referans video gereklidir. Tek başına referans ses kabul edilmez.
- Her referans görüntünün en-boy oranı yaklaşık 0,4 ile 2,5 (2:5 ile 5:2) arasında ve minimum genişlik ve yüksekliği 256 piksel olmalıdır.
- Her referans video 2 ile 15 saniye arasında uzunlukta ve kare hızı 23,976 ile 60 FPS arasında olmalıdır. Tüm referans videoların toplam süresi 15 saniyeyi aşamaz.
- Her referans ses klibi 2 ile 15 saniye arasında uzunlukta olmalıdır. Tüm referans ses kliplerinin toplam süresi 15 saniyeyi aşamaz.
- "MiniMax H3 Max" seçildiğinde, `watermark` ayarı devre dışı bırakılmalıdır.
- "MiniMax H3 Max" seçildiğinde, toplam referans dosyası sayısı (görüntüler, videolar ve sesler birlikte) 12'yi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
