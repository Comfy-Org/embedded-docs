# MinimaxHailuo03RegenerateNode

Bu düğüm, MiniMax H3 768P video çıktısını 2K çözünürlükte yeniden işler. Değiştirilmemiş 768P videoyu ve onu oluşturmak için kullanılan istemi yükler, bir MiniMax H3 yeniden oluşturma işi başlatır ve yeniden işlenmiş 2K videoyu döndürür. Orijinal üretimde ilk veya son kareler ya da referans medyası kullanıldıysa, aynı girdileri ekleyin.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video yeniden oluşturma için kullanılacak model. "MiniMax H3" seçildiğinde istem, çözünürlük ve referans medya ayarları görüntülenir. | DYNAMIC_COMBO | Evet | "MiniMax H3" |
| `video` | Yeniden işlenecek MiniMax H3 768P çıktı videosu. MiniMax H3 video düğümünün değiştirilmemiş çıktısını bağlayın (24 FPS, 4-15 saniye). 2K çıktılar kullanılamaz. | VIDEO | Evet | 24 FPS, 4-15 saniye |
| `first_frame` | Orijinal üretimde kullanıldıysa, ilk kare görseli. | IMAGE | Hayır | Görsel |
| `last_frame` | Orijinal üretimde kullanıldıysa, son kare görseli. | IMAGE | Hayır | Görsel |
| `watermark` | Videoya AIGC filigranı eklenip eklenmeyeceği. Varsayılan false değerindedir. | BOOLEAN | Evet | false / true |

### MiniMax H3 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Kaynak videoyu oluşturmak için kullanılan istemin aynısı. Boş olmamalıdır. | STRING | Evet | Metin (çok satırlı) |
| `resolution` | Kaynak videonun yeniden işleneceği çözünürlük. | COMBO | Evet | "2K" |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: `image_1` ile `image_9` arasındaki görselleri bağlayın (en fazla 9 görsel). Orijinal üretimdeki referans görselleri, aynı sırayla. | IMAGE | Hayır | 0-9 görsel |
| `reference_videos` | Genişletilebilir yuva: `video_1` ile `video_3` arasındaki videoları bağlayın (en fazla 3 video). Orijinal üretimdeki referans videoları, aynı sırayla. | VIDEO | Hayır | 0-3 video |
| `reference_audios` | Genişletilebilir yuva: `audio_1` ile `audio_3` arasındaki klipleri bağlayın (en fazla 3 klip). Orijinal üretimdeki ses referansları, aynı sırayla. Bir referans görsel veya video olmadan kullanılamaz. | AUDIO | Hayır | 0-3 klip |

### Kısıtlamalar

- `prompt` boş olmamalıdır.
- Kaynak `video`, değiştirilmemiş bir MiniMax H3 768P çıktısı olmalıdır: 24 FPS, genişlik ve yükseklik 32'ye bölünebilir, toplamda en fazla 1.032.192 piksel ve 17'şer adımlarla 107 ila 362 kare (24 FPS'te 4 ila 15 saniye). 2K çıktılar kaynak olarak kullanılamaz.
- `first_frame` ve `last_frame`, referans medyasıyla (`reference_images`, `reference_videos`, `reference_audios`) birbirini dışlar. Görüntüden videoya istem için kareleri, referanstan videoya istem için referans medyasını kullanın.
- `reference_audios`, en az bir `reference_images` veya `reference_videos` girdisi gerektirir.
- `first_frame`, `last_frame` ve her `reference_image` en-boy oranı 0,4 ile 2,5 arasında olmalı ve en az 256x256 piksel boyutunda olmalıdır.
- `reference_videos`: her video 23,976 ile 60 FPS arasında ve 2-15 saniye uzunluğunda olmalıdır; toplam süre 15 saniyeyi aşamaz.
- `reference_audios`: her klip 2-15 saniye uzunluğunda olmalıdır; toplam süre 15 saniyeyi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | MiniMax H3 videosunun 2K çözünürlükte yeniden işlenmiş hâli. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/tr.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
