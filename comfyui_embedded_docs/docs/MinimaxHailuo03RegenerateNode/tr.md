# MinimaxHailuo03RegenerateNode

Bu düğüm, MiniMax H3 768P video çıktısını 2K çözünürlükte yeniden oluşturur. Kaynak videoyu ve onu oluşturmak için kullanılan birebir promptu yükler, bir MiniMax H3 yeniden oluşturma işi başlatır ve yeniden oluşturulan 2K videoyu döndürür. Orijinal üretimde ilk veya son kareler ya da referans medyası kullanıldıysa, aynı girdileri ekleyin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video yeniden oluşturma için kullanılacak model. Bu model seçildiğinde aşağıda belgelenen prompt, çözünürlük ve referans medya ayarları görüntülenir. | COMBO | Evet | "MiniMax H3" |
| `prompt` | Kaynak videoyu oluşturmak için kullanılan birebir prompt. Boş olmamalıdır. | STRING | Evet | Text |
| `resolution` | Kaynak videonun yeniden oluşturulacağı çözünürlük. | COMBO | Evet | "2K" |
| `reference_images` | Orijinal üretimden referans görseller, aynı sırayla. En fazla 9 görsel. | IMAGE | Hayır | 0-9 images |
| `reference_videos` | Orijinal üretimden referans videolar, aynı sırayla. Her biri 2-15 saniye olmak üzere en fazla 3 video, toplamda 15 saniye. | VIDEO | Hayır | 0-3 videos |
| `reference_audios` | Orijinal üretimden ses referansları, aynı sırayla. Her biri 2-15 saniye olmak üzere en fazla 3 klip, toplamda 15 saniye. Bir referans görsel veya video olmadan kullanılamaz. | AUDIO | Hayır | 0-3 clips |
| `video` | Yeniden oluşturulacak MiniMax H3 768P çıktı videosu. Bir MiniMax H3 video düğümünün değiştirilmemiş çıktısını bağlayın (24 FPS, 4-15 saniye). 2K çıktılar kullanılamaz. | VIDEO | Evet | 24 FPS, 4-15 seconds |
| `first_frame` | Orijinal üretimden ilk kare görseli, eğer kullanıldıysa. | IMAGE | Hayır | Image |
| `last_frame` | Orijinal üretimden son kare görseli, eğer kullanıldıysa. | IMAGE | Hayır | Image |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği. Varsayılan değer false'tur. | BOOLEAN | Evet | false / true |

### Kısıtlamalar

- Kaynak `video`, değiştirilmemiş bir MiniMax H3 768P çıktısı olmalıdır: genişlik ve yükseklik 32'ye bölünebilir olmalı, toplam piksel sayısı en fazla 1,032,192 olmalı, 24 FPS ve 17'şer adımlarla 107 ila 362 kare (24 FPS'de 4 ila 15 saniye) olmalıdır. 2K çıktılar kaynak olarak kullanılamaz.
- `first_frame` / `last_frame` ile referans medyası (`reference_images`, `reference_videos`, `reference_audios`) birbirini dışlar. Görüntüden videoya (image-to-video) promptu için kareleri, referanstan videoya (reference-to-video) promptu için referans medyasını kullanın.
- `reference_audios`, en az bir `reference_images` veya `reference_videos` girdisi gerektirir.
- `reference_images`: her görselin en-boy oranı 0.4 ile 2.5 arasında olmalı ve en az 256x256 piksel boyutunda olmalıdır.
- `reference_videos`: her video 23.976 ile 60 FPS arasında ve 2-15 saniye uzunluğunda olmalıdır; toplam süre 15 saniyeyi aşamaz.
- `reference_audios`: her klip 2-15 saniye uzunluğunda olmalıdır; toplam süre 15 saniyeyi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | 2K çözünürlükte yeniden oluşturulmuş MiniMax H3 videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/tr.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
