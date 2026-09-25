# Text Encode Ming Image Edit

Text Encode Ming Image Edit, Ming görüntü düzenleme için bir metin istemini koşullandırmaya kodlar; isteğe bağlı olarak referans görüntüleri de karıştırır. İstem ve referans görüntüleri bir CLIP modeli tarafından tokenize edilir ve bir VAE bağlandığında referans görüntüleri ayrıca koşullandırmaya eklenen latent karelerine kodlanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | İstem ve referans görüntüleri tokenize etmek için kullanılan CLIP modeli. | CLIP | Evet | - |
| `vae` | Referans görüntüleri, koşullandırmaya eklenen latent karelere kodlayan isteğe bağlı VAE. VAE olmadan görüntüler, metin kodlayıcıyı yalnızca görü kulesi aracılığıyla koşullandırır. | VAE | Hayır | - |
| `prompt` | Kodlanacak metin istemi. Çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet | Çok satırlı metin |
| `images` | Büyütülebilir yuva: metin kodlayıcı tarafından görülen ve latent dizisine temiz kareler olarak eklenen isteğe bağlı referans görüntüler. 1..8 görüntü bağlayın (`image_1`, `image_2`, ...); sonraki görüntüler ilkine yeniden boyutlandırılır ve örneklenen latent onun boyutuyla eşleşmelidir. Yalnızca RGB kanalları kullanılır. | IMAGE | Hayır | 0 ile 8 arası |

**Not:** Referans görüntüler, yuva adlarının sayısal sırasına göre okunur ve boş yuvalar yok sayılır. Referans latentleri yalnızca hem `vae` hem de en az bir görüntü sağlandığında üretilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `CONDITIONING` | Kodlanmış istemi ve bir VAE ile referans görüntüler sağlandığında referans latentlerini içeren koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMingImageEdit/tr.md)

---
**Source fingerprint (SHA-256):** `675fb3cc0af006e1284fdb2a5ca2c268c540ee92e1ede90b2359f4e3fc8ba5ea`
