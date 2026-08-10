# MinimaxHailuo03ReferenceNode

Bu düğüm, sonucu koşullandırmak için referans görseller, videolar ve ses kullanarak MiniMax H3 modeliyle bir video oluşturur. Referanslara istemde bağlantı sırasına göre atıfta bulunulur: "Image 1", "Image 2", "Video 1", "Audio 1" ve benzeri.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model (varsayılan: "MiniMax H3"). "MiniMax H3" seçildiğinde aşağıdaki `prompt`, `duration`, `resolution`, `ratio`, `reference_images`, `reference_videos` ve `reference_audios` ayarları sağlanır. | STRING | Evet | "MiniMax H3" |
| `prompt` | Oluşturulacak videonun metin açıklaması. Referans medyaya sıralarıyla atıfta bulunulabilir, örneğin "Image 1", "Image 2", "Video 1" veya "Audio 1". | STRING | Evet | Minimum uzunluk: 1 karakter |
| `duration` | Oluşturulan videonun saniye cinsinden süresi. | INT | Evet | Birden fazla seçenek mevcuttur |
| `resolution` | Oluşturulan videonun çıktı çözünürlüğü. | STRING | Evet | Birden fazla seçenek mevcuttur |
| `ratio` | Oluşturulan videonun en-boy oranı. | STRING | Evet | Birden fazla seçenek mevcuttur |
| `reference_images` | Bağlantı sırasına göre istemde "Image 1".."Image 9" olarak atıfta bulunulan konu veya stil referans görselleri. En fazla 9 görsel. | IMAGE | Hayır | 0 ila 9 görsel |
| `reference_videos` | Bağlantı sırasına göre istemde "Video 1".."Video 3" olarak atıfta bulunulan hareket veya sahne referans videoları. Her biri 2-15 saniye, toplam 15 saniye olmak üzere en fazla 3 video. | VIDEO | Hayır | 0 ila 3 video |
| `reference_audios` | Bağlantı sırasına göre istemde "Audio 1".."Audio 3" olarak atıfta bulunulan ses referansları. Her biri 2-15 saniye, toplam 15 saniye olmak üzere en fazla 3 kliptir. Bir referans görsel veya video olmadan kullanılamaz. | AUDIO | Hayır | 0 ila 3 klip |
| `seed` | Rastgele tohum (seed). Aynı tohumla yapılan aynı istek benzer sonuçlar verir ancak birebir aynı sonuçları garanti etmez (varsayılan: 42). | INT | Evet | 0 ila 4294967295 |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği (varsayılan: false). | BOOLEAN | Hayır | true<br>false |

### Parametre Kısıtlamaları

- En az bir referans görsel veya bir referans video gereklidir. Tek başına referans ses kabul edilmez.
- Her referans görselin en-boy oranı yaklaşık 0.4 ile 2.5 (2:5 ile 5:2) arasında olmalı ve minimum genişlik ve yüksekliği 256 piksel olmalıdır.
- Her referans video, 23.976 ile 60 FPS arasında bir kare hızıyla 2 ila 15 saniye uzunluğunda olmalıdır. Tüm referans videolarının toplam süresi 15 saniyeyi aşamaz.
- Her referans ses klibi 2 ila 15 saniye uzunluğunda olmalıdır. Tüm referans ses kliplerinin toplam süresi 15 saniyeyi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `beca020333a544188e6c21829eb8e63415aa5299efc676438e85662a5f08660d`
