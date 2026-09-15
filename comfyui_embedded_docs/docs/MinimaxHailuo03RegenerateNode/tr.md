# MiniMax H3'ü 2K Olarak Yeniden Oluştur

Bu düğüm, bir MiniMax H3 768P video çıktısını 2K çözünürlükte yeniden render eder. Değiştirilmemiş 768P videoyu ve onu oluşturmak için kullanılan tam istemi yükler, bir MiniMax H3 yeniden oluşturma işi başlatır ve yeniden render edilmiş 2K videoyu döndürür. Orijinal oluşturma ilk veya son kareleri ya da referans medyayı kullandıysa, aynı girdileri ekleyin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video yeniden oluşturma için kullanılacak model. "MiniMax H3" seçildiğinde istem, çözünürlük ve referans medya ayarları görünür. | DYNAMIC_COMBO | Evet | "MiniMax H3" |
| `video` | Yeniden render edilecek MiniMax H3 768P çıktı videosu. Bir MiniMax H3 video düğümünün değiştirilmemiş çıktısını bağlayın (24 FPS, 4-15 saniye). 2K çıktılar kullanılamaz. | VIDEO | Evet | 24 FPS, 4-15 saniye |
| `first_frame` | Orijinal oluşturmada kullanıldıysa, ilk kare görüntüsü. | IMAGE | Hayır | Görsel |
| `last_frame` | Orijinal oluşturmada kullanıldıysa, son kare görüntüsü. | IMAGE | Hayır | Görsel |
| `watermark` | Videoya AIGC filigranı eklenip eklenmeyeceği. Varsayılan değer false'tur. | BOOLEAN | Evet | false / true |

### MiniMax H3 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Kaynak videoyu oluşturmak için kullanılan tam istem. Boş olmamalıdır. | STRING | Evet | Metin (çok satırlı) |
| `resolution` | Kaynak videonun yeniden render edileceği çözünürlük. | COMBO | Evet | "2K" |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: `image_1` ile `image_9` arasını bağlayın (en fazla 9 görsel). Orijinal oluşturmadaki referans görselleri, aynı sırayla. | IMAGE | Hayır | 0-9 görsel |
| `reference_videos` | Genişletilebilir yuva: `video_1` ile `video_3` arasını bağlayın (en fazla 3 video). Orijinal oluşturmadaki referans videoları, aynı sırayla. | VIDEO | Hayır | 0-3 video |
| `reference_audios` | Genişletilebilir yuva: `audio_1` ile `audio_3` arasını bağlayın (en fazla 3 klip). Orijinal oluşturmadaki ses referansları, aynı sırayla. Bir referans görsel veya video olmadan kullanılamaz. | AUDIO | Hayır | 0-3 klip |

### Kısıtlamalar

- `prompt` boş olmamalıdır.
- Kaynak `video`, değiştirilmemiş bir MiniMax H3 768P çıktısı olmalıdır: 24 FPS, genişlik ve yükseklik 32'ye bölünebilir, en fazla 1.032.192 toplam piksel ve 17'lik adımlarla 107 ila 362 kare (24 FPS'de 4 ila 15 saniye). 2K çıktılar kaynak olarak kullanılamaz.
- `first_frame` ve `last_frame`, referans medyayla (`reference_images`, `reference_videos`, `reference_audios`) birbirini dışlar. Görselden videoya istemi için kareleri veya referanstan videoya istemi için referans medyayı kullanın.
- `reference_audios`, en az bir `reference_images` veya `reference_videos` girdisi gerektirir.
- `first_frame`, `last_frame` ve her `reference_image`, 0,4 ile 2,5 arasında bir en-boy oranına sahip olmalı ve en az 256x256 piksel olmalıdır.
- `reference_videos`: her video 23,976 ile 60 FPS arasında ve 2-15 saniye uzunluğunda olmalıdır; toplam süre 15 saniyeyi aşamaz.
- `reference_audios`: her klip 2-15 saniye uzunluğunda olmalıdır; toplam süre 15 saniyeyi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | 2K çözünürlükte yeniden render edilmiş MiniMax H3 videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/tr.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
