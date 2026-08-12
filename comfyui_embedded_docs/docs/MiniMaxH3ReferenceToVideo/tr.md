# MiniMax H3 Referanstan Videoya

MiniMax H3 Reference to Video, MiniMax H3 referanstan videoya üretimi için gereken metin koşullandırmasını ve boş video latentini oluşturur. Bir istem ve isteğe bağlı referans görseller, videolar ve ses klipleri sağlarsınız; düğüm bu referansları, modelin üretim sırasında kullanabileceği token'lara kodlar. İstem, referanslara `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | İstemi tokenize etmek ve referans medyayı koşullandırma token'larına kodlamak için kullanılan CLIP modeli. | CLIP | Evet | |
| `vae` | Referans görselleri ve referans video karelerini latent uzaya kodlamak için kullanılan VAE. | VAE | Evet | |
| `audio_vae` | Referans sesi latent uzaya kodlamak için kullanılan VAE (32 kHz ses örnekleme hızı). | VAE | Evet | |
| `prompt` | Video için metin istemi. Referans medyaya `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle (her tür için 1'den başlayan) atıfta bulunulabilir. Çok satırlı ve dinamik istemleri destekler. | STRING | Evet | |
| `genişlik` | Oluşturulan videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ile 16384 (adım 32) |
| `yükseklik` | Oluşturulan videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ile 16384 (adım 32) |
| `uzunluk` | 24 fps'de kare sayısı; 124 = ~5 sn, eğitim aralığı ~124-362'dir (varsayılan: 124). | INT | Evet | 5 ile 3600 (adım 17) |
| `ref_görüntü_boyutu` | Referans görsel boyutlandırma modu. `match`, her referans görseli en-boy oranını koruyarak yalnızca küçültür ve üretimin piksel alanına ölçer; `max`, en iyi kimlik doğruluğu için referans işlem hattının 2048px kısa kenarını kullanır. Referans token'ları tüm örnekleme adımları boyunca iletilir; bu nedenle `max` birkaç kat daha yavaş olabilir (varsayılan: `match`). | COMBO | Evet | `"match"`<br>`"max"` |
| `ref_görüntüler` | İsteğe bağlı referans görseller. Her görsel, daha büyükse 2048px kısa kenara küçültülür ve asla büyütülmez. Birden fazla görsel sağlanabilir. | IMAGE | Hayır | 0 ile 9 |
| `ref_videolar` | İsteğe bağlı referans video kareleri (24 fps, 2-15 sn). Birden fazla video sağlanabilir. | IMAGE | Hayır | 0 ile 3 |
| `ref_video_sesleri` | İsteğe bağlı, referans videolarla dizine göre eşleştirilmiş ses parçaları; `ref_video_audio_N`, aynı numaralı `ref_video_N`'nin ses parçasıdır. | AUDIO | Hayır | 0 ile 3 |
| `ref_sesler` | İsteğe bağlı bağımsız referans ses klipleri. | AUDIO | Hayır | 0 ile 3 |

Notlar:
- İstem, referans medyaya her tür için 1'den başlayan etiketlerle atıfta bulunur: görseller için `<Picture i>`, videolar için `<Video k>` ve ses için `<Audio j>`. Referanslar modele sabit bir sırayla sunulur: önce görseller, sonra videolar (her ses parçasının `<Audio j>` etiketi, kendi `<Video k>` etiketinden hemen önce olacak şekilde), ardından bağımsız sesler.
- Referans videolar en az 5 kare içermelidir (24 fps'de ~0,2 saniye), aksi takdirde düğüm bir hata verir. Video kareleri ayrıca seçilen `length` ile sınırlandırılır ve desteklenen bir kare sayısına kırpılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | MiniMax H3 modeli tarafından kullanılan, kodlanmış istem ile kodlanmış referans görsel, video ve ses token'larını birlikte içeren koşullandırma. | CONDITIONING |
| `latent` | İstenen `genişlik`, `yükseklik` ve `uzunluk` (kare sayısı) değerlerinde boş ses-video latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `529e51c5c9c63a94176a15851f40ac42f7bd93e7d7c6ad334ed22aa29d04dfde`
