# MiniMax H3 Image Conditioning

MiniMax H3 Image ile bir istem metnini koşullandırmaya ve boş bir latent'e dönüştürür. Görseller olmadan metinden görsele; görseller bağlandığında onları düzenler ve istem metni onlara `<Picture 1>`, `<Picture 2>` vb. olarak atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | MiniMax H3 Image CLIP modeli; istem metnini varsa referans görsellerle birlikte tokenize eder ve koşullandırmayı kodlar. | CLIP | Evet | - |
| `vae` | MiniMax H3 Image VAE. Onunla birlikte görseller referans latent'ler olarak da sabitlenir; o olmadan yalnızca metin kodlayıcısını koşullandırırlar. | VAE | Hayır | - |
| `prompt` | Neyin oluşturulacağı veya referans görsellerin nasıl düzenleneceği. | STRING | Evet | Çok satırlı metin |
| `width` | Piksel cinsinden çıktı genişliği. 0, `image_1`in referans ölçeklemesinden sonraki genişliğini veya görsel yoksa 2048'i kullanır. Varsayılan: 0. | INT | Evet | 0 ile MAX_RESOLUTION arası (adım: 32) |
| `height` | Piksel cinsinden çıktı yüksekliği. 0, `image_1`in referans ölçeklemesinden sonraki yüksekliğini veya görsel yoksa 2048'i kullanır. Varsayılan: 0. | INT | Evet | 0 ile MAX_RESOLUTION arası (adım: 32) |
| `images` | Büyütülebilir referans görsel grubu, `image_1` ve sonrası; `image_1` düzenlenecek görseldir. İstem metni onlara `<Picture n>` olarak atıfta bulunur. | AUTOGROW | Hayır | 0 ile 100 görsel arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görseller bağlandığında referans latent'lerin eklendiği MiniMax H3 Image örnekleyicisi için koşullandırma. | CONDITIONING |
| `latent` | Tek bir görüntü için boş latent, çıktı boyutunun altıda birinde 24 kanal. | LATENT |

Not: Model 2048x2048 piksel alan için ayarlanmıştır, bu yüzden farklı bir tuval gerekmedikçe `width` ve `height` değerlerini 0 olarak bırakın.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `b0927bbc44ac82e8a23b1edb5470c0cc8945844c326a352d75495ed801d11b1d`
