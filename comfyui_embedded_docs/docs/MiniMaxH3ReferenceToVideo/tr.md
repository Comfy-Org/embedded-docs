# MiniMax H3 Referanstan Videoya

MiniMax H3 Referanstan Videoya, MiniMax H3 referanstan videoya üretimi için gereken metin koşullandırmasını ve boş ses-video latentini oluşturur. Bir istem ile isteğe bağlı referans görüntüleri, videoları ve ses kliplerini sağlarsınız; düğüm bu referansları modelin üretim sırasında kullanabileceği tokenlara kodlar. İstem, referanslara `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | İstemi tokenize etmek ve referans medyayı koşullandırma tokenlarına kodlamak için kullanılan CLIP modeli. | CLIP | Evet | |
| `vae` | Referans görüntüleri ve referans video karelerini latent uzaya kodlamak için kullanılan VAE. | VAE | Evet | |
| `audio_vae` | Referans sesi latent uzaya kodlamak için kullanılan VAE (32 kHz ses örnekleme hızı). | VAE | Evet | |
| `prompt` | Video için metin istemi. Referans medyaya `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle (her tür için 1 tabanlı) atıfta bulunulabilir. Çok satırlı ve dinamik istemleri destekler. | STRING | Evet | |
| `width` | Oluşturulan videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ila 16384 (adım 32) |
| `height` | Oluşturulan videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ila 16384 (adım 32) |
| `length` | 24 fps'de kare sayısı; 124 = ~5sn, eğitilmiş aralık ~124-362'dir (varsayılan: 124). | INT | Evet | 5 ila 3600 (adım 17) |
| `ref_image_size` | Referans görüntü boyutlandırma modu. `match` her referans görüntüsünü yalnızca küçülterek en-boy oranını koruyarak üretimin piksel alanına ölçekler; `max` en iyi kimlik doğruluğu için referans hattının 2048px kısa kenarını kullanır. Referans tokenları her örnekleme adımında taşındığından `max` birkaç kat daha yavaş olabilir (varsayılan: `match`). | COMBO | Evet | `"match"`<br>`"max"` |
| `ref_images` | İsteğe bağlı referans görüntüleri. Her görüntü, daha büyükse 2048px kısa kenara küçültülür ve asla büyütülmez. Birden fazla görüntü sağlanabilir. | IMAGE | Hayır | 0 ila 9 |
| `ref_videos` | 24 fps'de isteğe bağlı referans video kareleri (2-15sn). Birden fazla video sağlanabilir. | IMAGE | Hayır | 0 ila 3 |
| `ref_video_audios` | Dizinle referans videolarla eşleştirilmiş isteğe bağlı ses parçaları; `ref_video_audio_N`, aynı numaralı `ref_video_N`'nin ses parçasıdır. | AUDIO | Hayır | 0 ila 3 |
| `ref_audios` | İsteğe bağlı bağımsız referans ses klipleri. | AUDIO | Hayır | 0 ila 3 |

Notlar:
- İstem, referans medyaya tür başına 1 tabanlı etiketlerle atıfta bulunur: görüntüler için `<Picture i>`, videolar için `<Video k>` ve ses için `<Audio j>`. Referanslar modele sabit bir sırayla sunulur: görüntüler, ardından videolar (her video parçasının `<Audio j>` etiketi, kendi `<Video k>` etiketinden hemen önce gelir) ve ardından bağımsız ses.
- Referans videolar en az 5 kare içermelidir (~24 fps'de ~0,2 saniye), aksi takdirde düğüm bir hata verir. Video kareleri seçilen `length` ile sınırlandırılır ve desteklenen bir kare sayısına kırpılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | MiniMax H3 modeli tarafından kullanılan kodlanmış istem ile birlikte kodlanmış referans görüntü, video ve ses tokenlarını içeren koşullandırma. | CONDITIONING |
| `latent` | İstenen `width`, `height` ve `length` (kare sayısı) değerlerinde boş ses-video latenti. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
