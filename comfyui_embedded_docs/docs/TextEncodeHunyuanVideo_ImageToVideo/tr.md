# MetinKodlamaHunyuanVideo_GörüntüdenVideoya

TextEncodeHunyuanVideo_ImageToVideo düğümü, bir metin istemini referans görselden alınan görsel bilgilerle birleştirerek görüntüden videoya üretimi için koşullandırma verileri oluşturur. Hem metni hem de CLIP görüş çıktısındaki görsel yerleştirmelerini işlemek için bir CLIP modeli kullanır ve ardından bu iki kaynağı `image_interleave` ayarına göre harmanlayan token'lar üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Tokenizasyon ve kodlama için kullanılan CLIP modeli. | CLIP | Evet | - |
| `clip_görü_çıktısı` | Referans görsel için görsel bağlam sağlayan CLIP görüş modelinden alınan görsel yerleştirmeler. | CLIP_VISION_OUTPUT | Evet | - |
| `istem` | Video üretimini yönlendiren metin açıklaması. Çok satırlı girişi ve dinamik istemleri destekler. İstem, modelden referans görsele dayalı olarak videoyu tanımlamasını isteyen bir şablon kullanılarak biçimlendirilir; ana içerik, nesne ayrıntıları, eylemler, arka plan ve kamera açıları gibi yönleri kapsar. | STRING | Evet | - |
| `görüntü_serpiştirme` | Görselin metin istemine kıyasla ne kadar etkili olduğunu belirler. Daha yüksek sayı, metin isteminden daha fazla etki anlamına gelir. (varsayılan: 2) | INT | Evet | 1-512 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Video üretimi için metin ve görsel bilgilerini birleştiren koşullandırma verileri. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
