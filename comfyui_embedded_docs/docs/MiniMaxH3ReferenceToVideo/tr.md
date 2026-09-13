# MiniMax H3 Referanstan Videoya

MiniMax H3 Reference to Video, MiniMax H3 referanstan videoya üretimi için gereken metin koşullandırmasını ve boş ses-video latentini oluşturur. Bir istem ile isteğe bağlı referans görseller, videolar ve ses klipleri sağlarsınız; düğüm bu referansları modelin üretim sırasında kullanabileceği koşullandırmaya kodlar. İstem, referanslara `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | İstemi tokenize etmek ve referans medyayı koşullandırma tokenlarına kodlamak için kullanılan CLIP modeli. | CLIP | Evet | |
| `vae` | Video VAE. Bu olmadan referans görseller/videolar yalnızca metin kodlayıcıyı koşullandırır. | VAE | Hayır | |
| `audio_vae` | Ses VAE. Bu olmadan referans ses yalnızca metin kodlayıcıyı koşullandırır. | VAE | Hayır | |
| `prompt` | Video için metin istemi. Referans medyaya `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle atıfta bulunulabilir (her tür için 1 tabanlı). Çok satırlı ve dinamik istemleri destekler. | STRING | Evet | |
| `genişlik` | Oluşturulan videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ile 16384 (adım: 32) |
| `yükseklik` | Oluşturulan videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ile 16384 (adım: 32) |
| `uzunluk` | 24 fps'te kare sayısı, (124 = ~5 sn, eğitilmiş aralık ~124-362) (varsayılan: 124). | INT | Evet | 5 ile 3600 (adım: 17) |
| `ref_görüntü_boyutu` | Referans görsel boyutlandırma. `match`, her referansı (yalnızca küçültme, en boy oranını koruyarak) üretimin piksel alanına ölçekler; `max`, en iyi kimlik sadakati için referans işlem hattının 2048 piksel kısa kenarını kullanır. Referans tokenları her örnekleme adımından geçer, bu nedenle `max` birkaç kat daha yavaş olabilir (varsayılan: `match`). | COMBO | Evet | `"match"`<br>`"max"` |
| `ref_görüntüler` | Genişletilebilir yuva: 9 adede kadar referans görsel bağlayın (`ref_image_1` ... `ref_image_9`). Referans görsel (daha büyükse 2048 kısa kenara küçültülür, asla büyütülmez). | IMAGE | Hayır | 0 ile 9 |
| `ref_videolar` | Genişletilebilir yuva: 3 adede kadar referans video bağlayın (`ref_video_1` ... `ref_video_3`). 24 fps'te referans video kareleri (2-15 sn). | IMAGE | Hayır | 0 ile 3 |
| `ref_video_sesleri` | Genişletilebilir yuva: 3 adede kadar ses parçası bağlayın (`ref_video_audio_1` ... `ref_video_audio_3`). Aynı numaralı referans videonun ses parçası. | AUDIO | Hayır | 0 ile 3 |
| `ref_sesler` | Genişletilebilir yuva: 3 adede kadar bağımsız referans ses klibi bağlayın (`ref_audio_1` ... `ref_audio_3`). Bağımsız referans sesi. | AUDIO | Hayır | 0 ile 3 |

Notlar:

- İstem, referans medyaya her tür için 1 tabanlı etiketlerle atıfta bulunur: görseller için `<Picture i>`, videolar için `<Video k>` ve ses için `<Audio j>`. Referanslar modele sabit bir sırayla sunulur: önce görseller, sonra videolar (her ses parçasının `<Audio j>` etiketi kendi `<Video k>` etiketinden hemen önce olacak şekilde), sonra bağımsız ses.
- `ref_video_audio_N` girişine bağlanan bir ses parçası, `ref_video_N` girişine bağlanan referans videoyla birlikte kullanılır.
- Referans videolar en az 5 kare içermelidir (24 fps'te ~0,2 saniye), aksi halde düğüm bir hata verir. İstenen `length` değerinin ötesindeki kareler kırpılır ve kalan kare sayısı model tarafından desteklenen bir değere ayarlanır.
- İstenen `length`, latent oluşturulmadan önce desteklenen bir kare sayısına hizalanır.
- `vae` olmadan, referans görseller ve videolar yalnızca metin kodlayıcıyı koşullandırır (referans latentleri üretilmez). `audio_vae` olmadan, referans ses yalnızca metin kodlayıcıyı koşullandırır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Kodlanmış istemi içeren koşullandırma. Referans medya ve ilgili VAE'ler sağlandığında, MiniMax H3 modeli tarafından kullanılan kodlanmış referans görsel, video ve ses içeriğini de içerir. | CONDITIONING |
| `latent` | İstenen `width`, `height` ve `length` (kare sayısı) değerlerinde boş ses-video latent, hizalanmış video latentini ve ses latentini içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
