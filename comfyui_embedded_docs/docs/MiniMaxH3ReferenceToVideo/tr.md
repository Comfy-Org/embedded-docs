# MiniMax H3 Referanstan Videoya

MiniMax H3 Referanstan Videoya düğümü, MiniMax H3 referanstan videoya üretimi için gereken metin koşullandırmasını ve boş ses-video latentini oluşturur. Bir prompt ve isteğe bağlı referans görüntüler, videolar ve ses klipleri sağlarsınız; düğüm bu referansları modelin üretim sırasında kullanabileceği tokenlara kodlar. Prompt, referanslara `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Promptu tokenize etmek ve referans medyayı koşullandırma tokenlarına kodlamak için kullanılan CLIP modeli. | CLIP | Evet | |
| `vae` | Referans görüntüleri ve referans video karelerini latent uzaya kodlamak için kullanılan VAE. | VAE | Evet | |
| `audio_vae` | Referans sesi latent uzaya kodlamak için kullanılan VAE. Ses, ses VAE örnekleme hızına (varsayılan 32 kHz) yeniden örneklenir. | VAE | Evet | |
| `prompt` | Video için metin promptu. Referans medyaya `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle atıfta bulunulabilir (her tür için 1 tabanlı). Çok satırlı ve dinamik promptları destekler. | STRING | Evet | |
| `genişlik` | Oluşturulan videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ila 16384 (adım 32) |
| `yükseklik` | Oluşturulan videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ila 16384 (adım 32) |
| `uzunluk` | 24 fps'de kare sayısı; 124 = ~5 sn, eğitilen aralık ~124-362'dir (varsayılan: 124). | INT | Evet | 5 ila 3600 (adım 17) |
| `ref_görüntü_boyutu` | Referans görüntü boyutlandırması. `match`, her referans görüntüsünü üretimin piksel alanına en-boy oranını koruyarak yalnızca küçültür; `max`, en iyi kimlik doğruluğu için referans hattının 2048px kısa kenarını kullanır. Referans tokenları her örnekleme adımında taşınır, bu nedenle `max` birkaç kat daha yavaş olabilir (varsayılan: `match`). | COMBO | Evet | `"match"`<br>`"max"` |
| `ref_görüntüler` | Büyüyen yuva: 1 ila 9 referans görüntüsü bağlayın (`ref_image_1` ... `ref_image_9`). Her görüntü daha büyükse 2048px kısa kenara küçültülür ve asla büyütülmez. | IMAGE | Hayır | 0 ila 9 |
| `ref_videolar` | Büyüyen yuva: 1 ila 3 referans videosu bağlayın (`ref_video_1` ... `ref_video_3`). 24 fps'de referans video kareleri (2-15 sn). | IMAGE | Hayır | 0 ila 3 |
| `ref_video_sesleri` | Büyüyen yuva: 1 ila 3 ses parçası bağlayın (`ref_video_audio_1` ... `ref_video_audio_3`). Aynı numaralı referans videosunun ses parçası. | AUDIO | Hayır | 0 ila 3 |
| `ref_sesler` | Büyüyen yuva: 1 ila 3 bağımsız referans ses klibi bağlayın (`ref_audio_1` ... `ref_audio_3`). | AUDIO | Hayır | 0 ila 3 |

Notlar:

- Prompt, referans medyaya her tür için 1 tabanlı etiketlerle atıfta bulunur: görüntüler için `<Picture i>`, videolar için `<Video k>` ve ses için `<Audio j>`. Referanslar modele sabit bir sırayla sunulur: görüntüler, ardından videolar (her ses parçasının `<Audio j>` etiketi, kendi `<Video k>` etiketinden hemen önce), ardından bağımsız ses.
- Referans videolar en az 5 kare içermelidir (~24 fps'de ~0,2 saniye), aksi takdirde düğüm bir hata verir. Video kareleri ayrıca seçilen `length` ile sınırlandırılır ve desteklenen bir kare sayısına kırpılır.
- İstenen `length`, latent oluşturulmadan önce desteklenen bir kare sayısına hizalanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | MiniMax H3 modeli tarafından kullanılan, kodlanmış prompt ile birlikte kodlanmış referans görüntü, video ve ses tokenlarını içeren koşullandırma. | CONDITIONING |
| `latent` | İstenen `width`, `height` ve `length` (kare sayısı) değerlerinde boş ses-video latenti. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
